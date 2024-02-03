B, P, L = input().split(" ")

B = int(B)
P = int(P)
L = int(L)

if B <= 10 and P <= 40 and L <= 90:
    print("S")
elif B <= 14 and P <= 60 and L <= 120:
    print("M")
elif B <= 18 and P <= 80 and L <= 180:
    print("L")
else:
    print("X")
