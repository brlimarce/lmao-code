from utility import constants as const
from utility.node import Node

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
    cnt = 0
    # iterate through the lex elements: finds the commment token and remove from lex
    for element in lex:
        # if TLDR is encountered first without OBTW key word: error
        if element[1] == "End of Multiline Comment" and flag_comment == False:
            return (False, "Error in comments")
        # checks the index of the OBTW keyword
        if element[1] == 'Start of Multiline Comment':
            flag_comment = True
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
        return (False, "Error in comments")
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
    # statement= [["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],["print"]]
    _codeblock = codeblock(lex, root)
    return _codeblock

"""
* codeblock()
| grammar of codeblock
"""
def codeblock(lex, root):
    if lex[0][1] == const.PRINT:
        _print= print_statement(lex, root)
        if _print[0] == True:
                lex= _print[1]
                return(True, lex)
        else:
                return (False, "Error in printing", None)
    if lex[0][1] == const.INPUT:
        _userinput= userinput(lex, root)
        if _userinput[0] == True:
                lex= _userinput[1]
                return(True, lex)
        else:
                return(False, "Error in user input", None)
    else:
        _expression = expression(lex, root)
        return _expression

"""
* expression()
| grammar of expression
"""
def expression(lex, root):
    # expression [["arithmetic"], ["vardeclaration"], ["boolean"], ['comparison'], ["typecasting"],["concatenation"],["assignment"]]

    # Break if there are no more lexemes.
    if lex == []:
      return (True, lex)
    

    # * Variable Declaration
    if lex[0][1] == const.VAR_DECLARATION:
        _vardeclaration = vardeclaration(lex, root)
        if _vardeclaration[0] == True:
            lex = _vardeclaration[1]
            return (True, lex)
        else:
            return (False, "Error in variable declaration", None)

    # * Typecasting
    if lex[0][1] == const.TYPECAST[0] or lex[2][1] == const.TYPECAST[0] or lex[1][1] == const.TYPECAST[1]:
        _typecast = typecast(lex, root)
        if _typecast[0] == True:
            lex = _typecast[1]
            return (True, lex)
        else:
            return (False, "Error in typecasting", None)
    
    if lex[1][1] == const.ASSIGNMENT: 
        _assignment= assignment(lex, root)
        if _assignment[0]== True:
                lex= _assignment[1]
                return(True, lex)
        else:
                return(False, "Error in assignment", None)
    
    if lex[0][1] == f"{const.ARITHMETIC_OP} (Addition)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Subtraction)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Multiplication)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Division)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Modulo)" or lex[0][1]== f"{const.ARITHMETIC_OP} (Max)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Min)" :
        _arithmetic= arithmetic(lex, root)
        if _arithmetic[0] == True:
                lex= _arithmetic[1]
                return(True, lex)
        else:
                return(False, "Error in arithmetic", None)

    else:
        return (False, "Syntax Error", None)
    

"""
* print() 
* calls printable() , printrec(), varident(), literal()
| grammar for printing
"""
def print_statement(lex, root):
        _print= [["Output", varident()],
                ["Output", literal()],
                ["Output", "expression"],
                ["Output", varident(), "printrec"]]
        return abstraction(_print, lex, root)

def printrec():
        return [[varident(), printrec()], varident()]

"""
* userinput()
* calls varident()
| grammar for getting input from user
"""
def userinput(lex, root):
        _userinput= [["Input", varident()]]

        return abstraction(_userinput, lex, root)

"""
* assignment()
| grammar of assignment
"""
def typecast(lex, root):
    _typecast = [["Explicit Typecasting", varident(), datatype()],
                   ["Explicit Typecasting", varident(), "Delimiter for Typecasting", datatype()],
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
    _assignment= [[varident(), "Variable Assignment", literal()],
            [varident(), "Variable Assignment", varident()],
            [varident(), "Variable Assignment", "expression"]]

    return abstraction(_assignment, lex, root)

"""
* vardeclaration()
| grammar of variable declaration
"""
def vardeclaration(lex, root):
    _vardeclaration = [
        ["Variable Declaration", varident(), "Variable Initialization", "expression"],
        ["Variable Declaration", varident(), "Variable Initialization",varident()],
        ["Variable Declaration", varident(), "Variable Initialization", literal()],
        ["Variable Declaration", varident()]]

    return abstraction(_vardeclaration, lex, root)

"""
* arithmetic()
* calls arithmvalue(), varident(), comparison(), relational(), arithmetic()
| grammar for arithmetic operation
"""
def arithmetic(lex, root):
        _arithmetic=[[f"{const.ARITHMETIC_OP} (Addition)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Subtraction)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Multiplication)", arithmvalue(), "Delimiter for Nested Expressions",arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Division)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Modulo)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Max)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()],
                [f"{const.ARITHMETIC_OP} (Min)", arithmvalue(), "Delimiter for Nested Expressions", arithmvalue()]] 
        
        return abstraction(_arithmetic, lex, root)

def arithmvalue():
        return ["NUMBR Literal","NUMBAR Literal","TROOF Literal", varident(),"comparison","relational","arithmetic"]

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

  # TODO: Add support for structured constructs.
  # e.g. conditional statements, loops

  return node