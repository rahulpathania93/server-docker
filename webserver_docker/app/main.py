from flask import Flask  # Import Flask web framework

app = Flask(__name__)  # Create a Flask application instance

@app.route('/')  # Define a route for the root URL
def home():
    # This function runs when someone visits http://localhost:5000/
    return "<h1>Hello from Dockerized Flask WebServer!</h1>"

# Run the Flask server if the script is executed directly
if __name__ == '__main__':
    # host='0.0.0.0' → makes the app accessible outside the container
    # port=5000 → match the EXPOSE setting in Dockerfile
    app.run(host='0.0.0.0', port=5007)
# end---------
#testing automation
#testing cicd