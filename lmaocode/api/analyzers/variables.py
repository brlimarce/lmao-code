"""
* Variable Declaration
| Deals with variable declaration
| and initialization.

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

def analyze(node: Node, lookup_table: dict) -> dict:
  # Check if the variable already exists.
  varname = node.children[0].lexeme
  if varname in lookup_table.keys():
    raise Exception(f"{varname} was already declared before.")
  
  # Initialize the variable (NOOB by default).
  lookup_table[varname] = const.NOOB

  # Reassign the value if specified.
  children = node.slice_children(1, len(node.children))
  if len(children) >= 2:
    # Check if the value is a literal, variable, or expression.
    children = children[1:]

    # * Literal
    if "Literal" in children[0].type:
      # TODO: Apply typecasting on literal.
      lookup_table[varname] = children[0].lexeme
    # * ANOTHER Variable
    elif children[0].type == "Identifier":
      temp_varname = children[0].lexeme

      # The variable does not exist.
      if temp_varname not in lookup_table.keys():
        raise Exception(f"{temp_varname} does not exist.")
      
      # The variable is the same as the one being declared.
      if temp_varname == varname:
        raise Exception(f"{varname} has not been declared yet.")
      
      # Reassign the variable.
      lookup_table[varname] = lookup_table[temp_varname]
    # * Expressions
    else:
      # TODO: Support expressions.
      raise Exception("Expressions are not yet supported.")
  return lookup_table
  