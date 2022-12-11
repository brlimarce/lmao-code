"""
* Loop
| Deals with both FOR and
| WHILE loops.

* Tree Structure

"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from analyzers import typecast, variables, expression
from utility import constants as const
from utility.node import Node

"""
* analyze()
| Main method for analyzing loops

* Parameters
| node (Node): The parent node
| lookup_table (dict): The lookup table

* Returns
| list: The code block to be executed
"""
def analyze(node: Node, lookup_table: dict, executable) -> dict:
  # Check if the label at the start and end of the
  # loop are similar.
  children = node.children
  if children[0].lexeme != children[len(children) - 1].children[0].lexeme:
    raise Exception(f"Cannot end without {children[0].lexeme} in the loop.")
  
  # Indicate the type of operation (update) and condition.
  is_increment = children[1].lexeme == "UPPIN"
  is_condition = children[4].lexeme == "TIL" # TIL for FAIL, WILE for WIN

  # Check if the variable exists.
  varname = children[3].lexeme
  if not variables.is_exist(varname, lookup_table):
    raise Exception(f"{varname} does not exist.")
  
  # Typecast an uninitialized value.
  value = None
  try:
    value = typecast.NUMBR(lookup_table[varname][const.VALUE_KEY])
  except:
    if const.YARN in lookup_table[varname][const.TYPE_KEY]:
      raise Exception(f"{typecast.NUMBR(lookup_table[varname][const.VALUE_KEY])} cannot be casted into NUMBR.")
    value = (const.FAIL, "TROOF")
    value = typecast.NUMBR(value[0])
  lookup_table[varname] = {
    const.VALUE_KEY: value[0],
    const.TYPE_KEY: value[1]
  }
  
  # Run the loop until the condition is met.
  expr_node = children[5].children[0]
  while True:
    flag = expression.evaluate_expr(expr_node, lookup_table)
    if (is_condition and flag[0] == const.WIN) or (not is_condition and flag[0] == const.FAIL):
      break

    # Execute the block of code.
    for child in children[6].children:
      if child.type == "Loop Break":
        return lookup_table
      executable.codeblock(child)

    # Increment/decrement the value.
    update_val = lookup_table[varname][const.VALUE_KEY] + 1 if is_increment else lookup_table[varname][const.VALUE_KEY] - 1
    lookup_table[varname] = {
      const.VALUE_KEY: update_val,
      const.TYPE_KEY: const.NUMBR
    }
  return lookup_table