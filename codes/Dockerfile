# Use an official Python runtime as a parent image
FROM python:3.10.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# installing dependcies
RUN pip install --no-cache-dir -r requirements.txt

# Dummy Port
EXPOSE 8080

# Run app.py when the container launches
CMD ["python3", "main.py"]
