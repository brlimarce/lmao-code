import re

def matching(token):
	valid= False
	with open("regex.txt",'r') as data_file:
		for line in data_file:
			lexeme= line.strip()
			x = re.search(lexeme, token)

			if (x != None):
				valid= True	
				
	if(valid == False):
		print("Invalid Syntax: "+ token)
	return valid

print(matching("WIN"))