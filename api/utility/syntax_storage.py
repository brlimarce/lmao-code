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
def codeblock(lex, root):
    # statement= [["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],
    # ["vardeclaration"],["print"],["typecasting"],["concatenation"],["assignment"]]
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
    if lex[0][1] == const.TYPECAST[0] or lex[1][1] == const.TYPECAST[1] or (len(lex) > 2 and lex[2][1] == const.TYPECAST[0]):
        _typecast = typecast(lex, root)
        if _typecast[0] == True:
            lex = _typecast[1]
            return (True, lex)
        else:
            return (False, "Invalid typecasting", lex[0][2])
   
    # * Assignment
    if lex[1][1] == const.ASSIGNMENT:
        _assignment = assignment(lex, root)
        if _assignment[0] == True:
            lex = _assignment[1]
            return (True, lex)
        else:
            return (False, "Invalid assignment", lex[0][2])
    
    # * Concatenation
    if lex[0][1] == const.CONCAT:
        _concat = concat(lex, root)
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
    
    # * Expression
    else:
        _expression = expression(lex, root, const.ALL)
        return _expression

"""
* expression()
| grammar of expression
"""
def expression(lex, root, type):
    # expression [["arithmetic"], ["boolean"], ['comparison']]

    # Break if there are no more lexemes.
    if lex == []:
        return (True, lex)

    # * Arithmetic
    if (lex[0][1] == f"{const.ARITHMETIC_OP} (Addition)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Subtraction)"
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Multiplication)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Division)"
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Modulo)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Max)"
            or lex[0][1] == f"{const.ARITHMETIC_OP} (Min)") and (type == const.ALL or type == const.ARITHMETIC):
        _arithmetic = arithmetic(lex, root)
        if _arithmetic[0] == True:
            lex = _arithmetic[1]
            return (True, lex)
        else:
          return (False, "Invalid arithmetic operation", lex[0][2])

    # * Comparison
    if (lex[0][1] == f"{const.COMPARISON_OP} (Not Equal)" or lex[0][1] == f"{const.COMPARISON_OP} (Equal)") \
            and (type == const.ALL or type == const.COMPARISON):
        _comparison = comparison(lex, root)
        if _comparison[0] == True:
            lex = _comparison[1]
            return (True, lex)
        else:
            return (False, "Invalid comparison", lex[0][2])

    else:
        return (False, "Syntax Error", lex[0][2])


"""
* print() 
* calls printable() , printrec(), varident(), literal()
| grammar for printing
"""
def print_statement(lex, root):
    _expression = (const.ALL, "expression")
    _print = [["Output", varident()],
              ["Output", literal()],
              ["Output", _expression],
              ["Output", varident(), "printrec"]]
    return abstraction(_print, lex, root)

def printrec():
    return [[printrec()], [varident()], [literal()]]

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
    _expression = (const.ALL, "expression")
    _assignment = [[varident(), "Variable Assignment", literal()],
                   [varident(), "Variable Assignment", varident()],
                   [varident(), "Variable Assignment", _expression]]

    return abstraction(_assignment, lex, root)


"""
* vardeclaration()
| grammar of variable declaration
"""
def vardeclaration(lex, root):
    _expression = (const.ALL, "expression")
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
def concat(lex, root):
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

    # Translate into an AST.
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
  if len(lex_copy) > 0 and lex_copy[0][1] == "Keyword for the ELSE Case":
    else_node = Node(croot, root, lex_copy[0][0], lex_copy[0][1])
    block = evaluate_code(lex_copy, root, croot)
    if not block[0]:
      return (False, block[1], root)

    for child in croot.children:
      else_node.add_child(child)
    croot.slice_children(len(croot.children), len(croot.children))
    
    croot.add_child(ifnode)
    croot.add_child(else_node)
    lex_copy = block[1]
  
  # Check if there is an OIC.
  if is_end(lex_copy) or (len(lex_copy) > 0 and lex_copy[0][1] != "End of Conditional Statement"):
    return (False, "There is no delimiter for ending the condition", root)
  
  # Add the AST to the root.
  root.add_child(croot)
  lex = lex_copy[2:]
  
  return (True, lex, root)

