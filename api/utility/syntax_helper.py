"""
* Syntax Helper
| Contains helper functions aside from the
| grammar in syntax storage.
"""
from utility import constants as const
from utility import syntax_storage

# Check if the list has no more elements.
def is_end(lex):
  return len(lex) <= 0

# Evaluate the code block of a structured construct.
def evaluate_block(code, root, is_gtfo):
  while code != []:
    # Variable declaration should not be in
    # conditional statements.
    if code[0][1] == const.VAR_DECLARATION:
      return (False, "Cannot declare variables in this scope")
    
    # Evaluate the expression.
    result = syntax_storage.codeblock(code, root, is_gtfo)
    if not result[0]:
      return(False, result[1])
    code = result[1]
  return (True, result[1])

# For conditionals to evaluate the entire code block.
def evaluate_code(lex_copy, root, croot, else_flag = False):
  # * Declaration
  lex_copy = lex_copy[2:len(lex_copy)]
  block = []
  index = 0

  # Get the code block.
  for e in lex_copy:
    # End if it reaches NO WAI or OIC.
    if else_flag:
      if e[1] == "Keyword for the ELSE Case" or e[1] == "End of Conditional Statement":
        break
    else:
      if e[1] == "End of Conditional Statement":
        break
    block.append(e)
    index += 1
  
  # Check if the statements are valid.
  result = evaluate_block(block, croot, False)
  if not result[0]:
    return (result[0], result[1], root)
  return (True, lex_copy[index:], croot)

# Evaluate the code block of a switch case.
def evaluate_switch_code(lex_copy, root, sroot, default_flag = False):
  # * Declaration
  block = []
  index = 0

  # Get the code block.
  for e in lex_copy:
    # End if it reaches NO WAI or OIC.
    if default_flag:
      if e[1] == "End of Conditional Statement":
        break
    else:
      if e[1] == "Keyword for the SWITCH Case" or e[1] == "Keyword for the Default Case" or e[1] == "End of Conditional Statement":
        break
    block.append(e)
    index += 1
  # Check if the statements are valid.
  result = evaluate_block(block, sroot, True)
  if not result[0]:
    return (result[0], result[1], root)
  return (True, lex_copy[index:], sroot)

# Stores the list of operations (arithmetic, boolean, and comparison).
operations= [f"{const.ARITHMETIC_OP} (Addition)", f"{const.ARITHMETIC_OP} (Subtraction)", f"{const.ARITHMETIC_OP} (Multiplication)",
                f"{const.ARITHMETIC_OP} (Division)", f"{const.ARITHMETIC_OP} (Modulo)", f"{const.ARITHMETIC_OP} (Max)", 
                f"{const.ARITHMETIC_OP} (Min)", f"{const.COMPARISON_OP} (Not Equal)", f"{const.COMPARISON_OP} (Equal)",
                f"{const.BOOLEAN_OP} (AND operator)", f"{const.BOOLEAN_OP} (OR operator)", f"{const.BOOLEAN_OP} (XOR operator)",
                f"{const.BOOLEAN_OP} (AND with Infinite Arity)", f"{const.BOOLEAN_OP} (OR with Infinite Arity)",  
                f"{const.BOOLEAN_OP} (NOT operator)"]