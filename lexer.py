import re
import token_regex as token

'''
'''
def matching(token: str) -> bool:
	valid = False
	with open("regex.txt",'r') as data_file:
		for line in data_file:
			lexeme= line.strip()
			x = re.search(lexeme, token)
			if x != None:
				valid = True
	return valid

'''
'''
def evaluate_statement(statement: str):
  print()

'''
'''
def analyze_program(filename: str):
  print()

print(matching("WIN"))