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
    line_error=0 
    cnt = 0
    # iterate through the lex elements: finds the commment token and remove from lex
    for element in lex:
        # if TLDR is encountered first without OBTW key word: error
        if element[1] == "End of Multiline Comment" and flag_comment == False:
            line_error= element[2]
            return (False, "Invalid comments", line_error)
        # checks the index of the OBTW keyword
        if element[1] == 'Start of Multiline Comment':
            flag_comment = True
            line_error= element[2]
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
        _print= print_statement(lex, root)
        if _print[0] == True:
                lex= _print[1]
                return(True, lex)
        else:
                return (False, "Invalid printing", lex[0][2])

    # * Input
    if lex[0][1] == const.INPUT:
        _userinput= userinput(lex, root)
        if _userinput[0] == True:
                lex= _userinput[1]
                return(True, lex)
        else:
                return(False, "Invalid user input", lex[0][2])
    
    # * Variable Declaration
    if lex[0][1] == const.VAR_DECLARATION:
        _vardeclaration = vardeclaration(lex, root)
        if _vardeclaration[0] == True:
            lex = _vardeclaration[1]
            return (True, lex)
        else:
            return (False, "Invalid variable declaration", lex[0][2])

    # * Typecasting
    if lex[0][1] == const.TYPECAST[0] or lex[2][1] == const.TYPECAST[0] or lex[1][1] == const.TYPECAST[1]:
        _typecast = typecast(lex, root)
        if _typecast[0] == True:
            lex = _typecast[1]
            return (True, lex)
        else:
            return (False, "Invalid typecasting", lex[0][2])
    # * Assignment
    if lex[1][1] == const.ASSIGNMENT: 
        _assignment= assignment(lex, root)
        if _assignment[0]== True:
                lex= _assignment[1]
                return(True, lex)
        else:
                return(False, "Invalid assignment", lex[0][2])
    
    # * Concatenation
    if lex[0][1] == const.CONCAT:
        _concat= concat(lex, root)
        if _concat[0] == True:
            lex= _concat[1]
            return (True, lex)
        else:
            return (False, "Invalid Concatenation", lex[0][2])
    
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
    if (lex[0][1] == f"{const.ARITHMETIC_OP} (Addition)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Subtraction)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Multiplication)" or lex[0][1] == f"{const.ARITHMETIC_OP} (Division)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Modulo)" or lex[0][1]== f"{const.ARITHMETIC_OP} (Max)" \
        or lex[0][1] == f"{const.ARITHMETIC_OP} (Min)") and (type== const.ALL or type== const.ARITHMETIC):
        _arithmetic= arithmetic(lex, root)
        if _arithmetic[0] == True:
                lex= _arithmetic[1]
                return(True, lex)
        else:
                return(False, "Invalid arithmetic operation", lex[0][2])
    
    # * Comparison
    if (lex[0][1] == f"{const.COMPARISON_OP} (Not Equal)" or lex[0][1] == f"{const.COMPARISON_OP} (Equal)") \
        and (type== const.ALL or type== const.COMPARISON):
        _comparison= comparison(lex, root)
        if _comparison[0] == True:
            lex= _comparison[1]
            return(True, lex)
        else:
            return(False, "Invalid comparison", lex[0][2])


    else:
        return (False, "Syntax Error", lex[0][2])
    

"""
* print() 
* calls printable() , printrec(), varident(), literal()
| grammar for printing
"""
def print_statement(lex, root):
        _expression= (const.ALL,"expression")
        _print= [["Output", varident()],
                ["Output", literal()],
                ["Output", _expression],
                ["Output", varident(), "printrec"]]
        
        return abstraction(_print, lex, root)

def printrec():
        return [[printrec()], [varident()],[literal()]]

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
    _expression= (const.ALL,"expression")
    _assignment= [[varident(), "Variable Assignment", literal()],
            [varident(), "Variable Assignment", varident()],
            [varident(), "Variable Assignment", _expression]]

    return abstraction(_assignment, lex, root)

