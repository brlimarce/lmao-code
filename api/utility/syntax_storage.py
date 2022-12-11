from utility import constants as const
from utility.node import Node
from utility.syntax_helper import *
from copy import deepcopy
from analyzers import variables, typecast

"""
* For all the grammar functions
* Parameters
| lex (list): List of lexemes with - separator by statement

* Return Statement
| (Tuple) [0]: boolean - True(no error) or False(error)
|         [1]: lex - updated list of lexemes; tokens for the grammar are removed
"""

"""
* comment()
| checks for the grammar of comments
"""
def comments(lex):
    ind_mult_comment = 0
    comments = []
    flag_comment = False
    line_error = 0
    cnt = 0
    # iterate through the lex elements: finds the commment token and remove from lex
    for element in lex:
        # if TLDR is encountered first without OBTW key word: error
        if element[1] == "End of Multiline Comment" and flag_comment == False:
            line_error = element[2]
            return (False, "Invalid comments", line_error)
        # checks the index of the OBTW keyword
        if element[1] == 'Start of Multiline Comment':
            flag_comment = True
            line_error = element[2]
            ind_mult_comment = cnt
            comments.append(element)
        # checks if a TLDR keyword exist after OBTW
        if cnt == ind_mult_comment + 1 and flag_comment == True:
            if element[1] == "End of Multiline Comment":
                flag_comment = False
                comments.append(element)
        # checks for all the single line comment
        if element[1] == "Single Comment":
            comments.append(element)
        cnt = cnt+1
    # if error: return error statement
    if flag_comment == True:
        return (False, "Invalid comments", line_error)
    # no error: return the updated lex w/out the comment tokens
    else:
        for c in comments:
            lex.remove(c)
        return (True, lex)

"""
* program_start()
| checks for the start and end of the program
| removes HAI and KTHXBYE keyword from the lex list
* Parameters
| lex (list): List of lexemes with - separator by statement

* Return Statement
| (Tuple) [0]: boolean - True(no error) or False(error)
|         [1]: lex - updated list of lexemes; tokens for the grammar are removed
"""
def program_start(lex):
    # Grammar
    program = ["Program Start", "statement", "Program End"]

    if lex[0][1] != program[0]:
        return (False, "No HAI keyword")
    elif lex[-1][1] != program[-1]:
        return (False, "No KTHXBYE keyword")
    else:
        return (True, lex[2:-1], Node(None, None, lex[0][0], lex[0][1]))

"""
* statement()
| grammar of statement
"""
def statement(lex, root):
    _codeblock = codeblock(lex, root)
    return _codeblock

