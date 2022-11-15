from utility import constants as const
import re
import token_regex as tokex

'''
* matching()
| Checks if the token matches the lexeme.

* Parameters
|

* Returns
|
'''
def matching(token: str):
  # # * Declaration
  print()
  # valid = False

  # Check if the token is valid.

  # return valid

	# valid = False
	# with open("regex.txt",'r') as data_file:
	# 	for line in data_file:
	# 		lexeme = line.strip()
	# 		x = re.search(lexeme, token)
	# 		if x != None:
	# 			valid = True
	# return valid

'''
* eval_statement()
| Find the tokens of the WHOLE statement.
| Otherwise, return an error.

* Parameters
| line (str): The line/statement of the program.

* Returns
| tuple (bool, list): `bool` indicates if there
| were no errors. `list` is for the tokens.
'''
def eval_statement(line: str) -> tuple:
  result = (True, '')
  line = line[:-1].strip() # Clean the line.

  # Evaluate the statement.
  matching(line)

  # Return the result.
  return result

'''
* analyze()
| Return a symbol table based on
| a given program.

* Parameters
| filename (str): The file with .lol extension.

* Returns
| list: The symbol table.
'''
def analyze(filename: str) -> list:
  # * Declaration
  symbol_table = []
  line_count = 0 # The line number.

  # Evaluate the program.
  with open(const.TEST_DIR + filename, 'r') as program:
    for line in program.readlines():
      line_count += 1
      try:
        result = eval_statement(line) # Evaluate the statement
        if result[0] == False:
          raise Exception(f'Error at line {line_count}. Invalid word: {result[1]}')
      except Exception as e:
        print(e) # Print an error message.
        return
  # Return the symbol table.
  return symbol_table

# * Main Program
if __name__ == '__main__':
  analyze('sample.lol')
