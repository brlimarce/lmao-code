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
                "userinput", "print", "printrec", "printable", "identifier", "literal"]

Rprint={
        "print": [["HO","printable"],["H1","printrec"]],
        "printrec": [["H2","printrect"],["literal"],["identifier"],["expression"]],
	"printable":[["literal"],["identifier"],["expression"]],
	"H0": [["output"]],
	"H1" : [["H4","H3"]],
	"H2": [["printable","H3"]],
	"H3": [["an"]],
	"H4": [["H0","H5"]],
	"H5": [["identifier"]]
}

Rstart={
        "program":[["A1","A0"]],
        "statement":[["codeblock","statement"],["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],["print"]],
        "codeblock":[["expression"],["loop"],["switch_case"],["ifthen"],["userinput"],["print"]],
        "A0": [["kthxbye"]],
        "A1": [["A2"],["statement"]],
        "A2": [["hai"]]
}

Rvardeclaration= {
        "vardeclaration": [["B0","B1"],["B3","B2"],["B3","B4"],["B3","B1"]],
        "B0":[["i has a"]],
        "B1":[["identifier"]],
        "B2":[["literal"]],
        "B3":[["B6"],["B5"]],
        "B4":[["expression"]],
        "B5": [["itz"]],
        "B6":[["B0"],["B1"]]
}

Rcomparison={
        "comparison":[["C0","relational"],["C1","relational"]],
        "compvalue":[["NUMBR"],["NUMBAR"],["identifier"],["arithmetic"]],
        "relational":[["C2","relational"],["C3","relational"],["NUMBR"],["NUMBAR"],["identifier"],["arithmetic"]],
        "C0":[["C5","C4"]],
        "C1":[["C6","C4"]],
        "C2":[["C7","C4"]],
        "C3":[["C8","C4"]],
        "C4":[["an"]],
        "C5":[["C9","compvalue"]],
        "C6":[["C10","compvalue"]],
        "C7":[["C11","compvalue"]],
        "C8":[["C12","compvalue"]],
        "C9":[["equal to"]],
        "C10":[["not equal to"]],
        "C11":[["maximize"]],
        "C12":[["minimize"]]
}

Rtypecasting={
        "typecasting":[["D0","datatype"],["D1","datatype"],["D2","datatype"],["D3","datatype"]],
        "datatype":[["type literal"]],
        "D0":[["D4","D5"]],
        "D1":[["D0","D6"]],
        "D2":[["D5","D7"]],
        "D3":[["D8","D5"]],
        "D4":[["maek"]],
        "D5":[["identifier"]],
        "D6":[["a"]],
        "D7":[["is now a"]],
        "D8":[["D9","D4"]],
        "D9":[["D5","D10"]],
        "D10":[["r"]]
}

Rconcat={
        "concatenation":[["E0","concat"]],
        "concat":[["E1","concatenation"],["literal"],["identifier"],["arithmetic"],["boolean"],["compare"],["typecast"]],
        "alltype":[["literal"],["identifier"],["arithmetic"],["boolean"],["compare"],["typecast"]],
        "E0":[["E3","E2"]],
        "E1":[["all type"],["E2"]],
        "E2":[["an"]],
        "E3":[["E4"],["alltype"]]
}

Rassignment={
        "assignment":[["F1","F0"],["F1","F2"],["F1","F3"]],
        "F1":[["F2","F4"]],
        "F0":[["literal"]],
        "F3":[["expression"]],
        "F2":[["identifier"]],
        "F4":[["r"]]
}

Rloop={
        "loop":[["G1","G0"],["G2","G0"],["G3","G0"]],
        "loop_expression":[["G4","G5"],["G6","G5"]],
        "G0":[["identifier"]],
        "G1":[["G8","G7"]],
        "G2":[["G10","G9"]],
        "G3":[["G11","G7"]],
        "G4":[["loop until"]],
        "G5":[["expression"]],
        "G6":[["loop while"]],
        "G7":[["loop end"]],
        "G8":[["G13","G12"]],
        "G9":[["loop end"]],
        "G10":[["G14","G12"]],
        "G11":[["G8","G15"]],
        "G12":[["statement"]],
        "G13":[["G14","loop_expression"]],
        "G14":[["G16","G0"]],
        "G15":[["loop break"]],
        "G16":[["G18","G17"]],
        "G17":[["loop var assign"]],
        "G18":[["G19","G0"]],
        "G19":[["loop start"]]
}

Rswitch={
        "switch_case":[["I1","I0"]],
        "case":[["I2","I0"],["I3","I0"]],
        "I0":[["oic"]],
        "I1":[["I4","case"]],
        "I2":[["I6","I5"]],
        "I3":[["I7","I5"]],
        "I4":[["start switch"]],
        "I5":[["codeblock"]],
        "I6":[["I8","I9"]],
        "I7":[["I10","I9"]],
        "I8":[["switch case"]],
        "I9":[["literal"]],
        "I10":[["switch default"]]
}

Rinput={
        "userinput":[["J0","J1"]],
        "J0":[["input"]],
        "J1":[["identifier"]]
}

Rifthen={
        "ifthen":[["K1","K0"],["K2","K0"]],
        "K0":[["oic"]],
        "K1":[["K4","K3"]],
        "K2":[["K5","K3"]],
        "K3":[["codeblock"]],
        "K4":[["K7","K6"]],
        "K5":[["K1","K8"]],
        "K6":[["if case"]],
        "K7":[["K9","K10"]],
        "K8":[["else case"]],
        "K9":[["expression"]],
        "K10":[["start if-else"]]
}