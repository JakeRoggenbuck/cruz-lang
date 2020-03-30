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
    'LPAREN',
    'RPAREN',
)

t_IF = r'if'
t_ELIF = r'elif'
t_ELSE = r'else'
t_WHILE = r'while'
t_FUNCTION = r'function'
t_READ = r'read'
t_WRITE = r'write'
t_READ = r'read'
t_BYTE = r'byte'
t_CHAR = r'char'
t_INT = r'int'
t_PREC = r'prec'
t_PTR = r'ptr'
t_LPAREN = r'\('
t_RPAREN = r'\)'
