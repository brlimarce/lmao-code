from utility import constants as const
from utility import helper
import re
import token_regex as tokex

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
def matching(line: str, line_number: int, flag: bool) -> tuple:
  # * Declaration
  lexemes = tokex.token_regex

  # if statement that handles multi-line comments (when OBTW is found)
  if flag == True: # comment_flag determines wheth
    if re.match(lexemes[4][0], line): #if it matches TLDR
      return ((True, False), None) #TLDR was found, turn off comment_flag
    else: 
      return ((True, True), None) #TLDR not found, keep on

  # Extract all tokens.
  result = []
  while line != " " and line != "" and line != None:
    for i in range(len(lexemes)):
      x = re.match(lexemes[i][0], line)
      if x != None:
        # Disregard if BTW is read (Single Comment).
        if x.group(0) == "BTW":
          line = None # Disregard everything else after `BTW`.
          break
        if x.group(0) == "OBTW":
          if result == []:
          # For OBTW, it has to exist by itself. If it's found with other lexemes, raise an error.
            return ((True, True), None)
          else:
            raise Exception(f"🚀 ~ Error at line {line_number} ~ OBTW/TLDR are misplaced.")
        result.append((x.group(0), lexemes[i][1]))
        line = line[x.end():].strip()
        break
  return ((True, False), result)

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
  comment_flag = False
  
  # Evaluate the program.
  with open(const.TEST_DIR + filename, "r") as program:
    for line in program.readlines():
      line_count += 1
      try:
        result = matching(line[:-1].strip(), line_count, comment_flag) # Evaluate the statement.
        if result[0][0] == False:
          raise Exception(f"🚀 ~ Error at line {line_count} ~ {result[1]} does not exist.")
        else:
          comment_flag = result[0][1]
        
          # Append the result.
          if result[1] != None:
            symbol_table[line_count] = result[1]
      except Exception as e:
        print(e) # Print an error message.
        return None
  # Return the symbol table.
  return symbol_table

# * Main Program
if __name__ == "__main__":
  # Analyze the program.
  filename = "comments.lol"
  symbol_table = analyze(filename)
  
  # Display the symbol table.
  if symbol_table != None:
    helper.print_symbol_table(filename, symbol_table)
