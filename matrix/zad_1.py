num = int(input())
matr = []
for i in range(num):
    matr.clear()
    for j in range(num):
        matr.append(j + 1 + num * i)
    print(matr)
