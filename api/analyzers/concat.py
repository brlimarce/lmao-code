"""
* Concatenation

* Tree Structure
      SMOOSH
     /   |   \
   str  AN   str
"""
from api.analyzers import variables
from api.analyzers.typecast import YARN
from api.utility import constants as const
from api.utility.node import Node

"""
* analyze_concat()
| Return a concatenated version based on the
| given list of strings.

* Parameters
| node (Node): The root node
| lookup_table (dict): The lookup table

* Returns
| tuple: Contains the value and YARN type
"""


def analyze_concat(node: Node, lookup_table: dict) -> tuple:
    return (concat(node.children, lookup_table), const.YARN)


"""
* concat()
| Append each value in a list then
| join them together.

* Parameters
| children (list): Contains values to be concatenated
| lookup_table (dict): The lookup table

* Returns
| str: The concatenated values
"""


def concat(children: list, lookup_table: dict) -> str:
    # * Declaration
    stringset = []
    error_msg = f"Cannot implicitly cast {const.NOOB} into {const.YARN}"

    # Append each value in the set.
    for child in children:
        # Skip the delimiter for concatenation.
        if child.lexeme != "AN":
            # * Variable
            if variables.is_variable(child.type):
                if not variables.is_exist(child.lexeme, lookup_table):
                    raise Exception(f"{child.lexeme} does not exist.")
                else:
                    # Raise an error for NOOBs.
                    if child.lexeme == const.NOOB:
                        raise Exception(error_msg)
                    stringset.append(YARN(lookup_table[child.lexeme][const.VALUE_KEY])[
                                     0].replace("\"", ""))
            # * Literal
            elif variables.is_literal(child.type):
                # Raise an error for NOOBs.
                if child.lexeme == const.NOOB:
                    raise Exception(error_msg)
                stringset.append(YARN(child.lexeme)[0].replace("\"", ""))
            # * Expression
            else:
                raise Exception("Expressions are not yet supported.")
    return "".join(stringset)
