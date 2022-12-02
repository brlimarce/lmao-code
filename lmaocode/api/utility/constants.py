"""
* Constants
| Is a collection of static variables.
"""

# * File Structure
TEST_DIR = 'api/test/'
FILE_EXT = '.lol'

# * Lexer Constants
UNDERSCORE = "_"
SPACE = " "
DASH = "-"

ARITHMETIC_OP = "Arithmetic Operator"
BOOLEAN_OP = "Boolean Operator"
COMPARISON_OP = "Comparison Operator"
LITERAL = "Literal"
YARN_LITERAL = "YARN Literal"
BTW_KEYWORD = "Single Comment"
OBTW_KEYWORD = "Start of Multiline Comment"
TLDR_KEYWORD = "End of Multiline Comment"
EMPTY_STRING = ""

# * Error Messages
INVALID_TOKEN = "Invalid Token"
MISPLACED_OBTW = "OBTW/TLDR are misplaced."
SYNTAX_ERROR = "Syntax Error"

# * Parser
VAR_DECLARATION= "Variable Declaration"
TYPECAST= ["Explicit Typecasting", "Delimiter for Typecasting"]
PRINT= "Input"

# * Semantics Analyzer
NOOB = "NOOB"