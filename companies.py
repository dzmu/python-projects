# author Tanner Mesaric
companies = ["Apple", "CVS", "Twitter", "Samsung", "android", "Jack", "CFA", "Wendys", "Cisco", "Facebook"]
addCompanies = []

while True:
    companiesOptions = input ("(V)iew, (A)dd company to wish list, (R)emove company from wish list, (Q)uit: ").strip().lower()
    if companiesOptions == "v":
        viewOptions = input ("View (A)ll companies or your (W)ish list? ").strip().lower()
        if viewOptions == "a":
            for company in companies:
                print(f"-{company}")
        elif viewOptions == "w":
            for company in addCompanies:
                print(f"-{company}")
        else:
            print("Invalid command")
    elif companiesOptions == "a":
        addCompany = input ("Enter company: ").strip().lower()
        addCompanies.append(addCompany)
    elif companiesOptions == "r":
        ReCompany = input ("Enter company: ").strip().lower()
        addCompanies.remove(ReCompany)
    elif companiesOptions == "q":
        break
    else:
        print("Invalid command")

print("Goodbye")

            

