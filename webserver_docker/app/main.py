from flask import Flask  # Flask is a micro web framework for Python

app = Flask(__name__)  # Create a Flask web app instance

@app.route('/')  # Define a route for the root URL
# When someone visits http://localhost:5000/ this function runs
def home():
    return "<h1>Hello from Dockerized Flask WebServer!</h1>"  # Response message shown on the browser

# Run the Flask app only when the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the server on 0.0.0.0 so it listens to all network interfaces inside the container
    app.run(host='0.0.0.0', port=5000)