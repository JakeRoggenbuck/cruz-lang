import sharlex

def read(fileName):
    with open(fileName) as f:
        lines = []
        lines += f.readlines()
        return lines

file_ = read('lex_test_file.cz')
data = """{}""".format("".join(file_[0:]))
lexed = sharlex.MyLexer()

lexed.input(data)

# Tokenize
while True:
    tok = lexed.token()
    if not tok: 
        break
    print(tok)
