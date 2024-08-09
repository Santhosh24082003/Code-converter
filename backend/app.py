from flask import Flask
from routes import init_routes
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Initialize routes for the main application
init_routes(app)

# Add a simple route to return "Hello, World!"
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3001))  # Ensure this matches your .env PORT
    app.run(debug=True, port=port)
