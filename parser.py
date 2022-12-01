import lexer
import syntax_storage as grammar


def parse(lex):
    print(lex)
    program= grammar.program_start(lex)
    print(program[1])
    print(program[0])

    
if __name__ == "__main__":
    filename = "comments.lol"
    symbol_table = lexer.analyze(filename)

    lex=[]
    for k in symbol_table:
        for i in symbol_table[k]:
            lex.append(i[1])
        if symbol_table[k] != []:
            if symbol_table[k][0][0] != "KTHXBYE":
                lex.append("-")

    parse(lex)

        






