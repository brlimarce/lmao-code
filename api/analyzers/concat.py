"""
* Concatenation

* Tree Structure
      SMOOSH
     /   |   \
   str  AN   str
"""
from api.analyzers import variables, expression
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
    return (concat(node.children, lookup_table, True), const.YARN)


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
def concat(children: list, lookup_table: dict, is_smoosh=False) -> str:
    # * Declaration
    stringset = []
    error_msg = f"Cannot implicitly cast {const.NOOB} into {const.YARN}"

    # Append each value in the set.
    for child in children:
        # For SMOOSH, discontinue if 
        if is_smoosh and (child != list and child.lexeme == "AN"):
            continue
        # * Variable
        if type(child) != list and variables.is_variable(child.type):
            if not variables.is_exist(child.lexeme, lookup_table):
                raise Exception(f"{child.lexeme} does not exist.")
            else:
                # Raise an error for NOOBs.
                if child.lexeme == const.NOOB:
                    raise Exception(error_msg)
                stringset.append(YARN(lookup_table[child.lexeme][const.VALUE_KEY])[
                                  0].replace("\"", ""))
        # * Literal
        elif type(child) != list and variables.is_literal(child.type):
            # Raise an error for NOOBs.
            if child.lexeme == const.NOOB:
                raise Exception(error_msg)
            stringset.append(YARN(child.lexeme)[0].replace("\"", ""))
        # * Expression
        else:
            node = Node(None, None, const.OP_BLOCK, const.OP_BLOCK)
            node._children = child
            stringset.append(str(expression.evaluate_expr(node, lookup_table)[0]))
    return "".join(stringset)
