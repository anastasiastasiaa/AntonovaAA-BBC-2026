print('Введите любое число')
a = int(input())
print('Введите любое число')
b = int(input())
print('Выберите операцию, которую вы бы хотели сделать между этими числами. Напишите +, -, * или /.')
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
else:
    print(a / b)