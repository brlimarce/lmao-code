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
                    ["identifier"],["comparison"],["relational"],["arithmetic"]],
    "vardeclaration": [["i has a", "identifier"],
                    ["i has a", "identifier", "itz", "literal"],
                    ["i has a", "identifier", "itz", "expression"],
                    ["i has a", "identifier", "itz", "identifier"]], 
    "boolean": [["bool and", "boolval", "an", "boolval"],
                ["bool or", "boolval", "an", "boolval"],
                ["bool xor", "boolval", "an", "boolval"],
                ["bool not", "boolval", "an", "boolval"],
                ["bool inf and", "boolval", "an", "allany"],
                ["bool inf or", "boolval", "an", "allany"]],
    "allany": [["boolnest", "an", "allany"],["boolval", "mkay"]],
    "boolval": [["literal"], ["identifier"], ["boolnest"], ["arithmetic"], ["comparison"]],
    "boolnest": [["bool and", "boolnest", "an", "boolval"],
                ["bool or", "boolnest", "an", "boolval"],
                ["bool xor", "boolnest", "an", "boolval"],
                ["bool not", "boolnest", "an", "boolval"]],
    "comparison": [["equal to", "compvalue", "an", "relational"],
                ["not equal to", "compvalue", "an", "relational"]],
    "compvalue": [["NUMBR"],["NUMBAR"],["identifier"],["arithmetic"]],
    "relational": [["maximize","compvalue", "an", "relational"],
                ["minimize","compvalue", "an", "relational"],
                ["compvalue"]],
    "typecasting":[["maek", "identifier", "datatype"],
                ["maek", "identifier", "a", "datatype"],
                ["identifier", "is now a", "datatype"],
                ["identifier", "r", "maek", "identifier", "datatype"]],
    "datatype": [["type literal"]],
    "concatenation": ["string concat", "alltype", "an", "concat"],
    "concat": [["alltype", "an", "concat"], ["alltype"]],
    "alltype": [["literal"], ["identifier"], ["arithmetic"],  ["boolean"], ["comparison"], ["typecasting"]],
    "assignment": [["identifier", "r", "literal"],
                ["identifier", "r", "identifier"],
                ["identifier", "r", "expression"]],
    "loop": [["loop start", "identifier", "loop var assign", "identifier", "loop_expression", "statement", "loop end", "identifier"],
            ["loop start", "identifier", "loop var assign", "identifier", "statement", "loop end", "identifier"],
            ["loop start", "identifier", "loop var assign", "identifier", "loop_expression", "statement", "loop break", "loop end", "identifier"]],
    "loop_expression": [["loop until", "expression"],["loop while", "expression"]],
    "switch_case":  ["start switch", "case", "oic"],
    "case":  [["switch case", "literal", "codeblock", "oic"],
            ["switch default", "literal", "codeblock", "oic"],
            ["switch default", "literal", "codeblock", "oic"]],
    "ifthen": [["expression", "start if-else", "if case", "codeblock", "oic"],
            ["expression", "start if-else", "if case", "codeblock", "else case", "codeblock" "oic"]],
    "userinput": [["input", "identifier"]],
    "print": [["output", "printable"],
            ["output", "identifier", "an", "printrec"]],
    "printrec":[["printable"],["printable", "an", "printrec"]],
    "printable": [["literal"],["identifier"],["expression"]],
    "identifier": [["identifier"]],
    "literal": [["NUMBR"],["NUMBAR"],["YARN"],["TROOF"]]
}

#  BTW variable declaration
#   I HAS A thing
#   I HAS A thing1 ITZ 3
#   BTW typecasting
#   var IS NOW A NUMBAR
#   BTW assignement
#   var1 R 5
#   var2 R num
#   BTW arithmetic
#   SUM OF 3 AN 5
#   DIFF OF 4 AN 3.14 
#   BTW printing
#   VISIBLE num
#   VISIBLE 4.6
#   BTW user input
#   GIMMEH var 
#   SMOOSH var AN 12 AN 15 AN "yes" AN AAA 

# I HAS A thing ITZ SUM OF 2 AN 5
#  I HAS A thing ITZ BOTH SAEM 5 AN 2
#  var1 R DIFF OF 2 AN 5
#  VISIBLE BIGGR OF 5 AN "9"
#  BOTH SAEM 5 AN 2
#  BOTH SAEM var AN BIGGR OF num AN SUM OF 2 AN 5