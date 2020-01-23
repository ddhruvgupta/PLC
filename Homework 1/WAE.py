from WAEParser import parser
import re


def substitute_var(var_map, exprn):
    if exprn[0] == 'id':
        exprn[0] = 'num'
        exprn[1] = var_map.get(exprn[1])
    elif exprn[0] == '+' or exprn[0] == '-' or exprn[0] == '*' or exprn[0] == '/' or exprn[0] == 'with':
        exprn[1] = substitute_var(var_map, exprn[1])
        exprn[2] = substitute_var(var_map, exprn[2])

    return exprn


def eval_expression(tree):
    if tree[0] == 'num':
        return tree[1]
    elif tree[0] == 'id':
        return 'ERROR'
    elif tree[0] == '+' or tree[0] == '-' or tree[0] == '*' or tree[0] == '/':
        v1 = eval_expression(tree[1])
        if v1 == 'ERROR':
            return 'ERROR'
        v2 = eval_expression(tree[2])
        if v2 == 'ERROR':
            return 'ERROR'
        if tree[0] == '+':
            return v1 + v2
        elif tree[0] == '-':
            return v1 - v2
        elif tree[0] == '*':
            return v1 * v2
        elif v2 != 0:
            return v1 / v2
        else:
            return 'ERROR'
    elif tree[0] == 'if':  # if clause
        v1 = eval_expression(tree[1])
        if v1 == 'ERROR':
            return 'ERROR'
        if v1 != 0:
            return eval_expression(tree[2])
        else:
            return eval_expression(tree[3])

    elif tree[0] == 'with':
        var_map = dict()
        try:
            var_map = eval_expression(tree[1])
        except:
            print(var_map)
            print("Exit")

        exprn = tree[2]
        tree[2] = substitute_var(var_map, exprn)
        print(tree[2])
        return eval_expression(tree[2])

    elif tree[0] == 'var_list':
        soln = dict()
        a = tree[1]
        while isinstance(a, list):
            soln[a[0][0]] = a[0][1]
            try:
                a = a[1]
            except:
                a = 1

        return soln

    elif re.match(r"[a-zA-Z]*", tree[0]):
        if type(tree[1]) == float:
            return {tree[0]: tree[1]}
        else:
            val = eval_expression(tree[1])
            # print(tree[0], val)
            return {tree[0]: val}

        # return [tree[0], tree[1]]


def read_input():
    result = ''
    while True:
        data = input('WAE: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i + 1]
            break
        else:
            result += data + ' '
    return result


def main():
    while True:
        data = read_input()
        if data == 'exit;':
            break
        try:
            tree = parser.parse(data)
        except Exception as inst:
            print(inst.args[0])
            continue
        print(tree)
        try:
            answer = eval_expression(tree)
            if answer == 'ERROR':
                print('\nEVALUATION ERROR\n')
            else:
                print('\nThe value is ' + str(answer) + '\n')
        except:
            pass


if __name__ == '__main__':
    main()