"""
* codeblock()
| grammar of codeblock
"""
def codeblock(lex, root, is_gtfo=False):
    # statement= [["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],
    # ["vardeclaration"],["print"],["typecasting"],["concatenation"],["assignment"]]
    
    # * Identifier (for SMOOSH)
    if lex[0][1] == "Identifier" and lex[1][1] == const.DASH:
      _smoosh = smoosh_var(lex, root)
      if _smoosh[0] == True:
          lex = _smoosh[1]
          return (True, lex)
      else:
          return (False, "Invalid variable", lex[0][2])
    
    # * Print
    if lex[0][1] == const.PRINT:
        _print = print_statement(lex, root)
        if _print[0] == True:
            lex = _print[1]
            return (True, lex)
        else:
            return (False, "Invalid printing", lex[0][2])
    
    # * Input
    if lex[0][1] == const.INPUT:
        _userinput = userinput(lex, root)
        if _userinput[0] == True:
            lex = _userinput[1]
            return (True, lex)
        else:
            return (False, "Invalid user input", lex[0][2])
    
    # * Variable Declaration
    if lex[0][1] == const.VAR_DECLARATION:
        _vardeclaration = vardeclaration(lex, root)
        if _vardeclaration[0] == True:
            lex = _vardeclaration[1]
            return (True, lex)
        else:
            return (False, "Invalid variable declaration", lex[0][2])
    
    # * Typecasting
    if lex[0][1] == const.TYPECAST[0] or (len(lex) > 2 and lex[1][1] == const.TYPECAST[1]) or (len(lex) > 3 and lex[2][1] == const.TYPECAST[0]):
        _typecast = typecast(lex, root)
        if _typecast[0] == True:
            lex = _typecast[1]
            return (True, lex)
        else:
            return (False, "Invalid typecasting", lex[0][2])
   
    # * Assignment
    if (len(lex) > 2 and lex[1][1] == const.ASSIGNMENT):
        _assignment = assignment(lex, root)
        if _assignment[0] == True:
            lex = _assignment[1]
            return (True, lex)
        else:
            return (False, "Invalid assignment", lex[0][2])
    
    # * Concatenation
    if lex[0][1] == const.CONCAT:
        _concat = concat(lex, root, True)
        if _concat[0] == True:
            lex = _concat[1]
            return (True, lex)
        else:
            return (False, "Invalid Concatenation", lex[0][2])
    
    # * IF-THEN Statement
    if lex[0][1] == "Start of IF-THEN Statement":
      _conditional = conditional(lex, root)
      if _conditional[0]:
        lex = _conditional[1]
        return (True, lex)
      return (False, _conditional[1], lex[0][2])
    
    # * SWITCH Case Statement
    if lex[0][1] == "Start of SWITCH Case Statement":
      _switch = switch(lex, root)
      if _switch[0]:
        lex = _switch[1]
        return (True, lex)
      return (False, _switch[1], lex[0][2])
    
    # * Loops
    if lex[0][1] == "Start of Loop":
      _loop = loop(lex, root)
      if _loop[0]:
        lex = _loop[1]
        return (True, lex)
      return (False, _loop[1], lex[0][2])
    
    # * GTFO Statement
    if lex[0][1] == "Loop Break":
      _break = break_block(lex, root, is_gtfo)
      if _break[0]:
        lex = _break[1]
        return (True, lex)
      return (False, _break[1], lex[0][2])
    
    # * Operation
    if lex[0][1] in operations:
        _operation = operation(lex, root, operations, True)
        if _operation[0] == True:
            lex = _operation[1]
            return (True, lex)
        else:
            return (False, "Invalid operation", lex[0][2])
    
    # * Expression
    else:
        _expression = expression(lex, root)
        return _expression

"""
* expression()
| grammar of expression
"""
def expression(lex, root):
    # expression [["arithmetic"], ["boolean"], ['comparison']]

    # Break if there are no more lexemes.
    if lex == []:
        return (True, lex)

    # * Arithmetic, Comparison, Boolean, Relational
    if lex[0][1] in operations:
        _operation = operation(lex, root, operations, False)
        if _operation[0] == True:
            lex = _operation[1]
            return (True, lex)
        else:
            return (False, "Invalid operation", lex[0][2])
    
    # * Smoosh
    if lex[0][1] == "String Concatenation":
      _concat = concat(lex, root)
      if _concat[0]:
        lex = _concat[1]
        return (True, lex)
      return (False, "Invalid concatenation", lex[0][2])

    else:
        # Get the unidentified line in the program.
        error_block = []
        for element in lex:
          if element[1] == const.DASH:
            break
          error_block.append(element[0])
        error = f"Cannot identify {' '.join(error_block)}"

        # Display the error.
        if len(lex[0]) < 3:
          return (False, error, 0)
        return (False, error, lex[0][2])

"""
* smoosh_var()
| Transfer the value of a variable to
| IT if the former exists.
"""
def smoosh_var(lex, root):
  root.add_child(Node(root, root, lex[0][0], lex[0][1]))
  lex = lex[2:]
  return (True, lex)

"""
* print_statement()
| grammar for printing

| ! Note: Does not support AN keyword.
"""
def print_statement(lex, root):
  # * Declaration
  print_node = Node(root, root, lex[0][0], lex[0][1])
  lex_copy = deepcopy(lex[1:])

  # Check if the output is a literal,
  # variable, or expression.
  while not is_end(lex_copy) and lex_copy[0][1] != const.DASH:
    # Literal
    if variables.is_literal(lex_copy[0][1]):
      print_node.add_child(Node(print_node, root, lex_copy[0][0], lex_copy[0][1]))
    # Variable
    elif variables.is_variable(lex_copy[0][1]):
      print_node.add_child(Node(print_node, root, lex_copy[0][0], lex_copy[0][1]))
    # Expression
    else:
      return (False, "Expressions are not yet supported.", root)
    lex_copy = lex_copy[1:]
  root.add_child(print_node)
  lex = lex_copy[1:]
  return (True, lex, root)

