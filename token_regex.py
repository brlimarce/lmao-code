import re

token_regex = [
  (re.compile(r"^HAI\b"), "start"),
  (re.compile(r"^KTHXBYE\b"), "end"),
  (re.compile(r"\bBTW\b"), "comment_single"),
  (re.compile(r"\bOBTW\b"), "comment_start"),
  (re.compile(r"\bTLDR\b"), "comment_end"),
  (re.compile(r"^I HAS A\b"), "declaration"),
  (re.compile(r"\bITZ\b"), "its"),
  (re.compile(r"^\bR\b"), "assignment"),
  (re.compile(r"\bSUM OF\b"), "arithmetic_op"),
  (re.compile(r"^\bIFF OF\b"), "arithmetic_op"),
  (re.compile(r"\bPRODUKT OF\b"), "arithmetic_op"),
  (re.compile(r"\bQUOSHUNT OF\b"), "arithmetic_op"),
  (re.compile(r"\bMOD OF\b"), "arithmetic_op"),
  (re.compile(r"\bBIGGR OF\b"), "arithmetic_op"),
  (re.compile(r"\bSMALLR OF\b"), "arithmetic_op"),
  (re.compile(r"\bBOTH OF\b"), "boolean_op"),
  (re.compile(r"\bEITHER OF\b"), "boolean_op"),
  (re.compile(r"\bWON OF\b"), "boolean_op"),
  (re.compile(r"\bNOT\b"), "boolean_op"),
  (re.compile(r"\bANY OF\b"), "boolean_op"),
  (re.compile(r"\bALL OF\b"), "boolean_op"),
  (re.compile(r"\bBOTH SAEM\b"), "BOTH SAEM"),
  (re.compile(r"\bDIFFRINT\b"), "DIFFRINT"),
  (re.compile(r"\bSMOOSH\b"), "concat"),
  (re.compile(r"\bMKAY\b"), "mkay"),
  (re.compile(r"\bMAEK\b"), "inf_end"),
  (re.compile(r"\bA\b"), "A"),
  (re.compile(r"^\bIS NOW A\b"), "typecast"),
  (re.compile(r"^VISIBLE\b"), "output"),
  (re.compile(r"\bGIMMEH\b"), "input"),
  (re.compile(r"^O RLY\?\b"), "start-if"),
  (re.compile(r"\bYA RLY\b"), "if_"),
  (re.compile(r"\bMEBBE\b"), "else_if"),
  (re.compile(r"\bNO WAI\b"), "else"),
  (re.compile(r"^OIC\b"), "cond-end"),
  (re.compile(r"^WTF\?\b"), "switch-start"),
  (re.compile(r"\bOMG\b"), "switch0"),
  (re.compile(r"\bOMGWTF\b"), "switch-default"),
  (re.compile(r"^IM IN YR\b"), "loop-start"),
  (re.compile(r"\bUPPIN\b"), "inc"),
  (re.compile(r"\bNERFIN\b"), "dec"),
  (re.compile(r"^YR\b"), "your"),
  (re.compile(r"\bTIL\b"), "until"),
  (re.compile(r"\bWILE\b"), "while"),
  (re.compile(r"^IM OUTTA YR\b"), "loop-end"),
  (re.compile(r"\bAN\b"), "and "),
  (re.compile(r"\"[\w!@#$%^&*()_+=-\[\]\\/.,;'{}| ]*\""), "string"),
  (re.compile(r"\bA (NOOB|NUMBR|NUMBAR|YARN|TROOF)\b"), "typeliteral"),
  (re.compile(r"\b-?\d+\b"), "literal"),
  (re.compile(r"\b-?\d*\.\d+\b"), "literal"),
  (re.compile(r"\b\"[^\"]*\"\b"), "literal"),
  (re.compile(r"\b(WIN|FAIL)\b"), "literal"),
  (re.compile(r"^[A-Za-z][\w]*\b"), "var")
]
