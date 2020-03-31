import ply.lex as lex

# List of token names.
tokens = (
    'PLUS',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LCBRACK',
    'RCBRACK',
    #'NAME',
)

reserved = {
    'if':'IF',
    'elif':'ELIF',
    'else':'ELSE',
    'while':'WHILE',
    'fun':'FUNCTION',
    'write':'WRITE',
    'read':'READ',
    'byte':'BYTE',
    'char':'CHAR',
    'int':'INT',
    'prec':'PREC',
    'ptr':'PTR',
    'takes':'TAKES',
    'return':'RETURN',
    'returns':'RETURNS'
}

def MyLexer():
    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LCBRACK = r'\{'
    t_RCBRACK = r'\}'
    #t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


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
