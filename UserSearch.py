listUsers = []
usersCount = int(input("Enter users count: "))
for i in range(usersCount):
    name = str(input("Enter name: "))
    age = int(input("Enter age: "))
    mDict = {"name":name, "age":age}
    listUsers.append(mDict)

searchName = str(input("Enter search value: "))
a = False
for x in listUsers:
    if searchName == x['name']:
        print("Found Em! " + searchName + " is " + str(x['age']) + " years old!")
        a = True

if a != True:
    print("No such value found!")
