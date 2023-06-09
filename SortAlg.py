from random import randrange

opsList = ["1", "2", "3", "4", "5"]
list = []

def addNumber(number):
    try:
        number = float(number)
    except:
        print("\nInvalid input!")
    else:
        list.append(number)
        print("\nNumber successfully added")

def drawNumbers(amount, lower, upper):
    for _ in range(10**amount):
        list.append(float(randrange(lower, upper+1)))

def sortList(sort):
    for i in range(len(list)):
        min = list[i]
        ind = 0
        if sort == "1":
            for j in range(i, len(list)):
                if list[j] < min:
                    min = list[j]
                    ind = j
        else:
            for j in range(i, len(list)):
                if list[j] > min:
                    min = list[j]
                    ind = j 
        if ind > 0:
            list.insert(i, min)
            list.pop(ind+1)


while True:
    print("\nSorting program\n")
    print("1 - Add a number")
    print("2 - Draw numbers")
    print("3 - Clear list")
    print("4 - Sorting list")
    print("5 - Exit\n")

    op = ""

    while op not in opsList:
        op = input("Select an option: ")
    print()

    if op == "1":
        number = input("Enter a number: ")
        addNumber(number)

    elif op == "2":
        print("Amount of numbers\n")
        print("1 - Ten\n2 - Hundred\n3 - Thousand\n4 - Ten Thousand")
        while True:
            amount = input("Select an option: ")
            if amount == "1" or "2" or "3" or "4":
                break
        while True:
            lower = input("Enter the lower limit for the draw: ")
            if lower.isnumeric():
                break
        while True:
            upper = input("Enter the upper limit for the draw: ")
            if upper.isnumeric():
                break
        drawNumbers(int(amount), int(lower), int(upper))
        print("Numbers successfully added")
    
    elif op == "3":
        list.clear()
        print("The list has been emptied")

    elif op == "4":
        if len(list) > 0:
            print("Sorting types\n")
            print("1 - Ascending\n2 - Descending\n")
            while True:
                sort = input("Select an option: ")
                if sort == "1" or "2":
                    break
            print(f"\nInitial list: {str(list)[1:-1]}\n")
            sortList(sort)
            print(f"Final list: {str(list)[1:-1]}\n")
        else:
            print("Empty list, insert some element before sorting")
    
    elif op == "5":
        print("Thank You!")
        break