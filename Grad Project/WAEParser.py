import ply.yacc as yacc
from LambdaLexer import tokens


def p_exprStart(p):
    'exprStart : expr SEMI'
    p[0] = p[1]


def p_exprStart2(p):
    'exprStart : expr LBRACKET NAME EQUALS expr RBRACKET SEMI'
    p[0] = ['substitute', p[1], p[3].upper(), p[5]]


def p_exprStart3(p):
    'exprStart : FV LBRACKET expr RBRACKET SEMI'
    p[0] = ['FV', p[3]]


def p_exprStart4(p):
    'exprStart : ALPHA LBRACKET expr COMMA NAME RBRACKET SEMI'
    p[0] = ['ALPHA', p[3], p[5].upper()]


def p_expr_1(p):
    'expr : NUMBER'
    p[0] = ['num', float(p[1])]


def p_expr_2(p):
    'expr : NAME'
    p[0] = ['NAME', p[1].upper()]


def p_expr_3(p):
    'expr : LPAREN expr expr RPAREN'
    p[0] = ['APPLY', p[2], p[3]]


def p_expr_4(p):
    'expr : LPAREN LAMBDA NAME expr RPAREN'
    p[0] = ['LAMBDA', p[3].upper(), p[4]]


def p_expr_5(p):
    'expr : LPAREN OP expr expr RPAREN'
    p[0] = [p[2], p[3], p[4]]


def p_error(p):
    print(p)
    print("Syntax error in input!")


parser = yacc.yacc()
