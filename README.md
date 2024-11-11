# Simple Flask TODO App with Docker
This is a simple TODO app designed to demonstrate a **Flask** application. The app serves as a basic TODO list API and frontend, and it is used to learn **Docker** step by step through this Medium article:
[https://medium.com/@CodeWithSahar/](https://medium.com/@CodeWithSahar/)

## Code Versions

You can access each version of the code by clicking on the title, and then follow the instructions in the README file:

- [Add simple Dockerfile for backend Flask app (Lesson 1)](https://github.com/TheSaharFarahzad/todo-app-medium/tree/lesson-1)
- [Multi-Stage Docker Build for Flask App (Lesson 2)](https://github.com/TheSaharFarahzad/todo-app-medium/tree/lesson-2)
- [Add Frontend with Nginx to Work with Backend (Lesson 3)](https://github.com/TheSaharFarahzad/todo-app-medium/tree/lesson-3)
- [Managing Multiple Containers with Docker Compose (Lesson 4)](https://github.com/TheSaharFarahzad/todo-app-medium/tree/lesson-4)

## Setup Instructions

### Cloning the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/TheSaharFarahzad/todo-app-medium.git
cd todo-app-medium
```

### Option 1: Run Backend and Frontend Separately

You can choose to build and run the backend and frontend Docker containers separately.

#### Backend Setup

Navigate to the backend directory and build the Docker image using the following command:

```bash
cd backend
docker build -t backend-app .
```

Once the image is built, you can run the Docker container with:

```bash
docker run -p 8000:8000 backend-app
```

#### Frontend Setup

Navigate to the frontend directory and build the Docker image using the following command:

```bash
cd frontend
docker build -t frontend-app .
```

Once the image is built, you can run the Docker container with:

```bash
docker run -p 80:80 frontend-app
```

### Option 2: Run Backend and Frontend Together with Docker Compose

You can also use Docker Compose to build and run both containers at once.

#### Build and Run Containers with Docker Compose

Navigate to the root of the project (where `docker-compose.yml` is located) and use the following command:

```bash
docker-compose up --build
```

Docker Compose will handle building both images and starting the containers according to the configuration in `docker-compose.yml`.

### Access the Application

Once both containers are running, you can access the application in your browser at [http://localhost:80](http://localhost:80).

The Flask application starts on port 8000. You can access the backend API at [http://localhost:8000](http://localhost:8000), which will show the message: "Welcome to the ToDo API! Available routes: /tasks."

## License

This project is licensed under the MIT License - see the LICENSE file for details.
