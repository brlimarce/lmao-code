from utility import constants as const
from utility.node import Node
from analyzers import variables, io, typecast, conditional, expression, loop
import lexer
from parser import parse

"""
* Semantics
| Serves as the main analyzer
| for the program's semantics.
"""
class Semantics:
  # * Properties
  _root = None
  _lookup_table = {}

  # * Constructor
  def __init__(self, root):
    self._root = root
    self._lookup_table = {const.IT: { 
      const.VALUE_KEY: const.NOOB, const.TYPE_KEY: const.NOOB 
    }}
  
  @property
  def lookup_table(self):
    return self._lookup_table
  
  """
  * raise_error()
  | Return a formatted version of the error.

  * Parameters
  | line_number (int): Line number in the program
  | message (str): The error

  * Returns
  | str: The formatted error message
  """
  def raise_error(self, line_number: int, message: str) -> str:
    return f"🚀 ~ Error on Line {line_number}: {message}"

  """
  * analyze()
  | Execute the semantic analysis
  | on the program.

  * Returns
  | tuple: Contains the success flag and result
  """
  def analyze(self) -> tuple:
    # Analyze each statement.
    idx = 0

    for child in self._root.children:
      # Get the analyzer for each statement.
      try:
        # * IF-THEN Statement
        if child.type == "Start of IF-THEN Statement":
          result = conditional.analyze_ifthen(child, self._lookup_table)
          self._lookup_table = result[1] # Store lookup table.

          # Execute the code block in the matching CASE.
          if result[0] != None:
            for code in result[0].children:
              self.codeblock(code)
        # * SWITCH-CASE Statement
        elif child.type == "Start of SWITCH Case Statement":
          conditional.analyze_switch(child, self._lookup_table[const.IT][const.VALUE_KEY], self)
        # * Loop
        elif child.type == "Start of Loop":
          self._lookup_table = loop.analyze(child, self._lookup_table, self)
        # * Expression
        else:
          self.codeblock(child)
      except Exception as e:
        return (False, self.raise_error(idx + 1, e))
      finally:
        idx += 1
    # Return the flag and lookup table.
    return (True, self._lookup_table)

  """
  * codeblock()
  | Analyze the code block in
  | the program.

  | Does not include conditional statements
  | or loops.

  * Parameters
  | child (Node): The child node
  """
  def codeblock(self, child: Node):
    # * Operations
    if child.type == const.OP_BLOCK:
      self._lookup_table[const.IT] = expression.evaluate_expr(child, self._lookup_table)
    # * String Concatenation
    elif child.type == "String Concatenation":
      self._lookup_table[const.IT] = expression.evaluate_expr(child, self._lookup_table)
    # * Variable Declaration
    elif child.type == "Variable Declaration":
      self._lookup_table = variables.analyze(child, self._lookup_table)
    # * Input
    elif child.type == "Input":
      self._lookup_table = io.analyze_input(child, self._lookup_table)
    # * Output
    elif child.type == "Output":
      self._lookup_table = io.analyze_output(child, self._lookup_table)
    # * Variable Assignment
    elif child.children[0].type == "Variable Assignment":
      self._lookup_table = variables.analyze_assignment(child, self._lookup_table)
    # * Explicit Typecasting
    elif child.type == "Explicit Typecasting":
      self._lookup_table = typecast.analyze(child, self._lookup_table)