"""
* vardeclaration()
| grammar of variable declaration
"""
def vardeclaration(lex, root):
    _expression= (const.ALL,"expression")
    _vardeclaration = [
        ["Variable Declaration", varident(), "Variable Initialization",varident()],
        ["Variable Declaration", varident(), "Variable Initialization", literal()],
        ["Variable Declaration", varident()],
        ["Variable Declaration", varident(), "Variable Initialization", _expression],]

    return abstraction(_vardeclaration, lex, root)

"""
* concat()
| grammar for concatenation
"""
def concat(lex, root):
    index=0
    result= True
    for e in lex:
        if e[1] == const.DASH:
            last_ind= index
            if lex[last_ind -1][1] == 'Delimiter for Nested Expressions':
                result= False
            break
        if (index !=0) and (index%2==0):
            if e[1] != 'Delimiter for Nested Expressions':
                result= False
        else:
            if e[1] == 'Delimiter for Nested Expressions':
                result= False
        index= index+1

    # Translate into an AST.
    node = get_syntax_tree(lex[:index], root)
    root.add_child(node)

    lex = lex[index +1:]
    return(result, lex, root)

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
    return ["NUMBR Literal","NUMBAR Literal","TROOF Literal", varident() ,"comparison","relational", "arithmetic"]
  

"""
* comparison()
* calls compvalue(), relational()
| grammar for comparison
"""
def comparison(lex, root):
    _relational= ("comparison","relational")
    _arithmetic= (const.ARITHMETIC,"expression")
    _comparison= [[f"{const.COMPARISON_OP} (Equal)", compvalue(), "Delimiter for Nested Expressions", _relational],
                [f"{const.COMPARISON_OP} (Not Equal)", compvalue(), "Delimiter for Nested Expressions", _relational],
                [f"{const.COMPARISON_OP} (Equal)", "arithmetic", "Delimiter for Nested Expressions", _relational],
                [f"{const.COMPARISON_OP} (Not Equal)", "arithmetic", "Delimiter for Nested Expressions", _relational]]
    return abstraction(_comparison, lex, root)

def compvalue():
    return ["NUMBR Literal","NUMBAR Literal", varident()]

"""
* relational()
* calls compvalue(), arithmetic()
| grammar for comparison
"""
def relational(lex, root):
    _arithmetic= (const.ARITHMETIC,"expression")
    _relational= [[compvalue()],
                [f"{const.ARITHMETIC_OP} (Max)", compvalue(), "Delimiter for Nested Expressions", compvalue()],
                [f"{const.ARITHMETIC_OP} (Min)",compvalue(), "Delimiter for Nested Expressions", compvalue()],
                [f"{const.ARITHMETIC_OP} (Max)", "arithmetic", "Delimiter for Nested Expressions", "arithmetic"],
                [f"{const.ARITHMETIC_OP} (Min)", "arithmetic", "Delimiter for Nested Expressions", "arithmetic"],
                [f"{const.ARITHMETIC_OP} (Max)", compvalue(), "Delimiter for Nested Expressions", _arithmetic],
                [f"{const.ARITHMETIC_OP} (Min)", compvalue(), "Delimiter for Nested Expressions", _arithmetic],
                [f"{const.ARITHMETIC_OP} (Max)", "arithmetic", "Delimiter for Nested Expressions", compvalue()],
                [f"{const.ARITHMETIC_OP} (Min)", "arithmetic", "Delimiter for Nested Expressions", compvalue()],]
    
    _abstraction= abstraction(_relational, lex, root)
    if _abstraction[0] == True:
        lex= _abstraction[1]
        return(True, lex)
    else:
        return(False, lex)
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
                    if flag== True:
                        expr_len= len(lex[index:])
                        if i[1] == "expression":
                            exp_type= i[0]
                            _expression= expression(lex[index:], root, exp_type)
                            if _expression[0] == False:
                                flag= False
                            else:
                                lex_len = len(_expression[1])
                                upd_ind= expr_len-lex_len-2
                                index= index+ upd_ind
                        if i[1] == "relational":
                            _relational= relational(lex[index:], root)
                            if _relational[0] == False:
                                flag= False
                            else:
                                lex_len = len(_relational[1])
                                upd_ind= expr_len-lex_len-2
                                index= index+ upd_ind
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