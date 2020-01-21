from WAEParser import parser


def substitute_var(var, exprn):
    # print(exprn)
    var_name = var[0]
    var_val = var[1]
    # if type(var[1] == float):
    #     var_val = var[1]
    # else:
    #     var_val = eval_expression(var[1])

    if exprn[0] == 'id' and exprn[1] == var_name:
        exprn[0] = 'num'
        exprn[1] = var_val
    elif exprn[0] == '+'or exprn[0] == 'with':
        exprn[1] = substitute_var(var, exprn[1])
        exprn[2] = substitute_var(var, exprn[2])

    print(exprn)
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
        var = eval_expression(tree[1])
        # for i in range(0, len(tree[2]) - 1):
        #     tree[2][1] = substitute_var(var, tree[2][i])
        exprn = tree[2]
        tree[2] = substitute_var(var, exprn)
        print(tree[2])
        return eval_expression(tree[2])

    elif tree[0] == 'var':
        return [tree[1], tree[2]]


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
