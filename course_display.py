#Author Tanner Mesaric
def getCourses():
    courses = {}
    with open("Assignments/assignment19/course.txt") as file:
        for line in file:
            data = line.split(":")
            course = data[0].strip().lower()
            descripton = data[1].strip().lower()
            courses[course] = descripton
    return courses

def getDescription(courses):
    courseName = input("Enter course code: ").lower().strip()

    if courseName in courses:
        print(f"{courses[courseName]}")
    else:
        print(f"sorry, {courseName} is not in the dictionary")

def displayCourses(courses):
    for line in courses:
        print(f"{line}: {courses[line]}")

cL = getCourses()
#getDescription(cL)
print("Welcome to our course Library")
for i in cL:
    choice = input("Would you like to (V)iew, (L)ookup, or (Q)uit: ").lower().strip()
    if choice == "q":
        print("goodbye")
        break
    elif choice =="v":
        displayCourses(cL)
    elif choice =="l":
        getDescription(cL)