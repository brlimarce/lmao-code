HAI
    BTW variable dec
    I HAS A x
    I HAS A y
    
    GIMMEH x
    GIMMEH y

    I HAS A sum ITZ SUM OF x AN y
    I HAS A diff ITZ DIFF OF x AN y
    I HAS A prod ITZ PRODUKT OF x AN y
    I HAS A quo ITZ QUOSHUNT OF x AN y
    I HAS A mod ITZ MOD OF x AN y

    VISIBLE x "+" y " = " sum
    VISIBLE x "-" y " = " diff
    VISIBLE x "*" y " = " prod
    VISIBLE x "/" y " = " quo
    VISIBLE x "%" y " = " mod

    BTW VISIBLE x "+" y " = " SUM OF x AN y
    BTW VISIBLE x "-" y " = " DIFF OF x AN y
    BTW VISIBLE x "*" y " = " PRODUKT OF x AN y
    BTW VISIBLE x "/" y " = " QUOSHUNT OF x AN y
    BTW VISIBLE x "%" y " = " MOD OF x AN y

    I HAS A max ITZ BIGGR OF x AN y
    I HAS A min ITZ SMALLR OF x AN y

    VISIBLE "max(" x "," y ") = " max
    VISIBLE "min(" x "," y ") = " min

    BTW VISIBLE "max(" x "," y ") = " BIGGR OF x AN y
    BTW VISIBLE "min(" x "," y ") = " SMALLR OF x AN y
    
    BTW x^2 + y^2
    I HAS A expr ITZ SUM OF PRODUKT OF x AN x AN PRODUKT OF y AN y
    VISIBLE expr
    BTW VISIBLE SUM OF PRODUKT OF x AN x AN PRODUKT OF y AN y
    BTW (x+y)^2
    expr R PRODUKT OF SUM OF x AN y AN SUM OF x AN y
    VISIBLE expr
    BTW VISIBLE PRODUKT OF SUM OF x AN y AN SUM OF x AN y
    BTW max(x,y) - min(x,y)
    expr R DIFF OF BIGGR OF x AN y AN SMALLR OF x AN y
    VISIBLE expr
    BTW VISIBLE DIFF OF BIGGR OF x AN y AN SMALLR OF x AN y

    BTW x + y/x + 0
    expr R SUM OF x AN SUM OF QUOSHUNT OF y AN x AN FAIL
    VISIBLE expr
    BTW VISIBLE SUM OF x AN SUM OF QUOSHUNT OF y AN x AN FAIL

    expr R SUM OF x AN SUM OF QUOSHUNT OF "17" AN x AN FAIL
    VISIBLE expr
    BTW VISIBLE SUM OF x AN SUM OF QUOSHUNT OF "17" AN x AN FAIL
KTHXBYE
