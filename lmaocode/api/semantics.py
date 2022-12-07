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
  # Case 1: Variable Declaration
  print("== Case #1: Variable Declaration ==")
  root = Node(None, None, "HAI", "Program Start")
  child1 = Node(root, root, "I_HAS_A", "Variable Declaration")
  child2 = Node(child1, root, "thing", "Identifier")
  child3 = Node(child1, root, "ITZ", "Variable Initialization")
  child4 = Node(child1, root, "2.2", "NUMBAR Literal")

  root.add_child(child1)
  child1.add_child(child2)
  child1.add_child(child3)
  child1.add_child(child4)

  root.print_tree()
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ Lookup Table:", result[1])

  # Case 2: Variable Assignment
  print("\n== Case #2: Variable Assignment ==")
  child13 = Node(root, root, "thing", "Identifier")
  child14 = Node(child13, root, "R", "Variable Assignment")
  child15 = Node(child13, root, "IT", "Identifier")

  root.add_child(child13)
  child13.add_child(child14)
  child13.add_child(child15)

  root.print_tree()
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ Lookup Table:", result[1])

  # # Case 3.1: Typecasting
  # print("\n== Case #3.1: Typecasting ==")
  # child16 = Node(root, root, "MAEK", "Explicit Typecasting")
  # child17 = Node(child16, root, "thing", "Identifier")
  # child18 = Node(child16, root, "A", "Delimiter for Typecasting")
  # child19 = Node(child16, root, "NUMBAR", "TYPE Literal")

  # root.add_child(child16)
  # child16.add_child(child17)
  # child16.add_child(child18)
  # child16.add_child(child19)

  # root.print_tree()
  # analyzer = Semantics(root)
  # result = analyzer.analyze()
  # print("🚀 ~ Lookup Table:", result[1])

  # Case 3: Typecasting
  print("\n== Case #3: Typecasting ==")
  child20 = Node(root, root, "I_HAS_A", "Variable Declaration")
  child21 = Node(child20, root, "thing2", "Identifier")
  child22 = Node(child20, root, "ITZ", "Variable Initialization")
  child23 = Node(child20, root, "4.587586", "NUMBAR Literal")

  child20.add_child(child21)
  child20.add_child(child22)
  child20.add_child(child23)

  child24 = Node(root, root, "thing", "Identifier")
  child25 = Node(child24, root, "R", "Variable Assignment")
  child26 = Node(child24, root, "thing2", "Identifier")

  child24.add_child(child25)
  child24.add_child(child26)

  child27 = Node(root, root, "MAEK", "Explicit Typecasting")
  child28 = Node(child27, root, "thing", "Identifier")
  child29 = Node(child27, root, "A", "Delimiter for Typecasting")
  child30 = Node(child27, root, "NUMBR", "TYPE Literal")

  child27.add_child(child28)
  child27.add_child(child29)
  child27.add_child(child30)

  root.add_child(child20)
  root.add_child(child24)
  root.add_child(child27)

  root.print_tree()
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ Lookup Table:", result[1])

  # Case 4: Input
  print("\n== Case #4: Input ==")
  child5 = Node(child1, root, "GIMMEH", "Input")
  child6 = Node(child1, root, "IT", "Identifier")

  root.add_child(child5)
  child5.add_child(child6)

  root.print_tree()
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print("🚀 ~ Lookup Table:", result[1])

  # Case 5: Output
  print("\n== Case #5: Output ==")
  root2 = Node(None, None, "HAI", "Program Start")
  child7 = Node(child1, root, "VISIBLE", "Output")
  child8 = Node(child1, root, "2", "NUMBR Literal")
  child9 = Node(child1, root, "AN", "Delimiter for Nested Expressions")
  child10 = Node(child1, root, "IT", "Identifier")
  child11 = Node(child1, root, "AN", "Delimiter for Nested Expressions")
  child12 = Node(child1, root, "Hello          友達World", "YARN Literal")

  root2.add_child(child7)
  child7.add_child(child8)
  child7.add_child(child9)
  child7.add_child(child10)
  child7.add_child(child11)
  child7.add_child(child12)

  root2.print_tree()
  analyzer = Semantics(root2)
  result = analyzer.analyze()
  print("🚀 ~ Lookup Table:", result[1])
