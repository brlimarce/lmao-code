"""
* Node
| Base to generate the PARSE tree.

* Properties
| lexeme (str): The lexeme from the lexical analyzer.
| type (str): The type of lexeme.
| parent (Node): The parent node (None for ROOT NODE).
| children (list): List of succeeding nodes.
"""
class Node:
  # * Properties
  _lexeme = ""
  _type = ""
  _parent = None
  _children = []

  # * Constructor
  # ! `parent` is an OPTIONAL parameter. Use only for ROOT node.
  def __init__(self, lexeme: str, type: str, children: list, parent = None):
    self._lexeme = lexeme
    self._type = type
    self._parent = parent
    self._children = children
  
  # * Getters
  # Usage Example: n.lexeme (As if you accessed a property).
  @property
  def lexeme(self) -> str:
    return self._lexeme
  
  @property
  def type(self) -> str:
    return self._type
  
  @property
  def parent(self):
    return self._parent
  
  @property
  def children(self) -> list:
    return self._children