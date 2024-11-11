# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the /app directory in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (if your app uses this port)
EXPOSE 8000

# Define the default command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]