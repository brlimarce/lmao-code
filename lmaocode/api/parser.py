from api.utility import syntax_storage as syntax
from api.utility import constants as const

def cykParse(lex, R):
    n = len(lex)

    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
 
    # Filling in the table
    for j in range(0, n):
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:   
                # If a terminal is found
                if len(rhs) == 1 and \
                rhs[0] == lex[j]:
                    T[j][j].add(lhs)
        for i in range(j, -1, -1):  
        #     # Iterate over the range i to j + 1  
            for k in range(i, j + 1):    
        #         # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        # If a terminal is found
                        if(k==(n-1)):
                            if len(rhs) == 2 and \
                            rhs[0] in T[i][k] and \
                            rhs[1] in T[k][j]:
                                T[i][j].add(lhs)
                        else:
                            if len(rhs) == 2 and \
                            rhs[0] in T[i][k] and \
                            rhs[1] in T[k+1][j]:
                                T[i][j].add(lhs)      

    # If word can be formed by rules
    # of given grammar
    if len(T[0][n-1]) != 0:
        return (True, T)
    else:
        return (False, T)

def merge(row: list) -> list:
  lex = []
  for i in row:
    lex.append(i[1])
  return lex

def parse(symbol_table) -> tuple:
    # Define the rules.
    rules = [syntax.Rprint, syntax.Rvardeclaration, syntax.Rcomparison, syntax.Rtypecasting, syntax.Rconcat, syntax.Rassignment, syntax.Rloop, syntax.Rswitch, syntax.Rinput, syntax.Rifthen]
    terminal = syntax.terminal
    non_terminal = syntax.non_terminal
    line_count = 0

    # Concatenate lexemes in table.
    try:
      for k in symbol_table:
        line_count = k
        lex = merge(symbol_table[k])
        if lex == '': # Comments
          continue

        if k == 1 or k == len(symbol_table):
          # Check for HAI and KTHXBYE.
          if k == 1 and (len(lex) != 1 or lex[0] != "hai"):
            return (False, f"~ {const.SYNTAX_ERROR} at Line {k}: No HAI keyword")
          if k == len(symbol_table) and (len(lex) != 1 or lex[0] != "kthxbye"):
            return (False, f"~ {const.SYNTAX_ERROR} at Line {k}: No KTHXBYE keyword")
        else:
          for rule in rules:
            res = cykParse(lex, rule)
            if res[0] == True:
              break
      payload = None if res[0] == True else f"~ {const.SYNTAX_ERROR} at Line {line_count}"
      return (res[0], payload)
    except Exception as e:
      return (False, f'"~ Error at Line {line_count}: {e}')