# Simple Flask TODO App with Docker
This is a simple TODO app designed to demonstrate a **Flask** application. The app serves as a basic TODO list API, and it is used to learn **Docker** step by step through this Medium article:
[https://medium.com/CodeWithSahar/Docker](https://medium.com/CodeWithSahar/)

## Code Versions

You can access each version of the code by clicking on the title, and then follow the instructions in the README file:

- [Add simple Dockerfile for backend Flask app (Lesson 1)](https://github.com/TheSaharFarahzad/todo-app-medium/tree/lesson-1)

## Setup Instructions

### Cloning the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/TheSaharFarahzad/todo-app-medium.git
cd todo-app-medium
```

### Build the Docker Image

Navigate to the backend directory and build the Docker image using the following command:

```bash
cd backend
docker build -t backend-app .
```

### Run the Docker Container

Once the image is built, you can run the Docker container with:

```bash
docker run -p 8000:8000 backend-app
```

### Access the Application

The Flask application starts on port 8000. You can access it in your browser at [http://localhost:8000](http://localhost:8000), and it will show the message: "Welcome to the ToDo API! Available routes: /tasks."

## License

This project is licensed under the MIT License - see the LICENSE file for details.
