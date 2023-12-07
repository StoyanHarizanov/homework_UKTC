num = int(input())
sum_of_numbers = 0
for numbers in range(num):
    number = input().split(", ")
    sum_of_numbers += int(number[numbers])

print(sum_of_numbers)