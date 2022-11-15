from utility import constants as const
import re
import token_regex as tokex

"""
* matching()
| Checks if the token matches the lexeme.

* Parameters
|

* Returns
|
"""
def matching(line: str) -> tuple:
  # * Declaration
  lexemes = tokex.token_regex

  # Extract all tokens.
  result = []
  print("🚀 ~ file: lexer.py ~ line 22 ~ line", line)
  indices = [5, 49]
  
  # for idx in indices:
  # line = re.split(lexemes[5][0], line)[1].strip()
  # print(line)
  # line = re.split(lexemes[49][0], line)
  # print(line)
  # while line != " " and line != "" and line != None:
  #   is_match = False
  #   print("🚀 ~ file: lexer.py ~ line 24 ~ line:", line + "|")
  #   for i in range(len(lexemes)):
  #     x = re.search(lexemes[i][0], line)
  #     if x != None:
  #       result.append({ x.group(0): lexemes[i][1] })
  #       line = line[x.end():].strip()
  #       is_match = True
  #       break
  #   if not is_match and (line != " " or line != "" or line != None):
  #       return (False, line)
    # print("Index:", i, lexemes[i][0], lexemes[i][1])
  # valid = False

  # Check if the token is valid.

  # return valid

	# valid = False
	# with open("regex.txt","r") as data_file:
	# 	for line in data_file:
	# 		lexeme = line.strip()
	# 		x = re.search(lexeme, token)
	# 		if x != None:
	# 			valid = True
	# return valid
  return (True, result)

"""
* eval_statement()
| Find the tokens of the WHOLE statement.
| Otherwise, return an error.

* Parameters
| line (str): The line/statement of the program.

* Returns
| tuple (bool, list): `bool` indicates if there
| were no errors. `list` is for the tokens.
"""
def eval_statement(line: str) -> tuple:
  # Return the result.
  return matching(line[:-1].strip())

"""
* analyze()
| Return a symbol table based on
| a given program.

* Parameters
| filename (str): The file with .lol extension.

* Returns
| dict: The symbol table. `key` is line number
| and `value` is the list of tokens.
"""
def analyze(filename: str) -> dict:
  # * Declaration
  symbol_table = {}
  line_count = 0 # The line number.

  # Evaluate the program.
  with open(const.TEST_DIR + filename, "r") as program:
    for line in program.readlines():
      line_count += 1
      try:
        result = eval_statement(line) # Evaluate the statement
        break
        print("🚀 ~ file: lexer.py ~ line 85 ~ result", result, "\n")
        if result[0] == False:
          raise Exception(f"🚀 ~ Error at line {line_count} ~ {result[1]} does not exist.")
      except Exception as e:
        print(e) # Print an error message.
        return
  # Return the symbol table.
  return symbol_table

# * Main Program
if __name__ == "__main__":
  analyze("sample.lol")