# A helper function for conditionals to evaluate
# the entire code block.
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
  result = evaluate_block(block, croot)
  if not result[0]:
    return (result[0], result[1], root)
  return (True, lex_copy[index:], croot)

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
  lex = []
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
  result = evaluate_block(code_block, lroot)
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
  result = evaluate_block(code_block, lroot)
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

  # Add the children to the loop root.
  for child in loop_children:
    lroot.add_child(child)
  lroot.print_tree()
  return (True, lex, root)

"""
* arithmetic()
* calls arithmvalue(), varident(), comparison(), relational(), arithmetic()
| grammar for arithmetic operation
"""
def arithmetic(lex, root):
    _arithmetic = [[f"{const.ARITHMETIC_OP} (Addition)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Subtraction)", arithmvalue(
                   ), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Multiplication)", arithmvalue(
                   ), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Division)", arithmvalue(
                   ), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Modulo)", arithmvalue(
                   ), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Max)", arithmvalue(
                   ), "Delimiter for Nested Expressions", arithmvalue()],
                   [f"{const.ARITHMETIC_OP} (Min)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()]]

    return abstraction(_arithmetic, lex, root)

def arithmvalue():
    return ["NUMBR Literal", "NUMBAR Literal", "TROOF Literal", varident(), "comparison", "relational", "arithmetic"]

"""
* comparison()
* calls compvalue(), relational()
| grammar for comparison
"""
def comparison(lex, root):
    _relational = ("comparison", "relational")
    _arithmetic = (const.ARITHMETIC, "expression")
    _comparison = [[f"{const.COMPARISON_OP} (Equal)", compvalue(), "Delimiter for Nested Expressions", _relational],
                   [f"{const.COMPARISON_OP} (Not Equal)", compvalue(
                   ), "Delimiter for Nested Expressions", _relational],
                   [f"{const.COMPARISON_OP} (Equal)", "arithmetic",
                    "Delimiter for Nested Expressions", _relational],
                   [f"{const.COMPARISON_OP} (Not Equal)", "arithmetic", "Delimiter for Nested Expressions", _relational]]
    return abstraction(_comparison, lex, root)

def compvalue():
    return ["NUMBR Literal", "NUMBAR Literal", varident()]

"""
* relational()
* calls compvalue(), arithmetic()
| grammar for comparison
"""
def relational(lex, root):
    _arithmetic = (const.ARITHMETIC, "expression")
    _relational = [[compvalue()],
                   [f"{const.ARITHMETIC_OP} (Max)", compvalue(
                   ), "Delimiter for Nested Expressions", compvalue()],
                   [f"{const.ARITHMETIC_OP} (Min)", compvalue(
                   ), "Delimiter for Nested Expressions", compvalue()],
                   [f"{const.ARITHMETIC_OP} (Max)", "arithmetic",
                    "Delimiter for Nested Expressions", "arithmetic"],
                   [f"{const.ARITHMETIC_OP} (Min)", "arithmetic",
                    "Delimiter for Nested Expressions", "arithmetic"],
                   [f"{const.ARITHMETIC_OP} (Max)", compvalue(
                   ), "Delimiter for Nested Expressions", _arithmetic],
                   [f"{const.ARITHMETIC_OP} (Min)", compvalue(
                   ), "Delimiter for Nested Expressions", _arithmetic],
                   [f"{const.ARITHMETIC_OP} (Max)", "arithmetic",
                    "Delimiter for Nested Expressions", compvalue()],
                   [f"{const.ARITHMETIC_OP} (Min)", "arithmetic", "Delimiter for Nested Expressions", compvalue()], ]

    _abstraction = abstraction(_relational, lex, root)
    if _abstraction[0] == True:
        lex = _abstraction[1]
        return (True, lex)
    else:
        return (False, lex)

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
                        expr_len = len(lex[index:])
                        if i[1] == "expression":
                            exp_type = i[0]
                            _expression = expression(
                                lex[index:], root, exp_type)
                            if _expression[0] == False:
                                flag = False
                            else:
                                lex_len = len(_expression[1])
                                upd_ind = expr_len-lex_len-2
                                index = index + upd_ind
                        if i[1] == "relational":
                            _relational = relational(lex[index:], root)
                            if _relational[0] == False:
                                flag = False
                            else:
                                lex_len = len(_relational[1])
                                upd_ind = expr_len-lex_len-2
                                index = index + upd_ind
                else:
                    if i != lex[index][1]:
                        flag = False
                index = index+1
            if flag == True and lex[index][1] == const.DASH:
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