"""
* userinput()
* calls varident()
| grammar for getting input from user
"""
def userinput(lex, root):
    _userinput = [["Input", varident()]]

    return abstraction(_userinput, lex, root)

"""
* assignment()
| grammar of assignment
"""
def typecast(lex, root):
    _typecast = [["Explicit Typecasting", varident(), datatype()],
                 ["Explicit Typecasting", varident(
                 ), "Delimiter for Typecasting", datatype()],
                 [varident(), "Delimiter for Typecasting", datatype()],
                 [varident(), "Variable Assignment", "Explicit Typecasting", varident(), datatype()]]

    return abstraction(_typecast, lex, root)

def datatype():
    return "TYPE Literal"

"""
* assignment()
* calls varident(), literal()
| grammar for assignment
"""
def assignment(lex, root):
    _expression = ("-", "expression")
    _assignment = [[varident(), "Variable Assignment", literal()],
                   [varident(), "Variable Assignment", varident()],
                   [varident(), "Variable Assignment", _expression]]

    return abstraction(_assignment, lex, root)

"""
* vardeclaration()
| grammar of variable declaration
"""
def vardeclaration(lex, root):
    _expression = ("-", "expression")
    _vardeclaration = [
        ["Variable Declaration", varident(), "Variable Initialization", varident()],
        ["Variable Declaration", varident(), "Variable Initialization", literal()],
        ["Variable Declaration", varident()],
        ["Variable Declaration", varident(), "Variable Initialization", _expression], ]

    return abstraction(_vardeclaration, lex, root)

"""
* concat()
| grammar for concatenation
"""
def concat(lex, root, is_standalone=False):
    index = 0
    result = True
    
    for e in lex:
        if e[1] == const.DASH:
            last_ind = index
            if lex[last_ind - 1][1] == 'Delimiter for Nested Expressions':
                result = False
            break
        if (index != 0) and (index % 2 == 0):
            if e[1] != 'Delimiter for Nested Expressions':
                result = False
        else:
            if e[1] == 'Delimiter for Nested Expressions':
                result = False
        index = index+1
    
    # Throw an exception if there is nothing to concatenate.
    if index == 1:
      result = False
    
    # Add to the root if it is a standalone
    # statement only.
    if is_standalone:
      node = get_syntax_tree(lex[:index], root)
      root.add_child(node)

    lex = lex[index + 1:]
    return (result, lex, root)

"""
* conditional()
| grammar for if-then statement

* Note: Some statements are already being
* translated along the way.
"""
def conditional(lex, root):
  # * Declaration
  croot = Node(root, root, lex[0][0], lex[0][1])
  lex_copy = deepcopy(lex)[2:len(lex)]

  # Check if IF CASE is present (required).
  if is_end(lex_copy) or lex_copy[0][1] != "Keyword for the IF Case":
    return (False, "Cannot find YA RLY", root)
  
  # Check the code block inside IF CASE.
  ifnode = Node(croot, root, lex_copy[0][0], lex_copy[0][1])
  block = evaluate_code(lex_copy, root, croot, True)
  if not block[0]:
    return (False, block[1], root)
  
  for child in croot.children:
    ifnode.add_child(child)
  croot.slice_children(len(croot.children), len(croot.children))
  lex_copy = block[1]

  # Check if an ELSE block exists.
  else_node = None
  if len(lex_copy) > 0 and lex_copy[0][1] == "Keyword for the ELSE Case":
    else_node = Node(croot, root, lex_copy[0][0], lex_copy[0][1])
    block = evaluate_code(lex_copy, root, croot)
    if not block[0]:
      return (False, block[1], root)

    for child in croot.children:
      else_node.add_child(child)
    croot.slice_children(len(croot.children), len(croot.children))
    
  # Add the IF and ELSE (if applicable) nodes.
  croot.add_child(ifnode)
  if else_node != None:
      croot.add_child(else_node)
  lex_copy = block[1]
  
  # Check if there is an OIC.
  if is_end(lex_copy) or (len(lex_copy) > 0 and lex_copy[0][1] != "End of Conditional Statement"):
    return (False, "There is no delimiter for ending the condition", root)
  
  # Add the AST to the root.
  root.add_child(croot)
  lex = lex_copy[2:]
  
  return (True, lex, root)

