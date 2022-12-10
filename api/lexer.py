# from api.utility import constants as const
# from api.utility import token_regex as tokex
from utility import constants as const
from utility import token_regex as tokex
import re

"""
* Lexer
| Performs lexical analysis and returns
| a symbol table of lexemes.
"""
class Lexer:
  # * Properties
  _program = []
  _multiline_flag = False

  # * Constructor
  def __init__(self, program):
    self._program = program
  
  """
  * raise_error()
  | Return a formatted version of the error.

  * Parameters
  | line_number (int): The line number in the program
  | token (str): The invalid token
  """
  def raise_error(self, line_number: int, token: str):
    return f"🚀 ~ Error on Line {line_number}: {token} is an invalid token."

  """
  * find_match()
  | Obtain all lexemes for a particular line

  * Parameters
  | line_number (int): The line number in the program
  | line (list): List of lexemes for a line in the program
  """
  def find_match(self, line_number: int, line: list) -> list:
    # * Declaration
    lexemes = tokex.token_regex
    result = []
    
    # Find matches until line is exhausted.
    while line != const.EMPTY_STRING:
      match = None
      for lex in lexemes:
        # Find a match based on the lexeme.
        match = re.match(lex[0], line)
        if match != None:
          # End the loop if it is a MULTILINE comment.
          if self._multiline_flag and lex[2] != const.TLDR_KEYWORD:
            line = const.EMPTY_STRING
            break

          # Replace the space delimiter of keywords with multiple
          # words into underscores.
          token = match.group(0)
          if const.SPACE in match.group(0) and lex[2] != f"{const.YARN} Literal":
            new_token = const.UNDERSCORE.join(match.group(0).split(const.SPACE))
            line = line.replace(token, new_token, 1)
            token = new_token

          # Append the match to the result
          result.append((token, lex[2]))

          # Catch SINGLE comments.
          if lex[2] == const.BTW_KEYWORD:
            line = const.EMPTY_STRING
            break
            
          # Catch MULTILINE comments.
          if lex[2] == const.OBTW_KEYWORD and not self._multiline_flag:
            self._multiline_flag = True
            line = const.EMPTY_STRING
            break
          
          # End the flag if TLDR keyword is found.
          if lex[2] == const.TLDR_KEYWORD and self._multiline_flag:
            self._multiline_flag = False

          # Catch YARN literals.
          if lex[2] != const.YARN_LITERAL and token not in line.split(const.SPACE):
            raise Exception(self.raise_error(line_number, line))
          line = self.remove_match(line, match.start(), match.end())
          break
      # The line isn't exhausted and there's no match.
      if line != "" and match == None:
        raise Exception(self.raise_error(line_number, line))
    return result
  
  """
  * remove_match()
  | Remove the match from the current line.

  * Parameters
  | line (str): A certain line in the program
  | start (int): The starting index of the string
  | end (int): The ending index of the string
  """
  def remove_match(self, line: str, start: int, end: int):
    return line[:start] + line[end + 1:]

  """
  * analyze()
  | The main method for lexical analysis

  * Returns
  | tuple: Contains a flag for any error/s and
  | the payload (symbol table or error message)
  """
  def analyze(self) -> tuple:
    try:
      # Run through each statement.
      symbol_table = {}
      for i in range(len(self._program)):
        result = self.find_match(i + 1, self._program[i])
        
        # Disregard empty results (i.e. comments).
        if result != []:
          symbol_table[i + 1] = result
      return (True, symbol_table)
    except Exception as e:
      # Return the error thrown.
      return (False, str(e))

# * Note: Uncomment this code block if needed.
if __name__ == '__main__':
  code = []
  # * NOTE: Replace `01_variables.lol` with your file name.
  with open('test/input.lol', 'r') as infile:
    for line in infile.readlines():
      code.append(line[:-1].strip())
  
  # Instantiate the lexer.
  lexer = Lexer(code)
  print(lexer.analyze())