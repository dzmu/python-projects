#Author Tanner Mesaric
FILE_NAME = "Assignments/assignment22/santas_list.txt"

def writeToys(toys):
    with open(FILE_NAME, "w") as file:
        for toy in toys:
            file.write(f"{toy}\n")

def readToys():
    toys = []
    with open(FILE_NAME) as file:
        for line in file:
            toys.append(line.strip())
    return toys

def listToys(toys):
    for toy in toys:
        print(f" - {toy}")



def addToys(toys):
    Etoy = input("Enter Toy: ")
    test = 0
    for toy in toys:
        if Etoy.lower().strip() == toy.lower().strip():
            print(f"{toy} is already in the list")
            test += 1
    if test == 0:
        toys.append(Etoy)
        print(f"{Etoy} was added.")
    return toys

def deleteToy(toys):
    Rtoy = input("Remove toy: ")
    test = 0
    for toy in toys:
        if Rtoy.lower().strip() == toy.lower().strip():
            toys.remove(toy)
            print(f"{toy} was removed.")
        else:
            test += 1
        if test == len(toys):
            print(f"Sorry, {Rtoy} was not found on the list.")
    return toys

print("Welcome to santas workshop!")
toys = readToys()
while True:
    choice = input("(L)ist, (A)dd, (D)elete, or (Q)uit: ").strip().lower()
    if choice == "a":
        addToys(toys)
    elif choice == "d":
        deleteToy(toys)
    elif choice == "l":
        listToys(toys)
    elif choice == "q":
        break
    else:
        print("Invalid Command")

writeToys(toys)
print("Goodbye")