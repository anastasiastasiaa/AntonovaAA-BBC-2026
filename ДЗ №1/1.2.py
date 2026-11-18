def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def umnozh(a, b):
    return a * b
def razdel(a, b):
    return a / b

print('Введите любое число')
n1 = int(input())
print('Введите любое число')
n2 = int(input())
print('Выберите операцию, которую вы бы хотели сделать между этими числами. Напишите +, -, * или /.')
op = input()
if op == '+':
    print(plus(n1, n2))
elif op == '-':
    print(minus(n1, n2))
elif op == '*':
    print(umnozh(n1, n2))
else:
    print(razdel(n1, n2))
