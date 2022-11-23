"""
* Server
| The backend server of the website using Flask.
| To turn on, enter: python server.py

| URL: http://localhost:5000/
"""
from flask import Flask, request
from api import lexer
from api.utility import constants as const

# Initialize Flask app.
app = Flask(__name__)

"""
* Main Route
| Serves as the initial route.

| URL: http://localhost:3000/
"""
@app.route("/start")
def main():
  starter_code = "BTW edit this code or upload a file!\nHAI\n  VISIBLE \"Hello World!\"\nKTHXBYE\n"
  return {
    "program": starter_code
  }

"""
* Interpreter
| Processes the compilation of LOLCODE.

* Parameters
| program (str): Lines of code separated by newline

* Returns
| symbol_table (list): List of lexemes and types
| success (bool): Checks if the execution is successful.
"""
@app.route("/interpret", methods=["POST"])
def interpret():
  # Clean the data for analysis.
  code = (request.json["program"])["program"]
  code = clean_code(code.split("\n"))

  # * Lexical Analysis
  res = lexer.analyze(code)

  # TODO: Error handling for GUI.
  return {
    "payload": res[1],
    "success": res[0]
  }

"""
* clean_code()
| A utility function to clean
| the program.

* Parameters
| program (list): Lines of code split by a newline

* Returns
| list: A clean set of program lines.
"""
def clean_code(program: list) -> list:
  return [program[i].strip() for i in range(len(program)) if program[i] != '']

# Run the app.
if __name__ == "__main__":
  app.run(debug=True)