from api.utility import constants as const
from api.utility import token_regex as tokex
import re
import copy as cpy

"""
* merge()
| Separate multi-word keywords via an underscore.

* Parameter
| match (str): The match/keyword.
"""
def merge(match: str):
  return const.UNDERSCORE.join(match.split(" "))

"""
* matching()
| Checks if the token matches the lexeme.

* Parameters
| line(str): A line in the program.
| line_number (int): The line number in the program.
| flag (bool): Flag for tracking comments.

* Returns
| tuple: `boolean` indicates if success and `result`
| contains a list of tokens.
"""
def matching(line: str, flag: bool) -> tuple:
  # * Declaration
  lexemes = tokex.token_regex
  statement = cpy.deepcopy(line)
  idx = 0

  # If statement that handles multi-line comments (when OBTW is found).
  if flag == True: # Comment flag
    if re.match(lexemes[4][0], line): # If it matches TLDR
      return ((True, False), None) # TLDR was found, turn off comment_flag.
    else: 
      return ((True, True), None) # TLDR not found, keep on.

  # Extract all tokens.
  result = []
  while line != " " and line != "" and line != None:
    # Flag for indicating the match.
    is_match_found = False
    is_string_literal = False
    is_btw = False # To avoid validating comments in the lexeme checker.

    # Run through the line.
    for i in range(len(lexemes)):
      x = re.match(lexemes[i][0], line)
      if x != None:
        # Disregard if BTW is read (Single Comment).
        if x.group(0) == "BTW":
          line = None # Disregard everything else after `BTW`.
          is_match_found = True
          is_btw = True
          break
        if x.group(0) == "OBTW":
          if result == []:
          # For OBTW, it has to exist by itself. If it's found with other lexemes, raise an error.
            return ((True, True), None)
          else:
            raise Exception(const.MISPLACED_OBTW)
        
        # `statement` is used to check for "dangling literals".
        if i == const.YARN_CASE_NUMBER:
          is_string_literal = True
          result = validate_lexeme(x.group(0), idx, is_string_literal, result)
        else:
          statement = statement.replace(x.group(0), merge(x.group(0)))

        # Append the result and cut the match off the line.
        result.append((x.group(0), lexemes[i][1]))
        line = line[x.end():].strip()
        is_match_found = True
        break
    
    # If there is no match, raise an error.
    if not is_match_found:
      return ((False, False), line)
    else:
      if not is_string_literal and not is_btw:
        # Check if the lexeme does not have dangling literals.
        result = validate_lexeme(statement, idx, is_string_literal, result)
    idx += 1
  return ((True, False), result)

"""
* validate_lexeme()
| Extra validation to remove `dangling literals`.

* Parameters
| statement (str): The line in the program.
| line_count (int): The line number.
| boundary (int): Index number (limit).
| is_string_literal (bool): Flag to indicate if it is a string literal.
| result (list): List of result

* Returns
| list: The modified result
"""
def validate_lexeme(statement: str, boundary: int, is_string_literal: bool, result: list) -> list:
  # * Declaration
  statement = [s for s in statement.split() if s != '"'] if not is_string_literal else statement.strip()
  boundary = boundary if not is_string_literal else 0
  error = f"{const.INVALID_TOKEN} ~ {statement[boundary] if not is_string_literal else statement} does not exist."

  if not is_string_literal:
    # Disregard comments.
    if statement[boundary] == "BTW":
      return
    else:
      statement[boundary] = " ".join(statement[boundary].split(const.UNDERSCORE))
      for c in statement[boundary]:
        if not c.isalnum() and not c.isspace() and c not in tokex.accepted_chars:
          raise Exception(f"{error}")
  return result

"""
* analyze()
| Return a symbol table based on
| a given program.

* Parameters
| code (list): A list of the program's lines

* Returns
| dict: The symbol table. `key` is line number
| and `value` is the list of tokens.
"""
def analyze(code: list) -> dict:
  # * Declaration
  symbol_table = {}
  line_count = 0 # The line number.
  comment_flag = False
  
  # Evaluate the program.
  for line in code:
    line_count += 1
    try:
      result = matching(line, comment_flag) # Evaluate the statement.
      if result[0][0] == False:
        return (False, f"~ Line {line_count}: {const.INVALID_TOKEN}: {result[1]}")
      else:
        comment_flag = result[0][1]
      
        # Append the result.
        if result[1] != None:
          symbol_table[line_count] = result[1]
    except Exception as e:
      return (False, f'"~ Line {line_count}: {e}')
  # Return the symbol table.
  return (True, symbol_table)
