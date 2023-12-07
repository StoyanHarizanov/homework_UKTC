num = int(input())
sum_of_numbers = 0
for numbers in range(num):
    number = input().split(", ")
    sum_of_numbers += int(number[num - numbers - 1])

print(sum_of_numbers)