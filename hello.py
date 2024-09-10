import pymongo
from pymongo import MongoClient


# print("hello world")
# varible=[1,2,3,4]
# var1 = 123
# var2 = 123.123
# var3 = 123.1
# var4 = "abc"
# var5 = 'a'
# var6 = {
#     "name": "John",
#     "age": 30,
#     "address":{
#         "street": "123 Main St",
#         "city": "Anytown",
#         "state": "CA",
#     }
# }
# print(varible)
# print(var1)
# # print(type(var1))
# print(var2)
# print(var3)
# print(type(var4))
# print(var5)
# print(type(var6))

# var6['name'] = 'new'
# print(var6)
# full = var6['name']
# full = var6['name1']       // it will return  kew error 
# full = var6.get('name')       // same as above
# full = var6.get('name1')        // it will return none 

# full = var6["address"]['city']
# full = var6.get('address').get('city')     another method >>>>
# print(full)
# full = var6.get('address')
# city = full.get('city')
# print(city)

students = [
    {
        "name": "John",
        "age": 30,
        "address":{
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        }
    },
    {
        "name": "John1",
        "age": 3,
        "address":{
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        }
    },

    123,'abc'
]

# print(students)
# print(students[0])
# print(students[1])
student1 = students[0]
# type casting 
# student2 = list(students[1])
# student2 = [students[1]]




# for student in students:
#     print(student)





