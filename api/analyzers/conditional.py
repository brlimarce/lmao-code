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
import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node
from analyzers.typecast import TROOF

"""
* analyze_ifthen()
| Return the code block if a condition
| is true. Otherwise, return None.

* Returns
| tuple: Contains the code block and the updated lookup table
"""
def analyze_ifthen(node: Node, lookup_table: dict) -> tuple:
  # Typecast the value of IT into TROOF.
  lookup_table[const.IT] = TROOF(lookup_table[const.IT]["value"])
  code_block = None
  
  # Evaluate the conditional statement.
  if lookup_table[const.IT] == const.WIN:
    # Return the code block for WIN.
    code_block = node.children[0]
  else:
    # Check if an ELSE case exists.
    if len(node.children) > 1 and node.children[1].type == "Keyword for the ELSE Case":
      code_block = node.children[1]
  return (code_block, lookup_table)

"""
* analyze_switch()
| Return the code block based on the
| satisfied switch condition
"""
def analyze_switch(node: Node, it_value: dict, executable) -> list:
  # Run through the cases.
  code = []
  DEFAULT_TYPE = "Keyword for the Default Case"
  is_gtfo = False
  
  for case in node.children:
    if case.type != DEFAULT_TYPE:
      # Check if the value matches.
      value = case.children[0].lexeme.replace("\"", "")
      block = case.children[1:]
      
      # Execute the code block.
      if value == it_value:
        for child in block:
          if child.type == "Loop Break":
            is_gtfo = True
            break
          executable.codeblock(child)
    # Run the DEFAULT case (if applicable).
    elif case.type == DEFAULT_TYPE and len(code) < 1:
      block = case.children[1:]
      for child in block:
        executable.codeblock(child)
    
    # End the loop on GTFO keyword.
    if is_gtfo:
      break
