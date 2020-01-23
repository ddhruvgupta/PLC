import ply.yacc as yacc
from WAELexer import tokens


# follows the order of tokens defined in WARLexar.py


def p_waeStart(p):
    'waeStart : wae SEMI'
    p[0] = p[1]


def p_wae_1(p):
    'wae : NUMBER'
    p[0] = ['num', float(p[1])]


def p_wae_2(p):
    'wae : ID'
    p[0] = ['id', p[1]]


def p_wae_3(p):
    'wae : LBRACE PLUS wae wae RBRACE'
    p[0] = ['+', p[3], p[4]]


def p_wae_4(p):
    'wae : LBRACE MINUS wae wae RBRACE'
    p[0] = ['-', p[3], p[4]]


def p_wae_5(p):
    'wae : LBRACE TIMES wae wae RBRACE'
    p[0] = ['*', p[3], p[4]]


def p_wae_6(p):
    'wae : LBRACE DIV wae wae RBRACE'
    p[0] = ['/', p[3], p[4]]


def p_wae_7(p):
    'wae : LBRACE IF wae wae wae RBRACE'
    p[0] = ['if', p[3], p[4], p[5]]


# make rule for with {x 3} {+ x x}
def p_wae_8(p):
    'wae : LBRACE WITH var wae RBRACE'
    p[0] = ['with', p[3], p[4]]


# make rule for {x 3}
def p_wae_9(p):
    'var : LBRACE ID NUMBER RBRACE'
    # print(p[2])
    p[0] = [p[2], float(p[3])]


# make rule for {x {+ 3 3}}
def p_wae_10(p):
    'wae : LBRACE ID wae RBRACE'
    p[0] = [p[2], p[3]]


# # def p_wae_11(p):
#     '''wae : LBRACE wae wae RBRACE
#             | LBRACE wae wae wae RBRACE'''
#     a = list()
#     for i in range(2, len(p) - 1):
#         a.append(p[i])
#     p[0] = a


# make rule for with {x {with {x 3} {+ x x}} {}
def p_wae_11(p):
    'wae : LBRACE WITH wae wae RBRACE'
    p[0] = ['with', p[3], p[4]]


def p_wae_12(p):
    'var_list : LBRACE vlist RBRACE'
    print(p[1:])
    p[0] = ['var_list', p[2]]


def p_wae_13(p):
    '''vlist : var
             | var vlist '''
    p[0] = p[1:]


# def p_vlist(p):
#     '''vlist : var vlist'''
#     p[0] = p[1:]


def p_wae_14(p):
    'wae : LBRACE WITH var_list wae RBRACE'
    p[0] = ['with', p[3], p[4]]


def p_error(p):
    print("Syntax error in input!" + str(p))


parser = yacc.yacc()
