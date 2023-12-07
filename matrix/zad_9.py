num = int(input())
the_biggest = 0
for i in range(num):
    numbers = input().split(", ")
    sec_half = numbers[num:]
    sum_sec_half = 0
    for i in sec_half:
        sum_sec_half += int(i)
    first_half = numbers[:num]
    sum_first_half = 0
    for j in first_half:
        sum_first_half += int(j)
    the_biggest += max(sum_first_half, sum_sec_half)
print(the_biggest)
