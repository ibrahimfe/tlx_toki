input_str = input()
A, op, B = input_str.split()

A = int(A)
B = int(B)

if op == '+':
    result = A + B
elif op == '-':
    result = A - B
elif op == '*':
    result = A * B
elif op == '<':
    result = A < B
elif op == '>':
    result = A > B
elif op == '=':
    result = A == B

if op in ['+', '-', '*']:
    print(result)
elif result:
    print("benar")
else:
    print("salah")