from utility import constants as const
from utility.node import Node
from analyzers import variables, io, typecast

"""
* Semantics
| Serves as the main analyzer
| for the program's semantics.
"""
class Semantics:
  # * Properties
  _root = None
  _lookup_table = {}

  # * Constructor
  def __init__(self, root):
    self._root = root
    self._lookup_table = {const.IT: { 
      const.VALUE_KEY: const.NOOB, const.TYPE_KEY: const.NOOB 
    }}
  
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
        # Check for the analyzer to use.
        # * Variable Declaration
        if child.type == "Variable Declaration":
          self._lookup_table = variables.analyze(child, self._lookup_table)
        # * Input
        elif child.type == "Input":
          self._lookup_table = io.analyze_input(child, self._lookup_table)
        # * Output
        elif child.type == "Output":
          self._lookup_table = io.analyze_output(child, self._lookup_table)
        # * Variable Assignment
        elif child.children[0].type == "Variable Assignment":
          self._lookup_table = variables.analyze_assignment(child, self._lookup_table)
        # * Explicit Typecasting
        elif child.type == "Explicit Typecasting":
          self._lookup_table = typecast.analyze(child, self._lookup_table)
      except Exception as e:
        return (False, self.raise_error(idx + 1, e))
      finally:
        idx += 1
    # Return the flag and lookup table.
    return (True, self._lookup_table)

if __name__ == '__main__':
  # Create a TEST CASE.
  root = Node(None, None, "HAI", "Program Start")

  # Variable Declaration
  child1 = Node(root, root, "I_HAS_A", "Variable Declaration")
  child2 = Node(child1, root, "thing", "Identifier")
  child3 = Node(child1, root, "ITZ", "Variable Initialization")
  child4 = Node(child1, root, "2.2", "NUMBAR Literal")

  child5 = Node(child1, root, "GIMMEH", "Input")
  child6 = Node(child1, root, "IT", "Identifier")

  child7 = Node(child1, root, "VISIBLE", "Output")
  child8 = Node(child1, root, "thing", "Identifier")
  child9 = Node(child1, root, "AN", "Delimiter for Nested Expressions")
  child10 = Node(child1, root, "2", "NUMBR Literal")
  child11 = Node(child1, root, "AN", "Delimiter for Nested Expressions")
  child12 = Node(child1, root, "2.2", "NUMBAR Literal")
  child13 = Node(child1, root, "AN", "Delimiter for Nested Expressions")
  child14 = Node(child1, root, "Hello          友達World", "YARN Literal")

  child15 = Node(child1, root, "thing", "Identifier")
  child16 = Node(child1, root, "R", "Variable Assignment")
  child17 = Node(child1, root, "IT", "Identifier")

  child18 = Node(child1, root, "MAEK", "Explicit Typecasting")
  child19 = Node(child1, root, "thing", "Identifier")
  child20 = Node(child1, root, "A", "Delimiter for Typecasting")
  child21 = Node(child1, root, "NUMBAR", "TYPE Literal")

  child22 = Node(child1, root, "MAEK", "Explicit Typecasting")
  child23 = Node(child1, root, "thing", "Identifier")
  child24 = Node(child1, root, "A", "Delimiter for Typecasting")
  child25 = Node(child1, root, "NUMBR", "TYPE Literal")

  root.add_child(child1)
  root.add_child(child5)
  root.add_child(child7)
  root.add_child(child15)
  root.add_child(child18)
  root.add_child(child22)

  child1.add_child(child2)
  child1.add_child(child3)
  child1.add_child(child4)

  child5.add_child(child6)

  child7.add_child(child8)
  child7.add_child(child9)
  child7.add_child(child10)
  child7.add_child(child11)
  child7.add_child(child12)
  child7.add_child(child13)
  child7.add_child(child14)

  child15.add_child(child16)
  child15.add_child(child17)

  child18.add_child(child19)
  child18.add_child(child20)
  child18.add_child(child21)

  child22.add_child(child23)
  child22.add_child(child24)
  child22.add_child(child25)

  # Print the tree.
  # * NOTE: Uncomment if not used.
  root.print_tree()
  print("= = =")

  # Do semantic analysis.
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ file: semantics.py:55 ~ result", result)
