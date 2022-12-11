from api.utility import constants as const
import re

"""
* Token Regex
| A list of tuples that are utilized for
| different analyzers.

* Properties
| A. Regex of the construct
| B. Name of the grammar it belongs to; and
| C. Descriptor in the symbol table
"""

token_regex = [
  (re.compile(r"^HAI\b"), "hai", "Program Start"),
  (re.compile(r"^KTHXBYE\b"), "kthxbye", "Program End"),
  (re.compile(r"\bBTW\b"), "btw", const.BTW_KEYWORD),
  (re.compile(r"\bOBTW\b"), "obtw", const.OBTW_KEYWORD),
  (re.compile(r"\bTLDR\b"), "tldr", const.TLDR_KEYWORD),
  (re.compile(r"\bITZ\b"), "itz", "Variable Initialization"),
  (re.compile(r"^\bR\b"), "r", "Variable Assignment"),
  (re.compile(r"\bNOT\b"), "bool not", f"{const.BOOLEAN_OP} (NOT operator)"),
  (re.compile(r"\bDIFFRINT\b"), "not equal to", f"{const.COMPARISON_OP} (Not Equal)"),
  (re.compile(r"\bSMOOSH\b"), "string concat", "String Concatenation"),
  (re.compile(r"\bMKAY\b"), "mkay", f"Delimiter for {const.COMPARISON_OP}"),
  (re.compile(r"\bMAEK\b"), "maek", "Explicit Typecasting"),
  (re.compile(r"^VISIBLE\b"), "output", "Output"),
  (re.compile(r"\bGIMMEH\b"), "input", "Input"),
  (re.compile(r"^OIC\b"), "oic", "End of Conditional Statement"),
  (re.compile(r"^WTF\?\B"), "start switch", "Start of SWITCH Case Statement"),
  (re.compile(r"\bOMG\b"), "switch case", "Keyword for the SWITCH Case"),
  (re.compile(r"\bOMGWTF\b"), "switch default", "Keyword for the Default Case"),
  (re.compile(r"\bUPPIN\b"), "loop inc", "Loop Increment"),
  (re.compile(r"\bNERFIN\b"), "loop dec", "Loop Decrement"),
  (re.compile(r"^YR\b"), "loop var assign", "Variable Assignment for Loop"),
  (re.compile(r"\bTIL\b"), "loop until", "Keyword for Loop Condition"),
  (re.compile(r"\bWILE\b"), "loop while", "Keyword for Loop Condition"),
  (re.compile(r"\bGTFO\b"), "loop break", "Loop Break"),
  (re.compile(r"^I HAS A\b"), "i has a", "Variable Declaration"),
  (re.compile(r"\bSUM OF\b"), "add", f"{const.ARITHMETIC_OP} (Addition)"),
  (re.compile(r"^\bDIFF OF\b"), "subtract", f"{const.ARITHMETIC_OP} (Subtraction)"),
  (re.compile(r"\bPRODUKT OF\b"), "multiply", f"{const.ARITHMETIC_OP} (Multiplication)"),
  (re.compile(r"\bQUOSHUNT OF\b"), "divide", f"{const.ARITHMETIC_OP} (Division)"),
  (re.compile(r"\bMOD OF\b"), "modulo", f"{const.ARITHMETIC_OP} (Modulo)"),
  (re.compile(r"\bBIGGR OF\b"), "maximize", f"{const.ARITHMETIC_OP} (Max)"),
  (re.compile(r"\bSMALLR OF\b"), "minimize", f"{const.ARITHMETIC_OP} (Min)"),
  (re.compile(r"\bBOTH OF\b"), "bool and", f"{const.BOOLEAN_OP} (AND operator)"),
  (re.compile(r"\bEITHER OF\b"), "bool or", f"{const.BOOLEAN_OP} (OR operator)"),
  (re.compile(r"\bWON OF\b"), "bool xor", f"{const.BOOLEAN_OP} (XOR operator)"),
  (re.compile(r"\bALL OF\b"), "bool inf and", f"{const.BOOLEAN_OP} (AND with Infinite Arity)"),
  (re.compile(r"\bANY OF\b"), "bool inf or", f"{const.BOOLEAN_OP} (OR with Infinite Arity)"),
  (re.compile(r"\bBOTH SAEM\b"), "equal to", f"{const.COMPARISON_OP} (Equal)"),
  (re.compile(r"^\bIS NOW A\b"), "is now a", "Delimiter for Typecasting"),
  (re.compile(r"^O RLY\?\B"), "start if-else", "Start of IF-THEN Statement"),
  (re.compile(r"\bYA RLY\b"), "if case", "Keyword for the IF Case"),
  (re.compile(r"\bNO WAI\b"), "else case", "Keyword for the ELSE Case"),
  (re.compile(r"^IM IN YR\b"), "loop start", "Start of Loop"),
  (re.compile(r"^IM OUTTA YR\b"), "loop end", "End of Loop"),
  (re.compile(r"\bAN\b"), "an", "Delimiter for Nested Expressions"),
  (re.compile(r"\"[^\"]*\""), "YARN", const.YARN_LITERAL),
  (re.compile(r"\b-?\d*\.\d+\b"), "NUMBAR", "NUMBAR Literal"),
  (re.compile(r"\b-?\d+\b"), "literal", "NUMBR Literal"),
  (re.compile(r"\b(WIN|FAIL)\b"), "TROOF", "TROOF Literal"),
  (re.compile(r"\b(NOOB|NUMBR|NUMBAR|YARN|TROOF)\b"), "type literal", "TYPE Literal"),
  (re.compile(r"\bA\b"), "a", "Delimiter for Typecasting"),
  (re.compile(r"^[A-Za-z][\w]*\b"), "identifier", "Identifier"),
]
