from utility import constants as const
from utility.node import Node
from analyzers import variables, io, typecast, conditional
import lexer
from parser import parse

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
    # self._lookup_table = {const.IT: { 
    #   const.VALUE_KEY: const.NOOB, const.TYPE_KEY: const.NOOB 
    # }}
    self._lookup_table = {const.IT: { 
      const.VALUE_KEY: 2, const.TYPE_KEY: "NUMBR Literal"
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
        # * IF-THEN Statement
        if child.type == "Start of IF-THEN Statement":
          result = conditional.analyze_ifthen(child, self._lookup_table)
          self._lookup_table = result[1] # Store lookup table.

          # Execute the code block in the matching CASE.
          if result[0] != None:
            for code in result[0].children:
              self.codeblock(code)
        # * SWITCH-CASE Statement
        elif child.type == "Start of SWITCH Case Statement":
          result = conditional.analyze_switch(child, self._lookup_table[const.IT][const.VALUE_KEY])
          if result != None:
            for code in result:
              for statements in code:
                self.codeblock(statements)
        # * Expression
        else:
          self.codeblock(child)
      except Exception as e:
        return (False, self.raise_error(idx + 1, e))
      finally:
        idx += 1
    # Return the flag and lookup table.
    return (True, self._lookup_table)

  """
  * codeblock()
  | Analyze the code block in
  | the program.

  | Does not include conditional statements
  | or loops.

  * Parameters
  | child (Node): The child node
  """
  def codeblock(self, child: Node):
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

if __name__ == '__main__':
  root = Node(None, None, "HAI", "Program Start")

  # ** LOOPS **
  

  # # ** SWITCH STATEMENT **
  # child1 = Node(root, root, "WTF?", "Start of SWITCH Case Statement")
  # root.add_child(child1)

  # child2 = Node(child1, child1, "OMG", "Keyword for the SWITCH Case Statement")
  # child3 = Node(child2, child1, 4, "NUMBR Literal")
  
  # child1.add_child(child2)
  # child2.add_child(child3)

  # child7 = Node(child3, child1, "VISIBLE", "Output")
  # child8 = Node(child7, child1, 2, "NUMBR Literal")

  # child3.add_child(child7)
  # child7.add_child(child8)

  # child4 = Node(child1, child1, "OMG", "Keyword for the SWITCH Case Statement")
  # child5 = Node(child4, child1, 3, "NUMBR Literal")

  # child1.add_child(child4)
  # child4.add_child(child5)

  # child9 = Node(child3, child1, "VISIBLE", "Output")
  # child10 = Node(child7, child1, "Same case but diff catch", "YARN Literal")

  # child5.add_child(child9)
  # child9.add_child(child10)

  # child6 = Node(child1, child1, "OMGWTF", "Keyword for the Default Case")
  # child1.add_child(child6)

  # child10 = Node(child6, child1, "VISIBLE", "Output")
  # child11 = Node(child10, child1, "Default Case", "YARN Literal")

  # child6.add_child(child10)
  # child10.add_child(child11)

  # # ** IF-THEN STATEMENT **
  # child1 = Node(root, root, "O_RLY?", "Start of IF-THEN Statement")
  # root.add_child(child1)

  # child2 = Node(child1, child1, "YA_RLY", "Keyword for the IF Case")
  # child3 = Node(child1, child1, "NO_WAI", "Keyword for the ELSE Case")

  # child1.add_child(child2)
  # # child1.add_child(child3)

  # # YA RLY
  # child4 = Node(child2, child1, "VISIBLE", "Output")
  # child5 = Node(child4, child1, "YAY, WIN", "TROOF Literal")

  # child2.add_child(child4)
  # child4.add_child(child5)

  # # NO WAI
  # child6 = Node(child3, child1, "VISIBLE", "Output")
  # child7 = Node(child6, child1, "OH NO, FAIL", "TROOF Literal")

  # child3.add_child(child6)
  # child6.add_child(child7)

  # * NOTE: Uncomment this code block
  # * for the analyzer.
  
  # # * Lexical Analyzer
  # code = []
  # with open("test/input.lol", "r") as infile:
  #     code = [line[:-1].strip() for line in infile.readlines()
  #             if line[:-1].strip() != ""]
  # result = lexer.Lexer(code).analyze()
  # symbol_table = result[1]

  # # * Syntax Analyzer
  # lex = []
  # for k in symbol_table:
  #     for i in symbol_table[k]:
  #         lex.append(i)
  #     if symbol_table[k] != []:
  #         if symbol_table[k][0][0] != "KTHXBYE" and symbol_table[k][0][0] != "OBTW" and \
  #                 symbol_table[k][0][0] != "TLDR" and symbol_table[k][0][0] != "BTW":
  #             lex.append(("Parser Delimiter", "-"))

  # node = parse(lex)
  # # node.print_tree()

  # * Semantics Analyzer
  analyzer = Semantics(root)
  result = analyzer.analyze()
  print(result)
