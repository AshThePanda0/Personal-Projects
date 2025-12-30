def num_assign():
    num = input("Please enter the number of assignments: ")
    while not num.isdigit():
        print("That was not an integer.")
        num = input("Please enter the number of assignments: ")
    return int(num)

def due_date():
    print("Please enter the due date")
    d = input("In format mm/dd/yyyy: ")
    date = ""
    for l in d:
        if l.isdigit() or l == "/":
            date += l
    return date

def name():
    name = input("Please enter the name of the assignment: ")
    return name

def main ():
    # Tell user the program
    print("This is a assignment organizer")
    print("This program will take in a number of assignments "
          "and explain information based on due date")
    x = num_assign()
    print(f"You have {x} assignments to enter")
    print("If this is incorrect, please rerun program and try again")
    count = 0
    assignments = {}
    while count < x:
        assignments[name()] = due_date()
        count += 1
    print(assignments)

    print("With this information, you can: ")
    print("1. Arrange by soonest due date")
    print("2. Arrange by alphabetical order")
    print("3. Exit Assignment")
    option = input("What would you like to do? ")

    while option != "3":
        while option != "1" and option != "2" and option != "3":
            print("That is not an option.")
            option = input("What would you like to do? ")

        if option == "1":
            print("Yes")
            option = input("What would you like to do? ")

        elif option == "2":
            print("No")
            option = input("What would you like to do? ")

    print("Thank you for using this program")


main()