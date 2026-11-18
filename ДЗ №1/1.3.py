def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        return n1 / n2

print('Введите любое число')
n1 = int(input())
while True:
    print('Введите любое число')
    n2 = int(input())
    print('Выберите операцию, которую вы хотите сделать между этими числами. Напишите +, -, *, /.')
    op = input()
    n1 = calc(n1, n2, op)
    print(n1)

