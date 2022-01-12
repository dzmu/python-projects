class Job:
    def __init__(self, title, description, skills, length, pay):
        self.title = title
        self.description = description
        self.skills = skills
        self.length = length
        self.pay = pay

    def is_match(self, title):
        if title == self.title:
            return True
        elif title != self.title:
            return False

    def display(self):
        print(" ")
        print(f"""*** {self.title} ***""")
        print(f"{self.description}")
        print("Skills: ")
        for skills in self.skills:
            print(f"- {skills}")
        print(f"Contract Length: {self.length}")
        print(f"""Pay rate: {self.pay}
        """)
