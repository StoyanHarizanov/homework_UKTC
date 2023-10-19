egg_size = input()
egg_color = input()
partidi_count = int(input())
total_sum_christmas = 0

if egg_size == "Small":
    if egg_color == "Red":
        total_sum_christmas += 9
    if egg_color == "Green":
        total_sum_christmas += 8
    if egg_color == "Yellow":
        total_sum_christmas += 5
elif egg_size == "Medium":
    if egg_color == "Red":
        total_sum_christmas += 13
    if egg_color == "Green":
        total_sum_christmas += 9
    if egg_color == "Yellow":
        total_sum_christmas += 7
elif egg_size == "Large":
    if egg_color == "Red":
        total_sum_christmas += 16
    if egg_color == "Green":
        total_sum_christmas += 12
    if egg_color == "Yellow":
        total_sum_christmas += 9

total_sum_christmas *= partidi_count
total_sum_christmas_TAX = total_sum_christmas * 0.35
total_sum_christmas -= total_sum_christmas_TAX

print(f"You have earned {total_sum_christmas:.2f} leva")