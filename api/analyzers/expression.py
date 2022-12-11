"""
* Expression
| Evaluates the conditional and
| loop statements.
"""
from utility import constants as const
from utility.node import Node
from analyzers import concat, operations
from copy import deepcopy

# Return the computed value or concatenated string.
def evaluate_expr(children, lookup_table: dict, is_nested=False) -> tuple:
  # * Declaration
  result = ()
  node = children

  # If expression is nested within a statement,
  # create a separate node for it.
  if is_nested:
    # * Smoosh
    if type(children[0]) == Node and children[0].type == "String Concatenation":
      node = convert_smoosh(children)
    # * Operations
    else:
      node = convert_op(children)

  # Perform the operation.
  # * Smoosh
  if children[0].type == "String Concatenation":
    result = concat.analyze_concat(node, lookup_table)
  # * Operations
  else:
    raise Exception("Invalid expression")
  return result

# Convert SMOOSH into a list of nodes for those
# with nested expressions.
def convert_smoosh(children: list) -> Node:
  for child in children[1:]:
    children[0].add_child(child)
  return children[0]

# Convert the operations into a reverse stack
# inside a `wrapper` node.
def convert_op(children: list) -> Node:
  node = Node(None, None, const.OP_BLOCK, const.OP_BLOCK)
  block = deepcopy(children)
  stack = []

  # Convert into a tuple.
  for i in range(len(block) - 1, -1, -1):
    stack.append((children[i].lexeme, children[i].type))
  node._children = stack
  return node