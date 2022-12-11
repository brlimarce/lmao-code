import sys
sys.path.append("../")

from utility import constants as const
from utility.node import Node
from analyzers import typecast, variables

"""
* analyze()
| The main method to analyze variable
| declaration and initialization.
* Parameters
| node (Node): The parent node
| lookup_table (dict): The lookup table
* Returns
| value: computed value for the expression
"""
#ARITHMETIC
def analyze(node: Node, lookup_table: dict, expressions_table: dict) -> tuple:
  terminal_child = len(node.children)
  exprStack = []
  for childindex in range(0, terminal_child):
    var = node.children[childindex]
    #PUSHING VALUES TO STACK, either LITERAL or Variable
    if var[0] == "Parser Delimiter":
      break

    if variables.is_literal(var[1]):
      exprStack.append(check_literal(var)) 
    elif variables.is_variable(var[1]):
      if variables.is_exist(var[0], lookup_table):
        exprStack.append((float(lookup_table[var[0]][const.VALUE_KEY]), lookup_table[var[0]][const.TYPE_KEY]))
      else: #catch unitialized variables
        raise Exception(f"Variable has not been initialized.")
    #OPERATIONS

    # //ARITHMETIC OPERATIONS
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Addition)": #Addition
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      computedValue = checked_values[0] + checked_values[1]
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Subtraction)": #Subtraction
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      computedValue = checked_values[0] - checked_values[1]
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Multiplication)": #Multiplication
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      computedValue = checked_values[0] * checked_values[1]
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Division)": #Division
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      computedValue = checked_values[0] / checked_values[1]
      print(checked_values[1], checked_values[0])
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Modulo)": #Modulo
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      computedValue = checked_values[0] % checked_values[1]
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Max)": #Max
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      if checked_values[0] > checked_values[1]:
        computedValue = checked_values[0]
      else:
        computedValue = checked_values[1]
      exprStack.append((computedValue, checked_values[2]))
      
    elif var[1] ==  f"{const.ARITHMETIC_OP} (Min)": #Min
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      if checked_values[0] > checked_values[1]:
        computedValue = checked_values[1]
      else:
        computedValue = checked_values[0]
      exprStack.append((computedValue, checked_values[2]))

     # //BOOLEAN OPERATIONS  
    elif var[1] ==  f"{const.BOOLEAN_OP} (AND operator)": #AND
      var2 = boolean_type_check(exprStack.pop())
      var1 = boolean_type_check(exprStack.pop())
      if var1 == True and var2 == True:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal"))

    elif var[1] ==  f"{const.BOOLEAN_OP} (OR operator)": #OR
      var2 = boolean_type_check(exprStack.pop())
      var1 = boolean_type_check(exprStack.pop())
      if var1 == True or var2 == True:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal"))

    elif var[1] ==  f"{const.BOOLEAN_OP} (XOR operator)": #XOR
      var2 = boolean_type_check(exprStack.pop())
      var1 = boolean_type_check(exprStack.pop())
      if (var1 == False and var2 == True) or (var2 == False and var1 == True):
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal")) 

    elif var[1] ==  f"{const.BOOLEAN_OP} (NOT operator)": #NOT
      var = boolean_type_check(exprStack.pop())
      if var == True:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal"))

    elif var[1] ==  f"{const.BOOLEAN_OP} (AND with Infinite Arity)":
    #INFINITE AND
      vars = []
      while len(exprStack)>0:
        vars = boolean_type_check(exprStack.pop())
      checkFlag = False
      for value in vars:
        if value == False:
            checkFlag = True
            pushVal = True
            break
      if checkFlag == False:
        pushVal = False
      if pushVal == True:
        exprStack.append((const.WIN, "TROOF Literal"))
      elif pushVal == False:
        exprStack.append((const.FAIL, "TROOF Literal"))

    elif var[1] ==  f"{const.BOOLEAN_OP} (OR with Infinite Arity)":
    #INFINITE OR
      vars = []
      while len(exprStack)>0:
        vars = boolean_type_check(exprStack.pop())
      checkFlag = False
      for value in vars:
        if value == True:
            checkFlag = True
            pushVal = True
            break
      if checkFlag == False:
        pushVal = False
      if pushVal == True:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      elif pushVal == False:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal"))

    elif var[1] ==  f"{const.COMPARISON_OP} (Not Equal)": #Not Equal to
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      if checked_values[0] != checked_values[1]:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal"))

    elif var[1] ==  f"{const.COMPARISON_OP} (Equal)": #Equal to
      var1 = exprStack.pop()
      var2 = exprStack.pop()
      checked_values = arith_type_check(var1, var2)
      if checked_values[0] == checked_values[1]:
        exprStack.append((const.WIN, f"{const.TROOF} Literal"))
      else:
        exprStack.append((const.FAIL, f"{const.TROOF} Literal")) 
  return exprStack.pop()


