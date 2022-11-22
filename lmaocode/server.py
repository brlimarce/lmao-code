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
| Processes the compilation
| of LOLCODE.

* Parameters
| program (str): Lines of code separated by newline

* Returns
| symbol_table (list): List of lexemes and types
| success (bool): Checks if the execution is successful.
"""
@app.route("/interpret", methods=["POST"])
def interpret():
  # Write the response in an input file.
  code = (request.json["program"])["program"]
  with open("api/" + const.TEST_DIR + "input" + const.FILE_EXT, "w") as outfile:
    outfile.writelines(code)

  # Apply lexical analysis.
  symbol_table = lexer.analyze("input" + const.FILE_EXT)

  # TODO: Error handling for GUI.
  return {
    "symbol_table": symbol_table,
    "success": True
  }

# Run the app.
if __name__ == "__main__":
  app.run(debug=True)