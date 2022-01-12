from job import Job

def get_jobs():
    jobs = []
    with open("assignments/assignment24/job.txt") as file:
        for line in file:
            data = line.split(',')
            title = data[0].strip()
            description = data[1].strip()
            skills_test = data[2].strip()
            data2 = skills_test.split('*')
            skills = []
            for i in data2:
                skills.append(i)
            length = data[3].strip()
            pay = data[4].strip()
            jobs.append(Job(title, description, skills, length, pay))
    return jobs

jobs = get_jobs()
while True:
        choice = input("(L)ist all jobs (D)etails, or (Q)uit: ").lower().strip()
        if choice == "q":
            print("Goodbye")
            break
        if choice == "l":
            for i in jobs:
                i.display()
        elif choice == "d":
            title = input("Enter Job Name: ")
            for i in jobs:
                if i.is_match(title) == True:
                    i.display()
        else:
            print("invalid command")


