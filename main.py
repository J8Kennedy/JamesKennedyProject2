text = open("Project2.txt","r")
lines = text.readlines()
for person in lines:
    id = person.strip().split(":")[0]
    gpa = person.strip().split(" ")[2]
    print(f"{id} has the gpa of {gpa}")