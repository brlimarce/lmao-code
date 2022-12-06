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
"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from analyzers.concat import concat
from analyzers import variables
from utility import constants as const
from utility.node import Node

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
  print(concat(node.children, lookup_table))
  return lookup_table
