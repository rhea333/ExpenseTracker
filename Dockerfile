# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP=run.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