"""
* switch()
| grammar of switch-case statement
"""
def switch(lex, root):
  # * Declaration
  sroot = Node(root, root, lex[0][0], lex[0][1])
  lex_copy = deepcopy(lex)[2:len(lex)]
  case_children = []

  # Throw an error if DEFAULT case is first.
  if is_end(lex_copy) or lex_copy[0][1] != "Keyword for the SWITCH Case":
    return (False, "Missing OMG keyword", root)

  # Check the validity of each case.
  case = lex_copy[0]
  while lex_copy != [] and case[0][1] != "Keyword for the Default Case":
    case = lex_copy
    if case[0][1] != "Keyword for the Default Case":
      # End the switch-case statement.
      if case[0][1] == "End of Conditional Statement":
        break
      
      # Check if the value is a literal.
      if (lex_copy == [] or not variables.is_literal(case[1][1])):
        return (False, "No literal found for OMG case", root)
      case_node = Node(sroot, root, case[0][0], case[0][1])
      value_node = Node(case_node, sroot, case[1][0], case[1][1])
      case_node.add_child(value_node)

      # Check the code block.
      lex_copy = lex_copy[3:]
      block = evaluate_switch_code(lex_copy, root, sroot)
      if not block[0]:
        return (False, block[1], root)
      
      # Add the children as nodes.
      for child in sroot.children:
        case_node.add_child(child)
      sroot.slice_children(len(sroot.children), len(sroot.children))
      case_children.append(case_node)
    lex_copy = block[1]
  
  # Check if the default case exists.
  if is_end(lex_copy) or lex_copy[0][1] != "Keyword for the Default Case":
    return (False, "Missing OMGWTF in the Switch-Case statement", root)
  
  # Evaluate the code block inside
  # the default case.
  case_node = Node(sroot, root, lex_copy[0][0], lex_copy[0][1])
  block = evaluate_switch_code(lex_copy[2:], root, sroot)
  if not block[0]:
    return (False, block[1], root)
  
  # Add the children as nodes.
  for child in sroot.children:
    case_node.add_child(child)
    sroot.slice_children(len(sroot.children), len(sroot.children))
    case_children.append(case_node)
  lex_copy = block[1]
  
  # Check if the condition was ended properly.
  if is_end(lex_copy) or (len(lex_copy) > 0 and lex_copy[0][1] != "End of Conditional Statement"):
    return (False, "There is no delimiter for ending the condition", root)
  
  # Add the AST to the root.
  for child in case_children:
    sroot.add_child(child)
  root.add_child(sroot)
  lex = lex_copy[2:]
  return (True, lex, root)

