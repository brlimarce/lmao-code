"""
* Boolean Operations
| The analyzer should return a TROOF value.

* Tree Structure
       OPERATION
      /         \
   op/vle      op/vle
   /    \      /    \
  l     l     l     l

| Nested OPERATIONS are allowed as long as
| they always have BINARY CHILDREN.
"""

"""
* analyze()
| The main method for evaluating
| boolean expressions.

* Returns
| tuple: Contains the TROOF literal and
| the TROOF type
"""
def analyze() -> tuple:
  print()

"""
* Boolean Operations
| Broken down into different methods for
| modularity and easier debugging.

* Parameters
| node (Node): A subtree of the expression

* Returns
| tuple: Contains the parsed value and new type
"""