"""
* check_literal()
| The method to check whether the literal given is either a float or an int
* Parameters
| child: child lexeme
* Returns
| tuple: contains value and type
"""
def check_literal(child: tuple) -> tuple:
    if "." in child[0]:
        return ((float(child[0]), f"{const.NUMBAR} Literal"))
    elif child[1] == f"{const.TROOF} Literal":
        return((child[0], f"{const.TROOF} Literal"))
    else:
        cleanchild = child[0].strip("\"")
        return ((int(cleanchild), f"{const.NUMBR} Literal"))

"""
* arith_type_check()
| The method to check and properly typecast
| the values in an arithmetic operation
* Parameters
| var1 and var2: the values to be used in the arithmetic operation
* Returns
| list: contains the converted values and the final typecast the value will have
"""
def arith_type_check(var1: tuple, var2: tuple) -> list:
  #check if var1 is literal, numbar or numbr, then typecast

  value1 = 0
  value2 = 0

  #check var1
  if var1[1] == const.LITERAL or var1[1] == f"{const.NUMBAR} Literal" or var1[1] == f"{const.NUMBR} Literal":
    value1 = float(var1[0])
  elif var1[1] == f"{const.TROOF} Literal":
    value1 = float(typecast.NUMBAR(var1[0])[0])
  elif var1[1] == const.NOOB:
    raise Exception(f"{const.NOOB} cannot be used in this operation") 

  #check var2
  if var2[1] == const.LITERAL or var2[1] == f"{const.NUMBAR} Literal" or var2[1] == f"{const.NUMBR} Literal":
    value2 = float(var2[0])
  elif var2[1] == f"{const.TROOF} Literal":
    value2 = float(typecast.NUMBAR(var2[0])[0])
  elif var1[1] == const.NOOB:
    raise Exception(f"{const.NOOB} cannot be used in this operation") 

  #if both are NUMBRs, resulting value is a NUMBR, else it's a NUMBAR
  if var1[1] == f"{const.NUMBAR} Literal" or var2[1] == f"{const.NUMBAR} Literal":
    answerType = f"{const.NUMBAR} Literal"
  else:
    answerType = f"{const.NUMBR} Literal"

  #TODO: Casting Literals
  return (value1, value2, answerType)

"""
* boolean_type_check()
| The method to check and properly typecast
| a value in a boolean operation
* Parameters
| var1: the values to be used in the boolean operation
* Returns
| boolVal: boolean representation of WIN and FAIL
"""
def boolean_type_check(var: tuple) -> list:
  #check if var1 is literal, numbar or numbr, then typecast
  if var[1] == const.LITERAL or var[1] == f"{const.NUMBAR} Literal" or var[1] == f"{const.NUMBR} Literal":
    casted = typecast.TROOF(var[0])
  elif var[1] == f"{const.TROOF} Literal":
    casted = var 

  if casted[0] == const.WIN:
    boolVal = True
  elif casted[0] == const.FAIL:
    boolVal = False
  return(boolVal)
