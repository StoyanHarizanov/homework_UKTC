num = int(input())
sum_of_numbers = 0
for numbers in range(num):
    number = input().split(", ")
    for i in number[num - numbers - 1:]:
        sum_of_numbers += int(i)
print(sum_of_numbers)