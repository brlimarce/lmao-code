"""
* Variable Declaration
| Deals with both declaration and initialization.

* Tree Structure
      I HAS A
      /     \       \
    var     ITZ   literal/variable/expression
"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node

"""
* analyze()
| The main method to analyze variable
| declaration and initialization.

* Parameters
| node (Node): The parent node
| lookup_table (dict): The lookup table
"""
def analyze(node: Node, lookup_table: dict) -> dict:
  # Check if the variable already exists.
  varname = node.children[0].lexeme
  if is_exist(varname, lookup_table):
    raise Exception(f"{varname} was already declared before.")
  
  # Initialize the variable (NOOB by default).
  lookup_table[varname] = const.NOOB

  # Reassign the value if specified.
  children = node.slice_children(1, len(node.children))
  if len(children) >= 2:
    # Check if the value is a literal, variable, or expression.
    children = children[1:]

    # * Literal
    if is_literal(children[0].type):
      # TODO: Apply typecasting on literal.
      lookup_table[varname] = children[0].lexeme
    # * ANOTHER Variable
    elif is_variable(children[0].type):
      temp_varname = children[0].lexeme

      # The variable does not exist.
      if not is_exist(temp_varname, lookup_table):
        raise Exception(f"{temp_varname} does not exist.")
      
      # The variable is the same as the one being declared.
      if temp_varname == varname:
        raise Exception(f"{varname} has not been declared yet.")
      
      # Reassign the variable.
      lookup_table[varname] = lookup_table[temp_varname]
    # * Value of IT
    elif children[0].lexeme == const.IT:
      lookup_table[varname] = lookup_table[const.IT]
    # * Expressions
    else:
      # TODO: Support expressions.
      raise Exception("Expressions are not yet supported.")
  return lookup_table

"""
* is_exist()
| Checks if the variable exists in
| the lookup table.

* Parameters
| name (str): The variable name
| lookup_table (dict): The lookup table

* Returns
| bool: Flag that indicates if a variable exists
"""
def is_exist(name: str, lookup_table: dict) -> bool:
  return name in lookup_table.keys()

"""
* is_literal()
| Checks if the lexeme is a literal.

* Parameters
| type (str): The lexeme type

* Returns
| bool: Flag that indicates if type is a literal
"""
def is_literal(type: str) -> bool:
  return "Literal" in type

"""
* is_variable()
| Checks if the lexeme is a variable.

* Parameters
| type (str): The lexeme type

* Returns
| bool: Flag that indicates if type is a variable
"""
def is_variable(type: str) -> bool:
  return type == "Identifier"