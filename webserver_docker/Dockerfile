


# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app source code into the container
COPY . /app

# Set environment variable so Flask knows where the app entry point is
ENV FLASK_APP=app/main.py

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app/main.py"]
