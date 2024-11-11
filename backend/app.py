from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Enabling CORS for both localhost and 127.0.0.1
CORS(app, resources={r"/*": {"origins": ["http://localhost", "http://127.0.0.1"]}})

# Initializing an in-memory list to store tasks
tasks = []


@app.route("/")
def home():
    # Home route with a message and available API routes
    return "Welcome to the ToDo API! Available routes: /tasks"


# Route to get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    print("Request received at /tasks with GET")
    return jsonify(tasks)


# Route to add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    print("Request received at /tasks with POST")
    task_data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": task_data.get("title"),
        "done": task_data.get("done", False),
    }
    tasks.append(task)
    return jsonify(task), 201


# Route to update the 'done' status of a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    print(f"Request received at /tasks/{task_id} with PUT")
    task_data = request.get_json()
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["title"] = task_data.get(
            "title", task["title"]
        )  # Update title if provided
        task["done"] = task_data.get("done", task["done"])  # Update 'done' status
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


# Route to delete a task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    print(f"Request received at /tasks/{task_id} with DELETE")
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200


if __name__ == "__main__":
    # Running the app on port 8000, accessible on all IPs
    app.run(host="0.0.0.0", port=8000)
