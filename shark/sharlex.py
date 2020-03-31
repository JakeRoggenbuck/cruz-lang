import ply.lex as lex

# List of token names.
tokens = (
    'PLUS',
    'NUMBER',
    'IF',
    'ELIF',
    'ELSE',
    'WHILE',
    'FUNCTION',
    'FUNCTION_NAME',
    'WRITE',
    'READ',
    'BYTE',
    'BYTE_VAR',
    'CHAR',
    'CHAR_VAR',
    'INT',
    'INT_VAR',
    'PREC',
    'PREC_VAR',
    'PTR',
    'PTR_VAR',
    'TAKES',
    'RETURN',
    'RETURNS',
    'LPAREN',
    'RPAREN',
    'LCBRACK',
    'RCBRACK',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_WHILE = r'while'
t_FUNCTION = r'fun'
t_FUNCTION_NAME = f'{t_FUNCTION} [a-zA-z0-9_]* '
t_WRITE = r'write'
t_READ = r'read'
t_BYTE = r'byte'
t_BYTE_VAR = f'{t_BYTE} [a-zA-z0-9_]*'
t_CHAR = r'char'
t_CHAR_VAR = f'{t_CHAR} [a-zA-z0-9_]*'
t_INT = r'int'
t_INT_VAR = f'{t_INT} [a-zA-z0-9_]*'
t_PREC = r'prec'
t_PREC_VAR = f'{t_PREC} [a-zA-z0-9_]*'
t_PTR = r'ptr'
t_PTR_VAR = f'{t_PTR} [a-zA-z0-9_]*'
t_TAKES = r'takes'
t_RETURN = r'return'
t_RETURNS = r'returns'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCBRACK = r'\{'
t_RCBRACK = r'\}'

lexer = lex.lex()

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def parlex(data):
    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