"""
* loop
| grammar for for/while loops
"""
def loop(lex, root):
  # * Declaration
  lroot = Node(root, root, lex[0][0], lex[0][1])
  lex_copy = deepcopy(lex)[1:]
  loop_children = []
  
  # Check if an identifier was used as a loop delimiter.
  if is_end(lex_copy) or not variables.is_variable(lex_copy[0][1]):
    return (False, "Missing identifier for the loop", root)
  loop_children.append(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))
  
  # Check the operation for the loop.
  lex_copy = lex_copy[1:]
  if is_end(lex_copy) or (lex_copy[0][1] != "Loop Increment" and lex_copy[0][1] != "Loop Decrement"):
    return (False, "Invalid operation on the loop", root)
  loop_children.append(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))

  # Check the statement -- YR <identifier>.
  lex_copy = lex_copy[1:]
  if is_end(lex_copy) or lex_copy[0][1] != "Variable Assignment for Loop":
    return (False, "Missing YR keyword", root)
  loop_children.append(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))

  lex_copy = lex_copy[1:]
  if is_end(lex_copy) or not variables.is_variable(lex_copy[0][1]):
    return (False, "Missing identifier for the loop", root)
  loop_children.append(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))

  # Check for TIL/WILE.
  lex_copy = lex_copy[1:]
  if is_end(lex_copy) or lex_copy[0][1] != "Keyword for Loop Condition":
    return (False, "No TIL or WILE", root)
  loop_children.append(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))

  # Get the code block for the expression.
  lex_copy = lex_copy[1:]
  code_block = []
  index = 0
  
  while is_end(lex_copy) or lex_copy[0][1] != const.DASH:
    code_block.append(lex_copy[0])
    lex_copy = lex_copy[1:]
    index += 1
  code_block.append(lex_copy[0])
  lex_copy = lex_copy[1:]
  
  # Check if the expression is relational or comparison.
  if is_end(code_block) or (const.COMPARISON_OP not in code_block[0][1] and const.BOOLEAN_OP not in code_block[0][1]):
    return (False, "Missing boolean/comparison expression", root)
  result = evaluate_block(code_block, lroot, True)
  if not result[0]:
    return (False, result[1], root)
  
  # Move the node to temporary list.
  expr_node = Node(lroot, lroot, const.LOOP_EXPR, const.LOOP_EXPR)
  for child in lroot.children:
    expr_node.add_child(child)

  loop_children.append(expr_node)
  lroot.slice_children(len(lroot.children), len(lroot.children))
  
  # Check the validity of each statement.
  code_block = []
  while not is_end(lex_copy) and lex_copy[0][1] != "End of Loop":
    code_block.append(lex_copy[0])
    lex_copy = lex_copy[1:]
  
  # Add the code block to the loop.
  result = evaluate_block(code_block, lroot, True)
  if not result[0]:
    return (False, result[1], root)
  
  # Get the child nodes for each statement.
  code_node = Node(lroot, lroot, const.LOOP_CODEBLOCK, "Loop Code Block")
  for child in lroot.children:
    code_node.add_child(child)
  
  loop_children.append(code_node)
  lroot.slice_children(len(lroot.children), len(lroot.children))

  # Check for IM OUTTA YR.
  if is_end(lex_copy) or lex_copy[0][1] != "End of Loop":
    return (False, "Missing IM OUTTA YR in loop", root)
  loopend = Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1])
  lex_copy = lex_copy[1:]

  # Check for the label.
  if is_end(lex_copy) or not variables.is_variable(lex_copy[0][1]):
    return (False, "Missing identifier for the loop", root)
  loopend.add_child(Node(lroot, lroot, lex_copy[0][0], lex_copy[0][1]))
  loop_children.append(loopend)
  lex_copy = lex_copy[1:]
  
  if not is_end(lex_copy) and lex_copy[0][1] != const.DASH:
    return (False, "There is an extra block in the loop", root)

  # Add the children to the loop root.
  for child in loop_children:
    lroot.add_child(child)
  root.add_child(lroot)
  lex = lex_copy[1:]
  return (True, lex, root)

"""
* break_block()
| grammar for breaking loops
| and conditions
"""
def break_block(lex, root, is_gtfo):
  # Throw an exception if GTFO is outside
  # of conditionals and loops.
  if not is_gtfo:
    return (False, "No conditional or loop to break", root)
  root.add_child(Node(root, root, lex[0][0], lex[0][1]))

  # GTFO should only be the only one in a line.
  lex = lex[1:]
  if is_end(lex) or lex[0][1] != const.DASH:
    return (False, "There is an unidentified block in the program", root)
  lex = lex[1:]
  return (True, lex, root)

