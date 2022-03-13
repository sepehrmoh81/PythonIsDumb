listUsers = []
usersCount = int(input("Enter users count: "))
for i in range(usersCount):
    name = str(input("Enter name: "))
    age = int(input("Enter age: "))
    mDict = {"name":name, "age":age}
    listUsers.append(mDict)

searchName = str(input("Enter search value: "))
found = False
for x in listUsers:
    if searchName == x['name']:
        print("Found Em! " + searchName + " is " + str(x['age']) + " years old!")
        found = True

if found == False:
    print("No such value found!")
