#import predefined module time
import time 

#import user defined modules
from sum.sum import *
from diff.diff import diff
from user.user import User

print(sum(10, 20))
user1 = User("XYZ",1008)
user1.show_user()

#lists
list1 = [1,"XYZ",10.4, True]
print(lis1)
print(list1[1])
print(list1[:])
print(list1[1:])
print(list1[1:3])

for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

#Tuple
tup1 = (1,"XYz",10.4, True)
print(tup1)

#set
set1 = {1,2,3,1,4}
print(set1)

#dictionary
dict1 = {
    "fname":"XYZ",
    "Lname": "PQZ",
    "id" :91
}
print(dict1)
print(dict1["lname"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

for key in dict1.keys():
    print(dtc1[key])


# Checks if the file is the main execution file
if __name__ == "__main__":
    print(f'__name__:{__name__}')

