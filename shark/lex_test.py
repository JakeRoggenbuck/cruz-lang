 import ply.lex as lex


tokens = (
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
    'NAME',
)


t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_WHILE = r'while'
t_FUNCTION = r'function'
t_WRITE = r'write'
t_READ = r'read'
t_BYTE = r'byte'
t_CHAR = r'char'
t_INT = r'int'
t_PREC = r'prec'
t_PTR = r'ptr'
t_TAKES = r'takes',
t_RETURN = r'return',
t_RETURNS = r'returns',
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCBRACK = r'\{'
t_RCBRACK = r'\}'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
