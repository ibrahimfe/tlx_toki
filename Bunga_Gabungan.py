bungaG, bungaQ = input().split(" ")

bungaG = int(bungaG)
bungaQ = int(bungaQ)

total = bungaG ** 2 + bungaQ ** 2 + 1

if total % 4 == 0:
    print(total % 4)
else: 
    print(-1)