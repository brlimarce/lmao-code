"""
* Typecasting
| Deals with both explicit and implicit ones.

* Tree Structure
(Explicit Typecasting)
        MAEK
       /    \             \
    var     A (optional)  TYPE

(Variable Reassignment)
         var
      /       \
  IS NOW A    TYPE
"""
# To go outside the folder (relative path).
import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node
import math

"""
* analyze()
| The main method for typecasting. Calls the
| right typecast for a certain value.
"""
def analyze(node: Node, lookup_table: dict) -> dict:
  # Cast depending on the type.
  cast_type = node.children[len(node.children) - 1].lexeme
  value = lookup_table[node.children[0].lexeme] if node.type == "Explicit Typecasting" else lookup_table[node.lexeme]
  result = ()

  # * YARN
  # TODO: Support with IS NOW A
  var = node.children[0].lexeme
  value = value[const.VALUE_KEY]
  if cast_type == const.YARN:
    result = YARN(value)
  # * NOOB
  elif cast_type == const.NOOB:
    result = NOOB(value)
  # * TROOF
  elif cast_type == const.TROOF:
    result = TROOF(value)
  # * NUMBAR
  elif cast_type == const.NUMBAR:
    result = NUMBAR(value)
  # * NUMBR
  elif cast_type == const.NUMBR:
    result = NUMBR(value)

  # Update the values.
  lookup_table[var] = {
    const.VALUE_KEY: result[0],
    const.TYPE_KEY: result[1]
  }

  return lookup_table

"""
* Typecasters
| Broken down into different methods for
| modularity and easier debugging.

* Parameters
| value (dynamic): The value to be typecasted

* Returns
| tuple: Contains the parsed value and new type
"""
# any -> NOOB (EXPLICIT)
def NOOB(value) -> tuple:
  # NUMBR and NUMBAR Literals
  if is_numbr(value)[0] or is_numbar(value)[0]:
    return (
      0 if is_numbr(value)[1] == 0 else 0.0,
      const.NUMBR if is_numbr(value)[0] else const.NUMBAR
    )
  # TROOF Literal
  elif is_troof(value):
    return (const.FAIL, const.TROOF)
  # YARN Literal
  else:
    return (const.EMPTY_STRING, const.YARN)

# any -> NOOB (IMPLICIT)
def IMPLICIT_NOOB(value) -> tuple:
  # TROOF Literal
  if is_troof(value):
    return (const.FAIL, const.TROOF)
  # Other Literals
  else:
    raise Exception(f"{const.NOOB} cannot be implicitly casted into this data type.")

# any -> NUMBR
def NUMBR(value) -> tuple:
  try:
    # TROOF Literal
    new_value = 0
    if value == const.WIN or value == const.FAIL:
      new_value = 1 if value == const.WIN else 0
    # NUMBAR Literal
    elif is_numbar(value)[0]:
      value = float(value)
      new_value = math.trunc(value)
    # Normal Values
    else:
      new_value = int(value)
    return (new_value, const.NUMBR)
  except:
    raise Exception(f"The value cannot be casted into a {const.NUMBR}.")

# any -> NUMBAR
def NUMBAR(value) -> tuple:
  try:
    # Parse WIN or FAIL
    new_value = 0.0
    if value == const.WIN or value == const.FAIL:
      new_value = 1.0 if value == const.WIN else 0.0
    # Normal Values
    else:
      new_value = float(value)
    return (new_value, const.NUMBAR)
  except:
    raise Exception(f"The value cannot be casted into a {const.NUMBAR}.")

# any -> YARN
def YARN(value) -> tuple:
  # NUMBAR Literal
  new_value = ""
  if is_numbar(value)[0] and not is_numbr(value)[0]:
    result = is_numbar(value)[1]
    new_value = f"{int(result * 100) / 100.0:.2f}"
  # NOOB Literal
  elif value == const.NOOB:
    new_value = ""
  # Other Literals (NUMBR, TROOF, & YARN)
  else:
    new_value = str(value)
  return (new_value, const.YARN)

# any -> TROOF
def TROOF(value) -> dict:
  # NUMBR and NUMBAR Literals
  new_value = const.FAIL
  if is_numbr(value)[0] or is_numbar(value)[0]:
    new_value = const.FAIL if is_numbr(value)[1] == 0 or is_numbar(value)[1] == 0 else const.WIN
  # NOOB Literal
  elif value == const.NOOB:
    new_value = const.FAIL
  # YARN Literals
  else:
    new_value = const.FAIL if value == const.EMPTY_STRING else const.WIN
  return (new_value, const.TROOF)

"""
* Type Validators
| To validate a certain data type because
| the table does not recognize them immediately.

* Parameters
| value (dynamic): The value to be typecasted

* Returns
| tuple/bool: Indicates the validity of the data type
| and the parsed value if any
"""
def is_numbar(value) -> tuple:
  try:
    result = float(value)
    return (True, result)
  except:
    return (False, None)

def is_numbr(value) -> tuple:
  try:
    result = int(value)
    return (True, result)
  except:
    return (False, None)

def is_troof(value) -> bool:
  return value == const.WIN or value == const.FAIL