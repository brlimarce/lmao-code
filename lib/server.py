"""
* Server
| The backend server of the website using Flask.
| To turn on, enter: python server.py

| URL: http://localhost:5000/
"""
from flask import Flask, request

# Initialize Flask app.
app = Flask(__name__)

"""
* Main Route
| Serves as the initial route.

| URL: http://localhost:3000/
"""
@app.route("/")
def main():
  return None

"""
* Interpreter
| Processes the compilation
| of LOLCODE.

* Parameters
| program (str): Lines of code separated by newline
"""
@app.route("/interpret", methods=["POST"])
def interpret():
  return None

# TODO: Remove the block of code below.
# @app.route("/change", methods=["POST"])
# def change():
#   name = request.json["name"]
#   return {
#     "Name": name,
#     "Age": "21",
#     "Date": x,
#     "programming": ["JavaScript", "C#"]
#   }

# Run the app.
if __name__ == "__main__":
  app.run(debug=True)