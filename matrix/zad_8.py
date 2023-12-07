num = int(input())
matr = []
check = True
for number in range(num):
    matr.append(input())
symbol = input()
for row in range(num):
    row_matr = matr[row]
    for index, col in enumerate(row_matr):
        if col == symbol:
            print(f"({row}, {index})")
            check = False
if check:
    print(f"{symbol} does not exist in matrix!")


