count_of_work = int(input())
total_points = 0
red = 0
orange = 0
yellow = 0
white = 0
other = 0
black = 0
for coun_of_work in range(count_of_work):
    color = input()
    if color == "red":
        red += 1
        total_points += 5
    elif color == "orange":
        orange += 1
        total_points += 10
    elif color == "yellow":
        yellow += 1
        total_points += 15
    elif color == "white":
        white += 1
        total_points += 20
    elif color == "black":
        black += 1
        total_points //= 2
    else:
        other += 1

print(f"Total points: {total_points}")
print(f"Red sector: {red}")
print(f"Orange sector: {orange}")
print(f"Yellow sector: {yellow}")
print(f"White sector: {white}")
print(f"Other colors picket: {other}")
print(f"Divides from black sector: {black}")