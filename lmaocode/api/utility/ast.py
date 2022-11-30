"""
* Abstract Syntax Tree
| Represents the overall syntax of
| the program.

| In this case, the DS will be
| represented via node (class).
"""
class Node:
  """
  * Properties
  | 1. parent (Node)
  | 2. root (Node): Start of the program/code block
  | 3. children (Node)
  | 4. token (str): The lexeme extracted from the lexer
  | 5. type (str): Type of lexeme
  """
  _parent = None
  _root = None
  _children = []
  _token = None
  _type = None

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
  def token(self) -> str:
    return self._token
  
  @property
  def type(self) -> str:
    return self._type
