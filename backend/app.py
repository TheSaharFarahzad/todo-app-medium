import os
from uuid import UUID, uuid4

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel, Field, ValidationError

# MongoDB connection string from environment variables
MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client.todolist
todos = db.todos

app = Flask(__name__)

# Enabling CORS for localhost and 127.0.0.1
CORS(app, resources={r"/*": {"origins": ["http://localhost", "http://127.0.0.1"]}})


# Pydantic model for Task
class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    title: str
    done: bool = False

    # Serialize UUID manually for JSON response
    def json(self):
        task_dict = self.dict(exclude_unset=True)
        # Check if _id is present, Convert UUID or ObjectId to string
        if "_id" in task_dict:
            task_dict["_id"] = str(task_dict["_id"])
        return task_dict


@app.route("/")
def home():
    return "Welcome to the ToDo API! Available routes: /tasks"


# Route to get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = []
    for task in todos.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return jsonify(tasks)


# Route to add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    task_data = request.get_json()
    try:
        task = Task(**task_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    new_task = task.json()
    result = todos.insert_one(new_task)
    new_task["_id"] = str(result.inserted_id)
    return jsonify(new_task), 201


# Route to update the task (title or done)
@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task_data = request.get_json()

    if not task_data:
        return jsonify({"error": "No data provided for update"}), 400

    # Prepare the update data
    update_data = {}

    if "title" in task_data:
        update_data["title"] = task_data["title"]

    if "done" in task_data:
        # Ensure 'done' is a boolean
        if not isinstance(task_data["done"], bool):
            return jsonify({"error": "'done' must be a boolean value"}), 400
        update_data["done"] = task_data["done"]

    # If no valid fields to update, return an error
    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    # Update the task in MongoDB
    result = todos.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})

    if result.matched_count:
        # Retrieve the updated task to send it back as a response
        updated_task = todos.find_one({"_id": ObjectId(task_id)})
        updated_task["_id"] = str(updated_task["_id"])
        return jsonify(updated_task)

    return jsonify({"error": "Task not found"}), 404


# Route to delete a task by ID
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = todos.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    # Running the app on port 8000, accessible on all IPs
    app.run(host="0.0.0.0", port=8000)
