# Четене на имената на децата и n-тото хвърляне
children = input().split()
n = int(input())

# Инициализация на индекса на текущото дете
current_child_index = 0

# Симулиране на играта
while len(children) > 1:
    # Пресмятане на индекса на детето, което ще бъде премахнато
    current_child_index = (current_child_index + n - 1) % len(children)

    # Изваждане на детето, което е премахнато
    removed_child = children.pop(current_child_index)

    # Отпечатване на информация за премахнатото дете
    print(f"Removed {removed_child}")

# Отпечатване на останалото дете, което е победител
print(f"Winner is {children[0]}")
