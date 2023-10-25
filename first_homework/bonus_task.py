import random
kids_in_grade = int(input("Enter the biggest student's numbers in grade: "))
list_of_numbers = []
for number in range(1, kids_in_grade + 1):
    list_of_numbers.append(number)
print()
sick_kids = input("Enter the number of the children who are absent, separated by ', ' \n"
                  "Or if there is noone absent-type'There is noone absent'").split(", ")

if sick_kids[0] != "There is noone absent":
    for number_of_sick_kid in sick_kids:
        if number_of_sick_kid in list_of_numbers:
            list_of_numbers.remove(int(number_of_sick_kid))
        elif number_of_sick_kid not in list_of_numbers:
            continue
print(list_of_numbers)
while True:
    print()
    command = input("Do you want to test someone?-type 'Yes' or 'No': ")
    if command.lower() == "no":
        break

    elif list_of_numbers == [] and command.lower() == "yes":
        print()
        print("There is no more children to test:)")
        break

    elif command.lower() == "yes":
        absent_kid = random.choice(list_of_numbers)
        print()
        print(f"The child who you are going to test is '{absent_kid}' number.")
        list_of_numbers.remove(absent_kid)
        continue
