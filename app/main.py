from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

app = Flask(__name__)

@app.route('/<random_string>')
def return_backwards_string(random_string):
    
    return "".join(reversed(random_string))

@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
# This is a simple Flask application that reverses a string passed in the URL
# and returns the value of an environment variable named "MODE" when accessed at the '/get-mode' endpoint.
# The application is set to run on all interfaces at port 8080. 