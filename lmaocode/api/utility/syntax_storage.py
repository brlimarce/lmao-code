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
            print("flag_comment is False")
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
        print("flag_comment is True")
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
    if lex[0] == const.TYPECAST[0] or lex[2] == const.TYPECAST[0] or lex[1] == const.TYPECAST[1]:
        _assignment = assignment(lex, root)
        if _assignment[0] == True:
            lex = _assignment[1]
            return (True, lex)
        else:
            return (False, "Error in typecasting", None)
    else:
        return (False, "Syntax Error", None)

"""
* assignment()
| grammar of assignment
"""
def assignment(lex, root):
    _assignment = [["Explicit Typecasting", varident(), datatype()],
                   ["Explicit Typecasting", varident(
                   ), "Delimiter for Typecasting", datatype()],
                   [varident(), "Delimiter for Typecasting", datatype()],
                   [varident(), "Variable Assignment", "Explicit Typecasting", varident(), datatype()]]

    return abstraction(_assignment, lex, root)

"""
* vardeclaration()
| grammar of variable declaration
"""
def vardeclaration(lex, root):
    _vardeclaration = [
        ["Variable Declaration", varident(), "Variable Initialization", "expression"],
        ["Variable Declaration", varident(), "Variable Initialization",
         varident()],
        ["Variable Declaration", varident(), "Variable Initialization", literal()],
        ["Variable Declaration", varident()]]

    return abstraction(_vardeclaration, lex, root)

"""
* datatype()
| grammar of data type
"""
def datatype():
    return "TYPE Literal"

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
  node.print_tree()

  # TODO: Add support for structured constructs.
  # e.g. conditional statements, loops

  return node