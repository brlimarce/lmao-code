from api.utility import syntax_storage as grammar
from api.utility.node import Node

"""
* parse()
| Apply parsing in the symbol table.

* Returns
| tuple: Contains a flag (success) and parse tree.
"""
def parse(lex):
    # * Declaration
    handle_comments = grammar.comments(lex)
    root_node = None # Root Node

    #error in comments
    if handle_comments[0] == False:
        # print error
        raise Exception(f"🚀 ~ Syntax Error on Line {handle_comments[2]}: {handle_comments[1]}.")

    # no error in comments: parse the program
    else:
        lex = handle_comments[1]
        if lex==[]: 
            return (True, None)
        program = grammar.program_start(lex)

        # error in program start
        if program[0] == False:
            # print the error
            raise Exception(f"🚀 ~ Syntax Error: {program[1]}.")
        # no error in program start: iterate through the statements
        else:
            # Add the root node.
            root_node = Node(None, None, "HAI", "Program Start")

            lex = program[1]
            if lex==[]: 
                return None
            statement = grammar.statement(lex, root_node)

            # error in the statement
            if (statement[0]) == False:
                # print the error
                raise Exception(f"🚀 ~ Syntax Error on Line {statement[2]}: {statement[1]}.")
            # no error: check if the lex is empty which means that the whole program is parsed
            else:
                # check the length of the lex list
                lex = statement[1]
                recursion = False

                # if not empty: perform recursion in statement function
                if len(lex) != 0:
                    recursion = True
                # loop while lex is not empty
                while (recursion):
                    mult_statement = grammar.statement(lex, root_node)

                    # error: print error; break the loop
                    if (mult_statement[0] == False):
                        raise Exception(f"🚀 ~ Syntax Error on Line {mult_statement[2]}: {mult_statement[1]}.")
                    else:
                        # no error: check for the len of lex; update the lex
                        # if lex is empty: parsing is done and successful; end the loop
                        # else empty: continue with the loop
                        lex = mult_statement[1]
                        if len(lex) == 0:
                            recursion = False
                            return (True, root_node)
                # else empty: parsing done and successful
                else:
                    return (True, root_node)

"""
* analyze()
| The main method to apply syntax
| analysis to the program.
"""
def analyze(result: tuple):
  try:
    # * Declaration
    lex = []
    symbol_table = result[1]

    # Merge each line separated by a dash.
    if result[0]:
      for k in symbol_table:
          for i in symbol_table[k]:
              i=i+(k,)
              lex.append(i)
          if symbol_table[k] != []:
              if symbol_table[k][0][0] != "KTHXBYE" and symbol_table[k][0][0] != "OBTW" and \
                      symbol_table[k][0][0] != "TLDR" and symbol_table[k][0][0] != "BTW":
                  lex.append(("Parser Delimiter", "-"))
    return parse(lex)
  except Exception as e:
    return (False, str(e))
