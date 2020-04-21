import ply.lex as lex

reserved = {'if': 'IF', 'with': 'WITH'}
tokens = ['NUMBER', 'REG', 'INC', 'DEC', 'JMP', 'CONTINUE', 'CLR', 'MOV', 'EQUALS', 'LABEL', 'COMMA'] + \
    list(reserved.values())

t_REG = r'[Rr][0-9]*'
t_INC = r'[I][N][C]'
t_DEC = r'[D][E][C]'
t_JMP = r'[J][M][P]'
t_CONTINUE = r'[C][O][N][T][I][N][U][E]'
t_CLR = r'[CLR]'
t_MOV = r'[M][O][V]'
t_EQUALS = r'\='
t_LABEL = r'[Nn][0-9][ab]*'
t_COMMA = r'\,'
t_IF = r'[iI][fF]'


def t_NUMBER(t):
    r'[-+]?[0-9]+(\.([0-9]+)?)?'
    t.value = float(t.value)
    t.type = 'NUMBER'
    return t


# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # t.lexer.skip(1)
    raise Exception('LEXER ERROR')


lexer = lex.lex()
## Test it out


# # data = '''
# # { with {x 26} {* {+ x 20} {+ y 22}}};
# # # '''
# data = '''
# INC R1
# '''
#
# #
# ## Give the lexer some input
# lexer.input(data)
# #
# ## Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
