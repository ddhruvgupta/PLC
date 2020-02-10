import ply.yacc as yacc
from WAELexer import tokens


def p_ramStart(p):
    'ramStart : ram'
    p[0] = p[1]


def p_ram_1(p):
    'ram : NUMBER'
    print(p[1])
    p[0] = ['num', float(p[1])]


def p_ram_2(p):
    'ram : REG'
    p[0] = ['REG', p[1].upper()]


def p_ram_3(p):
    'ram : REG EQUALS NUMBER'
    p[0] = ['=', p[1].upper(), p[3]]


def p_ram_4(p):
    'ram : INC REG'
    p[0] = ['INC', p[2].upper()]


def p_ram_5(p):
    'ram : DEC REG'
    p[0] = ['DEC', p[2].upper()]


def p_ram_6(p):
    'ram : REG ram'
    p[0] = ['IF', p[1].upper(), p[2]]


def p_ram_7(p):
    'ram : JMP LABEL'
    p[0] = ['JMP', p[2].upper().strip('AB')]


def p_ram_8(p):
    'ram : LABEL ram'
    p[0] = [p[1].upper().strip('AB'), p[2]]


def p_ram_9(p):
    'ram : MOV REG COMMA REG'
    p[0] = ['MOV', p[2].upper(), p[4].upper()]


def p_ram_10(p):
    'ram : CONTINUE'
    p[0] = ['CON']


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()
