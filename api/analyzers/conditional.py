"""
* Conditional Statements
| Deals with both the IF-THEN statement
| and SWITCH Case Statement.

* Tree Structure

(If-then Statement)
      O RLY?
     /      \      \
  YA RLY  NO WAI   OIC
    |       |
   expr    expr

(If Statement)
    O RLY?
      |      \
    YA RLY   OIC
      |
     expr

(Switch Case Statement)
      WTF?
    /      \     \      \
  OMG     OMG   OMGWTF  OIC
   |       |      |
  val     val   expr
   |       |
  expr    expr

* Note: Based on the specs, I think it's still
possible to have NO default case.
"""
# To go outside the folder (relative path).
from api.analyzers.typecast import TROOF
from api.utility.node import Node
from api.utility import constants as const
import sys
sys.path.append("../")


"""
* analyze_ifthen()
| Return the code block if a condition
| is true. Otherwise, return None.

* Returns
| tuple: Contains the code block and the updated lookup table
"""


def analyze_ifthen(node: Node, lookup_table: dict, executable) -> tuple:
    # Typecast the value of IT into TROOF.
    if const.TROOF not in lookup_table[const.IT][const.TYPE_KEY]:
        result = TROOF(lookup_table[const.IT][const.VALUE_KEY])
        lookup_table[const.IT] = {
            const.VALUE_KEY: result[0],
            const.TYPE_KEY: result[1]
        }

    # Evaluate the conditional statement.
    if lookup_table[const.IT][const.VALUE_KEY] == const.WIN:
        # Return the code block for WIN.
        for child in node.children[0].children:
            executable.codeblock(child)
    else:
        # Check if an ELSE case exists.
        if len(node.children) > 1 and node.children[1].type == "Keyword for the ELSE Case":
            for child in node.children[1].children:
                executable.codeblock(child)
    return lookup_table


"""
* analyze_switch()
| Return the code block based on the
| satisfied switch condition
"""


def analyze_switch(node: Node, it_value: dict, executable) -> list:
    # Run through the cases.
    DEFAULT_TYPE = "Keyword for the Default Case"
    is_gtfo = False
    is_case = False

    for case in node.children:
        if case.type != DEFAULT_TYPE:
            # Check if the value matches.
            value = case.children[0].lexeme.replace("\"", "")
            block = case.children[1:]

            # Execute the code block.
            if value == it_value:
                is_case = True
                for child in block:
                    if child.type == "Loop Break":
                        is_gtfo = True
                        break
                    executable.codeblock(child)
        # Run the DEFAULT case (if applicable).
        elif case.type == DEFAULT_TYPE and not is_case:
            for child in case.children:
                executable.codeblock(child)
        # End the loop on GTFO keyword.
        if is_gtfo:
            break
