"""
* Variable Declaration
| Deals with both declaration and initialization.

* Tree Structure
(Variable Declaration/Initialization)
      I HAS A
      /     \       \
    var     ITZ     vle

(Variable Assignment)
      var
    /     \
   R     vle
"""
# To go outside the folder (relative path).
from api.analyzers import typecast, expression
from api.utility.node import Node
from api.utility import constants as const
import sys
sys.path.append("../")


"""
* analyze()
| The main method to analyze variable
| declaration and initialization.

* Parameters
| node (Node): The parent node
| lookup_table (dict): The lookup table

* Returns
| dict: The lookup table
"""


def analyze(node: Node, lookup_table: dict) -> dict:
    # Check if the variable already exists.
    varname = node.children[0].lexeme
    if is_exist(varname, lookup_table):
        raise Exception(f"{varname} was already declared before.")

    # Initialize the variable (NOOB by default).
    lookup_table[varname] = {
        const.VALUE_KEY: const.NOOB,
        const.TYPE_KEY: const.NOOB
    }

    # Reassign the value if specified.
    children = node.slice_children(1, len(node.children))
    if len(children) >= 2:
        # Check if the value is a literal, variable, or expression.
        children = children[1:]

        # * Literal
        if is_literal(children[0].type):
            lookup_table[varname] = {
                const.VALUE_KEY: children[0].lexeme,
                const.TYPE_KEY: children[0].type
            }
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
            lookup_table[varname] = {
                const.VALUE_KEY: lookup_table[temp_varname][const.VALUE_KEY],
                const.TYPE_KEY: lookup_table[temp_varname][const.TYPE_KEY],
            }

        # * Value of IT
        elif children[0].lexeme == const.IT:
            lookup_table[varname] = {
                const.VALUE_KEY: lookup_table[const.IT][const.VALUE_KEY],
                const.TYPE_KEY: lookup_table[const.IT][const.TYPE_KEY],
            }
        # * Expressions
        else:
            result = expression.evaluate_expr(
                node.children[1:], lookup_table, True)
            lookup_table[varname] = {
                const.VALUE_KEY: result[0],
                const.TYPE_KEY: result[1],
            }
    return lookup_table


"""
* analyze_assignment()
| The method to reassign values
| to a variable.

* Parameters
| node (Node): The parent node
| lookup_table (dict): The lookup table

* Returns
| dict: The lookup table
"""


def analyze_assignment(node: Node, lookup_table: dict) -> dict:
    # Check if the parent is an EXISTING VARIABLE.
    if not is_exist(node.lexeme, lookup_table):
        raise Exception(f"{node.lexeme} does not exist.")

    # Assign the value to the variable.
    value = node.children[1]
    varname = node.lexeme

    if is_literal(value.type):
        lookup_table[varname] = {
            const.VALUE_KEY: value.lexeme,
            const.TYPE_KEY: (value.type).replace(const.LITERAL, "").strip()
        }
    elif is_variable(value.type):
        # Raise an error if variable is non-existent.
        if not is_exist(value.lexeme, lookup_table):
            raise Exception(f"{value.lexeme} does not exist.")
        lookup_table[varname] = {
            const.VALUE_KEY: lookup_table[value.lexeme][const.VALUE_KEY],
            const.TYPE_KEY: lookup_table[value.lexeme][const.TYPE_KEY]
        }
    else:
        result = expression.evaluate_expr(
            node.children[1:], lookup_table, True)
        lookup_table[varname] = {
            const.VALUE_KEY: result[0],
            const.TYPE_KEY: result[1]
        }
    return lookup_table


"""
* analyze_smoosh_var()
| Assign the value of a variable
| to the IT variable.
"""


def analyze_smoosh_var(var: str, lookup_table: dict):
    # Throw an error is variable does not exist.
    if not is_exist(var, lookup_table):
        raise Exception(f"{var} does not exist.")

    # Assign the value to the IT variable.
    lookup_table[const.IT] = {
        const.VALUE_KEY: lookup_table[var][const.VALUE_KEY],
        const.TYPE_KEY: lookup_table[var][const.TYPE_KEY]
    }

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
