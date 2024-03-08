# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY services /app/services

# Expose the port that the Flask app runs on
EXPOSE 5010

# Define the command to run your application

CMD ["uvicorn", "services.hfservice:app", "--host", "0.0.0.0", "--port", "5010"]