list = []
UserCount = int(input("please enter number of users : "))

for a in range (0,UserCount) :
    member = [input("please enter User Name : "),int (input("please enter User age : "))]
    list.append(member)

userfound = 0
GivenName = input("please enter user name to search:")
for searchName in list:
    if GivenName == searchName[0]:
             print(searchName[1])
             break
    else:
        userfound = userfound + 1
        
    if userfound == UserCount :
        print("There is no user with given name")
        
