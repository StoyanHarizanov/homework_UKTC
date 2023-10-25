count_of_peeople = int(input())
the_best_stu = ""
the_best_score = -1
for participate in range(count_of_peeople):
    name = input()
    total_score = 0
    while True:
        command = input()
        if command == "Stop":
            break
        command = int(command)
        total_score += command
    print(f"{name} has {total_score} points.")
    if total_score > the_best_score:
        the_best_stu = name
        the_best_score = total_score
        print(f"{the_best_stu} is the new number 1!")
print(f"{the_best_stu} won competition with {the_best_score} points!")

