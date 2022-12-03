"""
* Input/Output

* Tree Structure
(Input)
      GIMMEH
        |
     variable

(Output)
      VISIBLE
         |
     vle AN vle

(Concatenation)
      SMOOSH
     /   |   \
   str  AN   str
"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node
from analyzers import variables, typecast

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
  temp = input()
  lookup_table[varname] = {
    const.VALUE_KEY: temp,
    const.TYPE_KEY: const.YARN
  }
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
  print(concatenate(node.children, lookup_table))
  return lookup_table

"""
* analyze_concat()
| Concatenate the given strings and store
| them in a variable.

* Parameters
| node (Node): The root node
| lookup_table (dict): The lookup table
| var (str): The variable name (default: IT)

* Returns
| dict: The updated lookup table
"""
def analyze_concat(node: Node, lookup_table: dict, var = const.IT) -> dict:
  # Assign the concatenated string to a variable.
  lookup_table[var] = {
    const.VALUE_KEY: concatenate(node.children, lookup_table),
    const.TYPE_KEY: const.YARN
  }

  return lookup_table

"""
* concatenate()
| Append each value in a list then
| join them together.

* Parameters
| children (list): Contains values to be concatenated
| lookup_table (dict): The lookup table

* Returns
| str: The concatenated values
"""
def concatenate(children: list, lookup_table: dict) -> str:
  # * Declaration
  stringset = []

  # Append each value in the set.
  for child in children:
    # Skip the delimiter for concatenation.
    if child.lexeme != "AN":
      # TODO: Use `YARN` instead of `str`.
      # * Variable
      if variables.is_variable(child.type):
        if not variables.is_exist(child.lexeme, lookup_table):
          raise Exception(f"{child.lexeme} does not exist.")
        else:
          stringset.append(str(lookup_table[child.lexeme][const.VALUE_KEY]))
      # * Literal
      elif variables.is_literal(child.type):
        stringset.append(str(child.lexeme))
      # * Expression
      else:
        raise Exception("Expressions are not yet supported.")
  return "".join(stringset)