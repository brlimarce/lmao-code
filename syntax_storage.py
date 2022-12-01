R= {
    "program": [["hai", "statement", "kthxbye"]],
    "statement": [["codeblock", "statement"],["codeblock"]],
    "codeblock": [["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],["print"]],
    "expression": [["arithmetic"], ["vardeclaration"], ["boolean"], ['comparison'], ["typecasting"],["concatenation"],["assignment"]],
    "arithmetic":[["add", "arithmvalue", "an", "arithmvalue"],
                ["subtract", "arithmvalue", "an", "arithmvalue"],
                ["multiply", "arithmvalue", "an", "arithmvalue"],
                ["divide", "arithmvalue", "an", "arithmvalue"],
                ["modulo", "arithmvalue", "an", "arithmvalue"],
                ["maximize", "arithmvalue", "an", "arithmvalue"],
                ["minimize", "arithmvalue", "an", "arithmvalue"]],
    "arithmvalue": [["NUMBR"],["NUMBAR"],["TROOF"],
                    ["varident"],["comparison"],["relational"],["arithmetic"]],
    "vardeclaration": [["i has a", "varident"],
                    ["i has a", "varident", "itz", "literal"],
                    ["i has a", "varident", "itz", "expression"],
                    ["i has a", "varident", "itz", "varident"]], 
    "boolean": [["bool and", "boolval", "an", "boolval"],
                ["bool or", "boolval", "an", "boolval"],
                ["bool xor", "boolval", "an", "boolval"],
                ["bool not", "boolval", "an", "boolval"],
                ["bool inf and", "boolval", "an", "allany"],
                ["bool inf or", "boolval", "an", "allany"]],
    "allany": [["boolnest", "an", "allany"],["boolval", "mkay"]],
    "boolval": [["literal"], ["varident"], ["boolnest"], ["arithmetic"], ["comparison"]],
    "boolnest": [["bool and", "boolnest", "an", "boolval"],
                ["bool or", "boolnest", "an", "boolval"],
                ["bool xor", "boolnest", "an", "boolval"],
                ["bool not", "boolnest", "an", "boolval"]],
    "comparison": [["equal to", "compvalue", "an", "relational"],
                ["not equal to", "compvalue", "an", "relational"]],
    "compvalue": [["NUMBR"],["NUMBAR"],["varident"],["arithmetic"]],
    "relational": [["maximize","compvalue", "an", "relational"],
                ["minimize","compvalue", "an", "relational"],
                ["compvalue"]],
    "typecasting":[["maek", "varident", "datatype"],
                ["maek", "varident", "a", "datatype"],
                ["varident", "is now a", "datatype"],
                ["varident", "r", "maek", "varident", "datatype"]],
    "datatype": [["type literal"]],
    "concatenation": ["string concat", "alltype", "an", "concat"],
    "concat": [["alltype", "an", "concat"], ["alltype"]],
    "alltype": [["literal"], ["varident"], ["arithmetic"],  ["boolean"], ["comparison"], ["typecasting"]],
    "assignment": [["varident", "r", "literal"],
                ["varident", "r", "varident"],
                ["varident", "r", "expression"]],
    "loop": [["loop start", "varident", "loop var assign", "varident", "loop_expression", "statement", "loop end", "varident"],
            ["loop start", "varident", "loop var assign", "varident", "statement", "loop end", "varident"],
            ["loop start", "varident", "loop var assign", "varident", "loop_expression", "statement", "loop break", "loop end", "varident"]],
    "loop_expression": [["loop until", "expression"],["loop while", "expression"]],
    "switch_case":  ["start switch", "case", "oic"],
    "case":  [["switch case", "literal", "codeblock", "oic"],
            ["switch default", "literal", "codeblock", "oic"],
            ["switch default", "literal", "codeblock", "oic"]],
    "ifthen": [["expression", "start if-else", "if case", "codeblock", "oic"],
            ["expression", "start if-else", "if case", "codeblock", "else case", "codeblock" "oic"]],
    "userinput": [["input", "varident"]],
    "print": [["output", "printable"],
            ["output", "varident", "an", "printrec"]],
    "printrec":[["printable"],["printable", "an", "printrec"]],
    "printable": [["literal"],["varident"],["expression"]],
    "varident": [["identifier"]],
    "literal": [["NUMBR"],["NUMBAR"],["YARN"],["TROOF"]]
}

terminal=["hai", "kthxbye", "add", "an", "subtract", "divide", "modulo", "maximize",
            "minimize", "NUMBR", "NUMBAR", "TROOF", "i has a", "itz", "bool and", "bool or",
            "bool xor", "bool not", "bool inf and", "bool inf or", "mkay", "equal to", "not equal to",
            "maek", "a", "is now a", "r", "type literal", "string concat", "loop start", "loop var assign",
            "loop end", "loop break", "loop until", "loop while", "start switch", "oic", "switch case", 
            "switch default", "start if-else", "if case", "else case", "input", "output", "identifier",
            "NUMBR", "NUMBAR", "YARN", "TROOF"]

non_terminal=["program", "statement", "codeblock", "expression", "arithmetic", "arithmvalue", 
                "vardeclaration", "boolean", "allany", "boolval", "boolnest", "comparison",
                "compvalue", "relational", "typecasting", "datatype", "concatenation", "concat", 
                "alltype", "assignment", "loop", "loop_expression", "switch_case", "case", "ifthen", 
                "userinput", "print", "printrec", "printable", "varident", "literal"]

VAR_DECLARATION= "i has a"
TYPECAST= ["maek", "is now a"]

def program_start(lex):
        program= ["hai", "statement", "kthxbye"]

        if lex[0] != program[0]:
                return ("No HAI keyword", False)
        elif lex[-1] != program[-1]:
                return ("No KTHXBYE keyword", False)
        else:
                lex= lex[2:-1]
                if len(lex) != 0:
                        _statement= statement(lex)
                        return _statement
                else:
                        return ("Pased successfully", True)

def statement(lex):
        # statement= [["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],["print"]]
        _codeblock= codeblock(lex)
        return _codeblock

def codeblock(lex):
        _expression= expression(lex)
        return _expression

def expression(lex):
        # expression [["arithmetic"], ["vardeclaration"], ["boolean"], ['comparison'], ["typecasting"],["concatenation"],["assignment"]]

        if lex[0]== VAR_DECLARATION:
                _vardeclaration= vardeclaration(lex)
                if _vardeclaration[1]== True:
                        lex= _vardeclaration[0]
                        if len(lex) != 0:
                                statement(lex)
                        else:
                                print("Parsed Successfuly")
                                return("Parsed Successfuly", True)
                else:
                        print("Error in variable declaration")
                        return("Error in variable declaration", False)

        if lex[0] == TYPECAST[0] or lex[2] == TYPECAST[0] or lex[1] == TYPECAST[1]:
                _assignment= assignment(lex)
                if _assignment[1] == True:
                        lex= _assignment[0]
                        if len(lex) != 0:
                                statement(lex)
                        else:
                                return ("Parsed Successfuly", True)
                else:
                        return ("Error in typecasting", False)

def assignment(lex):
        _assignment= [["maek", varident(), literal()],
                ["maek", varident(), "a", literal()],
                [varident(), "is now a", varident()],
                [varident(), "r", "maek", varident(), literal()]]

        return abstraction(_assignment, lex)
        


def vardeclaration(lex):
        _vardeclaration= [
                ["i has a", varident(), "itz", "expression"],
                ["i has a", varident(), "itz", varident()],
                ["i has a", varident(), "itz", literal()],
                ["i has a", varident()]]
        
        return abstraction(_vardeclaration, lex)
        

def varident():
        return "identifier"

def literal():
        return ["NUMBR","NUMBAR","YARN","TROOF"]
        


def abstraction(grammar, lex):
        result= False
        flag= True
        flag_literal= False
        index=0
        for k in grammar:
                for i in k:
                        if type(i)== list:
                                for e in i:
                                        if e == lex[index]:
                                                flag_literal= True
                                if flag_literal== False:
                                        flag= False
                        else:  
                                if i != lex[index]:
                                        flag= False
                        index= index+1
                if flag== True and lex[index]== "-":
                        result= True
                        lex= lex[index+1:]
                        break
                flag= True
                index=0
        return(lex, result)

        
