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
def analyze(node: Node, lookup_table: dict, var = const.IT) -> dict:
  # Cast depending on the type.
  cast_type = node.children[len(node.children) - 1].lexeme
  value = lookup_table[node.children[0].lexeme] if node.type == "Explicit Typecasting" else lookup_table[node.lexeme]

  # * YARN
  value = value[const.VALUE_KEY]
  print(cast_type)
  if cast_type == const.YARN:
    YARN(value, var, lookup_table)
  # * NOOB
  elif cast_type == const.NOOB:
    NOOB(value, var, lookup_table)
  # * TROOF
  elif cast_type == const.TROOF:
    TROOF(value, var, lookup_table)
  # * NUMBAR
  elif cast_type == const.NUMBAR:
    NUMBAR(value, var, lookup_table)
  # * NUMBR
  elif cast_type == const.NUMBR:
    NUMBR(value, var, lookup_table)
  return lookup_table

"""
* Typecasters
| Broken down into different methods for
| modularity and easier debugging.

* Parameters
| value (dynamic): The value to be typecasted
| varname (str): Name of the variable
| lookup_table (dict): The lookup table

* Returns
| dict: The updated lookup table
"""
# any -> NOOB
def NOOB(value, varname: str, lookup_table: dict) -> dict:
  # NUMBR and NUMBAR Literals
  if is_numbr(value)[0] or is_numbar(value)[0]:
    lookup_table[varname] = {
      const.VALUE_KEY: 0 if is_numbr(value)[1] == 0 else 0.0,
      const.TYPE_KEY: const.NUMBR if is_numbr(value)[0] else const.NUMBAR
    }
  # TROOF Literal
  elif is_troof(value):
    lookup_table[varname] = {
      const.VALUE_KEY: const.FAIL,
      const.TYPE_KEY: const.TROOF
    }
  # YARN Literal
  else:
    lookup_table[varname] = {
      const.VALUE_KEY: const.EMPTY_STRING,
      const.TYPE_KEY: const.YARN
    }

# any -> NUMBR
def NUMBR(value, varname: str, lookup_table: dict) -> dict:
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
    
    lookup_table[varname] = {
      const.VALUE_KEY: new_value,
      const.TYPE_KEY: const.NUMBR
    }

    return lookup_table
  except:
    raise Exception(f"The value cannot be casted into a {const.NUMBR}.")

# any -> NUMBAR
def NUMBAR(value, varname: str, lookup_table: dict) -> dict:
  try:
    # Parse WIN or FAIL
    new_value = 0.0
    if value == const.WIN or value == const.FAIL:
      new_value = 1.0 if value == const.WIN else 0.0
    # Normal Values
    else:
      new_value = float(value)
    
    lookup_table[varname] = {
      const.VALUE_KEY: new_value,
      const.TYPE_KEY: const.NUMBAR
    }

    return lookup_table
  except:
    raise Exception(f"The value cannot be casted into a {const.NUMBAR}.")

# any -> YARN
def YARN(value, varname: str, lookup_table: dict) -> dict:
  # NUMBAR Literal
  new_value = ""
  if is_numbar(value)[0]:
    result = is_numbar(value)[1]
    new_value = f"{int(result * 100) / 100.0:.2f}"
  # NOOB Literal
  elif value == const.NOOB:
    new_value = const.EMPTY_STRING
  # Other Literals (NUMBR, TROOF, & YARN)
  else:
    new_value = str(value)
  lookup_table[varname] = {
    const.VALUE_KEY: new_value,
    const.TYPE_KEY: const.YARN
  }
  return lookup_table

# any -> TROOF
def TROOF(value, varname: str, lookup_table: dict) -> dict:
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
  
  lookup_table[varname] = {
    const.VALUE_KEY: new_value,
    const.TYPE_KEY: const.TROOF
  }
  return lookup_table

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