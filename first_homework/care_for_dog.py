
required_food_kg = int(input())
total_food_grams = 0
while True:
    command = input()
    if command == "Stop":
        break
    daily_food_grams = int(command)
    total_food_grams += daily_food_grams

required_food_grams = required_food_kg * 1000
differens = (required_food_grams - total_food_grams)

if required_food_grams > total_food_grams:
    print(f'Food is enough! Leftovers: {differens} grams.')
    print(f"So you spent {{differens / 1000 * 5.50:.2f}} leva for food.")
if required_food_grams == total_food_grams:
    print(f'Food is enough! Leftovers: {differens} grams.')
    print(f"So you spent {{total_food_grams / 1000 * 5.50:.2f}} leva for food.")
elif required_food_grams < total_food_grams:
    print(f"Food is not enough. You need {abs(total_food_grams-required_food_grams)} grams more.")
    print(f"So you spent {{abs(differens) / 1000 * 5.50:.2f}} leva for food.")
