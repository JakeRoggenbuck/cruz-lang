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
    'WRITE',
    'READ',
    'BYTE',
    'CHAR',
    'INT',
    'PREC',
    'PTR',
    'TAKES',
    'RETURN',
    'RETURNS',
    'LPAREN',
    'RPAREN',
    'LCBRACK',
    'RCBRACK',
)

def MyLexer():
    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_IF = r'if'
    t_ELIF = r'elif'
    t_ELSE = r'else'
    t_WHILE = r'while'
    t_FUNCTION = r'fun'
    t_WRITE = r'write'
    t_READ = r'read'
    t_BYTE = r'byte'
    t_CHAR = r'char'
    t_INT = r'int'
    t_PREC = r'prec'
    t_PTR = r'ptr'
    t_TAKES = r'takes'
    t_RETURN = r'return'
    t_RETURNS = r'returns'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LCBRACK = r'\{'
    t_RCBRACK = r'\}'


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
