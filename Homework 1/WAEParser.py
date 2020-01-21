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


def p_wae_8(p):
    'wae : LBRACE WITH wae wae RBRACE'
    p[0] = ['with', p[3], p[4]]


def p_wae_9(p):
    'wae : LBRACE ID NUMBER RBRACE'
    # print(p[2])
    p[0] = ['var', p[2], float(p[3])]


def p_wae_10(p):
    'wae : LBRACE wae wae RBRACE'
    # print(p[2])
    p[0] = ['var2', p[2], p[3]]


def p_wae_11(p):
    'wae : LBRACE wae wae wae RBRACE'
    # print(p[2])
    p[0] = [p[1], p[2], p[3]]


def p_error(p):
    print("Syntax error in input!" + str(p))


parser = yacc.yacc()
