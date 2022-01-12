#author Tanner Mesaric

def sum(num):
    total = 0
    for i in range(num+1):
        total += i

def list_factors(numL):
    for i in range(1, numL + 1):
        if numL % i == 0:
            print(i, end = " ")
    print()

def factor(num, num2):
    factorsofnum = []
    correct = 0
    for i in range(1, num+1):
        if num % i == 0:
            factorsofnum.append(i)
    for i in range(len(factorsofnum)):
        false = len(factorsofnum)
        if factorsofnum[i] == num2:
            print(f"{num2} is a factor of {num}")

        else:
            correct+=1
        if correct == false:
            print(f"{num2} is not a factor of {num}")

print("Factor Fun")
while True:
    check = input("(C)heck Factor, (L)ist factors, or (Q)uit: ").strip().lower()
    if check == "c":
        num = int(input("Enter Number: "))
        num2 = int(input("Potential Factor: "))
        factor(num, num2)
    
    elif check =="l":
        numL = int(input("Enter Number: "))
        list_factors(numL)


    elif check =="q":
        print("Goodbye")
        break
    else: 
        print("Invalid command")

