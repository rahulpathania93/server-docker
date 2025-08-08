# Basic documentation for your project

# WebServer using Docker

This project creates a simple Python Flask web server and containerizes it using Docker.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <repo-url>
cd webserver_docker
```

### 2. Build the Docker Image
```bash
docker build -t flask-webserver .
```

### 3. Run the Container
```bash
docker run -p 5007:5007 flask-webserver
```

### 4. Open in Browser
Visit: [http://localhost:5007](http://localhost:5007)

You should see: `Hello from Dockerized Flask WebServer!`

