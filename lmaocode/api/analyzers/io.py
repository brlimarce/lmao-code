"""
* Input/Output

* Tree Structure
      VISIBLE         GIMMEH
         |              |
     vle AN vle      variable
"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node
from analyzers import variables

"""
* analyze_input()
| Prompt for user input.

* Parameters
| node (Node): The root node
| lookup_table (dict): The lookup table

* Returns
| dict: The updated lookup table
"""
def analyze_input(node: Node, lookup_table: dict) -> dict:
  # Check if the variable exists.
  varname = node.children[0].lexeme
  if not variables.is_exist(varname, lookup_table):
    raise Exception(f"{varname} does not exist.")
  
  # Ask for input.
  lookup_table[varname] = input()
  return lookup_table

"""
* analyze_output()
| Display the provided variables, literals,
| and/or expressions. Supports nesting.

* Parameters
| node (Node): The root node
| lookup_table (dict): The lookup table

* Returns
| dict: The updated lookup table
"""
def analyze_output(node: Node, lookup_table: dict) -> dict:
  # Append the string to be printed.
  stringset = []
  for child in node.children:
    # Skip the delimiter for concatenation.
    if child.lexeme != "AN":
      # * Variable
      if variables.is_variable(child.type):
        if not variables.is_exist(child.lexeme, lookup_table):
          raise Exception(f"{child.lexeme} does not exist.")
        else:
          stringset.append(str(lookup_table[child.lexeme]))
      # * Literal
      elif variables.is_literal(child.type):
        stringset.append(str(child.lexeme))
      # * Expression
      else:
        raise Exception("Expressions are not yet supported.")
  
  # Print the children.
  # TODO: Check if VISIBLE has space.
  print(" ".join(stringset))
  return lookup_table