"""
"""
from utility.node import Node
from analyzers import variables

class Semantics:
  # * Properties
  _root = None
  _lookup_table = {}

  # * Constructor
  def __init__(self, root):
    self._root = root
    self._lookup_table = {}
  
  @property
  def lookup_table(self):
    return self._lookup_table
  
  """
  * raise_error()
  | Return a formatted version of the error.

  * Parameters
  | line_number (int): Line number in the program
  | message (str): The error

  * Returns
  | str: The formatted error message
  """
  def raise_error(self, line_number: int, message: str) -> str:
    return f"~ Error in Line {line_number}: {message}"

  """
  * analyze()
  | Execute the semantic analysis
  | on the program.

  * Returns
  | tuple: Contains the success flag and result
  """
  def analyze(self) -> tuple:
    # Analyze each statement.
    idx = 0
    for child in self._root.children:
      # Get the analyzer for each statement.
      try:
        parent = child
        print("🚀 ~ file: semantics.py:33 ~ child", child.lexeme)

        # Check for the analyzer to use.
        # * Variable Declaration
        if parent.type == "Variable Declaration":
          self._lookup_table = variables.analyze(child, self._lookup_table)

        # Return the flag and lookup table.
        return (True, self._lookup_table)
      except Exception as e:
        return (False, self.raise_error(idx + 1, e))
      finally:
        idx += 1

if __name__ == '__main__':
  # Create a TEST CASE.
  root = Node(None, None, "HAI", "Program Start")

  # Variable Declaration
  child1 = Node(root, root, "I_HAS_A", "Variable Declaration")
  child2 = Node(child1, root, "thing", "Identifier")
  child3 = Node(child1, root, "ITZ", "Variable Initialization")
  child4 = Node(child1, root, "2.2", "NUMBAR Literal")

  root.add_child(child1)
  child1.add_child(child2)
  child1.add_child(child3)
  child1.add_child(child4)

  # Print the tree.
  # * NOTE: Uncomment if not used.
  root.print_tree()
  print()

  # Do semantic analysis.
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ file: semantics.py:55 ~ result", result)
