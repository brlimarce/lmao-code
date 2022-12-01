"""
* Abstract Syntax Tree
| Represents the overall syntax of
| the program.

| In this case, the DS will be
| represented via node (class).
"""
from collections import deque

class Node:
  """
  * Properties
  | 1. parent (Node)
  | 2. root (Node): Start of the program/code block
  | 3. children (Node)
  | 4. lexeme (str): The lexeme extracted from the lexer
  | 5. type (str): Type of lexeme
  """
  _parent = None
  _root = None
  _children = []
  _lexeme = None
  _type = None
  _key = 0

  # * Constructor
  def __init__(self, parent, root, lexeme, lexeme_type):
    self._parent = parent
    self._root = root
    self._children = []
    self._lexeme = lexeme
    self._type = lexeme_type

  """
  * Getters
  | Think of this as a getter in Java.
  | * Sample: node.parent
  """
  @property
  def parent(self):
    return self._parent
  
  @property
  def root(self):
    return self._root
  
  @property
  def children(self):
    return self._children

  @property
  def lexeme(self) -> str:
    return self._lexeme
  
  @property
  def type(self) -> str:
    return self._type

  """
  * add_child()
  | Add a child node to the
  | current node.

  * Parameter
  | child (Node): The child node
  """
  def add_child(self, child):
    self._children.append(child)
  
  """
  * print_tree()
  | Display the tree in the terminal by
  | doing preorder traversal.
  |
  | Used for debugging.
  """
  def print_tree(self):
    # * Declaration
    stack = deque([])
    visited = [] # Indicates the visited node
    
    # Append the root node.
    visited.append(self)
    stack.append(self)

    # Print the root node.
    self._print_node(self.lexeme)
    print()

    while len(stack) > 0:
      flag = 0 # Flag if all child nodes were visited

      # TOS is a leaf node.
      if len(stack[len(stack) - 1].children) == 0:
        x = stack.pop()
      # TOS is a parent node with children.
      else:
        parent = stack[len(stack) - 1]
      
      # Store children from left to right.
      for i in range(0, len(parent.children)):
        # Check if the children is visited.
        if parent.children[i] not in visited:
          flag = 1
          stack.append(parent.children[i])
          visited.append(parent.children[i])
          self._print_node(parent.children[i].lexeme)
          break
      
      # Remove the parent from the stack
      # if all children were visited.
      if flag == 0:
        print() # Space Allowance
        stack.pop()
  
  """
  * print_node()
  | A utility function that prints
  | the node depending on its level.

  * Parameters
  | level (int): Distance from child to root
  | lexeme (str): The lexeme
  """
  def _print_node(self, lexeme: str):
    print(f"🌿 ~ {lexeme}")