"""
* arithmetic()
* calls arithmvalue(), varident(), comparison(), relational(), arithmetic()
| grammar for arithmetic operation
"""
def operation(lex, root, operations, is_standalone):
    _lex = []
    for child in lex:
      if len(child) == 3:
        _lex.append(deepcopy(child))
      else:
        _lex.append(deepcopy(child))
        break
    
    #_lex= deepcopy(lex[:])
    _lex.reverse()
    stack= _lex[1:]
    index=0
    flag_value= True

    stack_cpy= stack[:]
    for s in range(len(stack_cpy)):
        if stack_cpy[s][1] in operations:
            if stack[index-1][1] == "VALID":
                pass
            elif stack[index-1][1] == varident():
                pass
            elif stack[index-1][1] not in literal():
                flag_value = False
            if stack[index-2][1] == f"{const.BOOLEAN_OP} (NOT operator)":
              if index == 1:
                stack[index] = ("-","VALID")
                stack.pop(index-1)
                index = index - 1
                break
                
                
              
            #check for the delimiter of the operation
            if stack[index-2][1] != "Delimiter for Nested Expressions":
                flag_value= False

            #second operand
            if stack[index-3][1] == "VALID":
                pass
            elif stack[index-3][1] == varident():
                pass
            elif stack[index-3][1] not in literal(): 
                flag_value= False
          
            if flag_value== True:
                stack[index] = ("-","VALID")
                stack.pop(index-1)
                stack.pop(index-2)
                stack.pop(index-3)
                index = index - 3 
            else:
                break
        index= index+1

    cnt=0
    for k in lex:
        if k[0] == 'Parser Delimiter':
            cnt=cnt+1
            break
        cnt= cnt+1
      
    # Create a node for the operation block.
    opnode = Node(root, root, const.OP_BLOCK, const.OP_BLOCK)
    
    # Add to the root if standalone statement.
    if is_standalone:
      for op in stack_cpy:
        opnode.add_child(op)
      root.add_child(opnode)
    
    return(flag_value, lex[cnt:], root, stack_cpy)

"""
* vardeclaration()
| grammar of varident
"""
def varident():
    return "Identifier"

"""
* literal()
| grammar of literal
"""
def literal():
    return ["NUMBR Literal", "NUMBAR Literal", "YARN Literal", "TROOF Literal"]

"""
* abstraction()
| checks if the lex exist in the grammar
"""
def abstraction(grammar, lex, root):
    # * Declaration
    result = False
    flag = True
    flag_literal = False
    index = 0
    node = None

    for k in grammar:
        if (len(lex)-1 >= len(k)):
            for i in k:
                if type(i) == list:
                    for e in i:
                        if e == lex[index][1]:
                            flag_literal = True
                    if flag_literal == False:
                        flag = False
                elif type(i) == tuple:
                    if flag == True:
                        if i[1] == "expression":
                            # len of remaining grammar to parser
                            rem_len= len(k) - (index+1)
                            if rem_len!=0:
                                _lex= lex[index:-(rem_len+1)]
                                _lex.append(('Parser Delimiter', '-'))
                            else:
                                _lex= lex[index:]
                            expr_len = len(_lex) - 1
                           
                            _expression = expression(_lex, root)
                            if _expression[0] == False:
                                flag = False
                            else:
                                index = (index + expr_len)-1
                else:
                    if i != lex[index][1]:
                        flag = False
                index = index+1
            if flag == True and lex[index][1] == const.DASH:
                # Slice the statement.
                index = 0
                lex_copy = deepcopy(lex)
                while not is_end(lex_copy) and lex_copy[0][1] != const.DASH:
                  index += 1
                  lex_copy = lex_copy[1:]

                # Translate into an AST.
                node = get_syntax_tree(lex[:index], root)
                root.add_child(node)

                # Set the other needed values.
                result = True
                lex = lex[index + 1:]
                break
            flag = True
            index = 0
    return (result, lex, root)

"""
* get_syntax_tree()
| Translate the grammar into a syntax tree.

* Parameters
| lex (list): The statement broken down into lexemes

* Returns
| Node: The main node (start of statement) and its children
"""
def get_syntax_tree(lex, root):
    # * Declaration
    node = None

    # * One-Liners
    # Translate one-lined statements.
    parent_name = lex[0][0]
    parent_type = lex[0][1]
    node = Node(root, root, parent_name, parent_type)

    # Add the children.
    for child in lex[1:]:
        node.add_child(Node(node, root, child[0], child[1]))
    return node
