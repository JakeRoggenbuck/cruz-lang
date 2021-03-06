import ply.lex as lex

# List of token names.
tokens = (
    'SET',
    'EQUAL',
    'NOT_EQUAL',
    'LESS',
    'GREATER',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'PLUS',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LCBRACK',
    'RCBRACK',
    'BYTE',
    'CHAR',
    'INT',
    'PREC',
    'PTR',
    'VAR_NAME',
    'IF',
    'ELIF',
    'ELSE',
    'WHILE',
    'FUNCTION',
    'RETURN',
    'RETURNS',
    'TAKES',
    'WRITE',
    'READ',
)

# Defines reserved words
reserved = {
    'byte':'BYTE',
    'char':'CHAR',
    'int':'INT',
    'prec':'PREC',
    'ptr':'PTR',
    'fun':'FUNCTION',
    'takes':'TAKES',
    'returns':'RETURNS',
    'return':'RETURN',
    'if':'IF',
    'elif':'ELIF',
    'else':'ELSE',
    'while':'WHILE',
    'write':'WRITE',
    'read':'READ',
}

def MyLexer():
    # Regular expression rules for simple tokens
    t_SET = r'\='
    t_EQUAL = r'\=='
    t_NOT_EQUAL = r'\!='
    t_LESS = r'\<'
    t_GREATER = r'\>'
    t_LESS_EQUAL = r'\<='
    t_GREATER_EQUAL = r'\>='
    t_PLUS = r'\+'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LCBRACK = r'\{'
    t_RCBRACK = r'\}'


    def t_DATA_TYPE_NAME(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'VAR_NAME')    # Check for reserved words
        return t

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
 
    # Build the lexer from my environment and return it    
    return lex.lex()
