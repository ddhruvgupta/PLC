import sys
from WAEParser import parser

import re
from collections import defaultdict
from pprint import pprint


# def eval_expression(tree):
#     while True:
#
#
# – FV(x) = {x},
# – FV(λx.M) = FV(M) ‐ {x}
# – FV(MN) = FV(M) ∪ FV(N)
def free_variables(tree):
    if tree[0] == 'num':
        return set()
    elif tree[0] == 'NAME':
        return set([tree[1]])
    elif tree[0] == 'APPLY':
        return free_variables(tree[1]).union(free_variables(tree[2]))
    elif tree[0] == 'LAMBDA':
        a = free_variables(tree[2])
        b = set([tree[1]])
        return a - b
    elif tree[0] in ['*', '/', '+', '-']:
        return free_variables(tree[1]).union(free_variables(tree[2]))


# λx.M =  λy.(M{x \ y})
def alpha(tree, var1):
    if tree[0] == 'LAMBDA':
        # get tree[1], replace all values of tree[1] in tree[2] with
        temp = tree[1]
        if tree[1] == var1:
            return tree
        else:
            tree[1] = var1
            replace(tree[2], var1, temp)
            return tree


def replace(tree, target, source):
    if tree[0] == 'num':
        return tree
    elif tree[0] == 'NAME':
        if tree[1] == target:
            return ['NAME', source]
        else:
            return tree
    elif tree[0] == 'APPLY':
        return ['APPLY', replace(tree[1], source, target),
                replace(tree[2], source, target)]

    elif tree[0] == 'LAMBDA':
        if tree[1] == target:
            return tree
        else:
            return ['LAMBDA', tree[1], replace(tree[2], target, source)]

    elif tree[0] in ['*', '/', '+', '-']:
        return ['APPLY', replace(tree[1], source, target),
                replace(tree[2], source, target)]


def substitution(tree, target, source):
    # – (λx.xy)[y := M]
    # y = target
    # M = source
    if tree[0] == 'num':
        return tree
    elif tree[0] == 'NAME':
        if tree[1] == target:
            return source
        else:
            return tree
    elif tree[0] == 'APPLY':

        return ['APPLY', substitution(tree[1], target, source),
                substitution(tree[2], target, source)]

    elif tree[0] == 'LAMBDA':
        if tree[1] == target:
            return tree
        elif tree[1] not in free_variables(source):
            return ['LAMBDA', tree[1], substitution(tree[2], target, source)]
        elif tree[1] in free_variables(source):
            t = replace(tree[2], tree[1] + "*", tree[1])
            return ['LAMBDA', tree[1] + "*", substitution(t, target, source)]

    elif tree[0] in ['*', '/', '+', '-']:
        return [tree[0], substitution(tree[1], target, source),
                substitution(tree[2], target, source)]


def beta_reduction(tree):
    # this function tries to find ONE beta reduction only. if found return beta reduction
    # return boolean to report if found

    if tree[0] == 'num':
        return (False, tree)
    elif tree[0] == 'NAME':
        return (False, tree)
    elif tree[0] == 'LAMBDA':
        found, tree_2 = beta_reduction(tree[2])
        if found:
            return (True, ['LAMBDA', tree[1], tree_2])
        else:
            return (False, tree)

    elif tree[0] == '*' or tree[0] == '-' or tree[0] == '+' or tree[0] == '/':
        found, tree_2 = beta_reduction(tree[1])
        if found:
            return (True, [tree[0], tree_2, tree[2]])
        else:
            found, tree_2 = beta_reduction(tree[2])
            if found:
                return (True, [tree[0], tree[1], tree_2])
            else:
                return (False, tree)

    else:  # this works for "APPLY"
        # check left child if LAMBDA
        if tree[1][0] == 'LAMBDA':
            return (True, substitution(tree[1][2], tree[1][1], tree[2]))
        else:
            found, tree_2 = beta_reduction(tree[1])
            if found:
                return (True, [tree[0], tree_2, tree[2]])
            else:
                found, tree_2 = beta_reduction(tree[2])
                if found:
                    return (True, [tree[0], tree[1], tree_2])
                else:
                    return (False, tree)


def eval(tree):
    if tree[0] in ['*', '/', '+', '-']:
        if tree[1][0] != 'num':
            tree[1] = eval(tree[1])

        if tree[2][0] != 'num':
            tree[2] = eval(tree[2])

        if tree[1][0] == 'num' and tree[2][0] == 'num':
            if tree[0] == '+':
                tree = ['num', tree[1][1]+tree[2][1]]
                return tree
            elif tree[0] == '-':
                tree = ['num', tree[1][1] - tree[2][1]]
                return tree
            elif tree[0] == '*':
                tree = ['num', tree[1][1] * tree[2][1]]
                return tree
            elif tree[0] == '/':
                tree = ['num', tree[1][1] / tree[2][1]]
                return tree

        return tree
    else:
        return tree


def inOrderTraversal(tree):
    # if tree[0] == 'APPLY':
    #     left = tree[1]
    #     right = tree[2]
    #
    #     if
    #     print('APPLY: ', left, right)

    print(tree[0])
    if len(tree) > 1:
        if type(tree[1]) == 'list':
            inOrderTraversal(tree[1])
        else:
            print(tree[1])
        if type(tree[2]) == 'list':
            inOrderTraversal(tree[2])
        else:
            print(tree[2])


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
        # inOrderTraversal(tree)
        if tree[0] == 'FV':
            print(free_variables(tree[1]))

        elif tree[0] == 'ALPHA':
            print(alpha(tree[1], tree[2]))

        elif tree[0] == 'substitute':
            print(substitution(tree[1], tree[2], tree[3]))

        else:
            while True:
                found, tree = beta_reduction(tree)
                if not found:
                    break
                print("beta: ", tree)

        # print()
            tree = eval( tree)
            print("beta: ", tree)
        # try:
        #     answer = eval_expression(tree)
        #     if answer == 'ERROR':
        #         print('\nEVALUATION ERROR\n')
        #     else:
        #         print('\nThe value is ' + str(answer) + '\n')
        # except:
        #     pass


main()
