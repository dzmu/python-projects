#Author Tanner Mesaric
print("Let's Configure your Homework List")

homeworkList = []

while True:
    homeworkI = input ("Enter Homework Item: ")
    homeworkList.append(f"{homeworkI}")
    addAgain = input ("Would you like to add another item (Y)es or (N)o: ").strip().lower()

    if addAgain != "y":
        break


print ("Here's Your Homework List: ")
for i in range (len(homeworkList)):
    print(f"- {homeworkList[i]}")