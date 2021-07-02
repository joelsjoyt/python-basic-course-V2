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
print(f'List : {list1}')
print(f'List element at index 1 : {list1[1]}')
print(f"List tuple ':' : {list1[:]}")
print(f"List from index 1 till end : {list1[1:]}")
print(f'List from 1 to 3: {list1[1:3]}')

for i in list1:
    print(f'List values: {i}')

for i in range(len(list1)):
    print(f'List values: {list1[i]}')

#Tuple
tup1 = (1,"XYz",10.4, True)
print(f'Tuple : {tup1}')

#set
set1 = {1,2,3,1,4}
print(f'Tuple : {set1}')

#dictionary
dict1 = {
    "fname":"XYZ",
    "lname": "PQZ",
    "id" :91
}
print(f'Dictionary : {dict1}')
print(f"Dictonary of key 'lname' : {dict1['lname']}")
print(f'Print Dictonary keys : {dict1.keys()}')
print(f'Print Dictionary Values : {dict1.values()}')
print(f'Print dictionary as key value pair: {dict1.items()}')

for key in dict1.keys():
    print(f'Dictionary Values: {dict1[key]}')


# Checks if the file is the main execution file
if __name__ == "__main__":
    print(f'__name__:{__name__}')

