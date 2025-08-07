
# Use the official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code to the container
COPY . .

# Set environment variable so Flask knows where to look
ENV FLASK_APP=app/main.py

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app/main.py"]