num = int(input())
matr = []
sum_row = 0
for i in range(num):
    matr.clear()
    sum_row = 0
    for j in range(num):
        matr.append(j + 1 + num * i)
        sum_row += j + 1 + num * i
    print(sum_row)



