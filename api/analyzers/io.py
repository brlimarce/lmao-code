"""
* Input/Output

* Tree Structure
(Input)
      GIMMEH
        |
     variable

(Output)
      VISIBLE
     /       \
    vle     vle

* Note: The AN keyword is optional, but since
I also use the same function for SMOOSH, it's
still supported.
"""
# To go outside the folder (relative path).
from api.utility.node import Node
from api.utility import constants as const
from api.analyzers import variables
from api.analyzers.concat import concat
import easygui_qt
import sys
sys.path.append("../")


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
    temp = easygui_qt.get_string(message="", title="GIMMEH")
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
def analyze_output(node: Node, lookup_table: dict, terminal) -> dict:
    output = concat(node.children, lookup_table)
    terminal.setText(f"{terminal.toPlainText()}\n{output}")
    return lookup_table