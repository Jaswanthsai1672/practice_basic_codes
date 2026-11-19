# # # numbers = [1, 2, 3, 4,4,5,3,6,5]
# # # print(numbers)

# # # numbers = []
# # # number = list((1,2,4,5))
# # # print(number)
# # # print(numbers)

# # numbers = list()
# # print(numbers)

# # numbers = []
# # numbers.append(10)
# # numbers.append(30)
# # numbers.append(50)
# # numbers.append(20)
# # print(numbers)

# # numbers.insert(2,40)
# # print(numbers)

# # numbers.extend([60, 70, 80])
# # print(numbers)
# # numbers.remove(20)
# # print(numbers)

# # numbers.insert(1,20)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # print(numbers[0])
# # print(numbers[1])
# # print(numbers[2])
# # print(numbers[3])
# # print(numbers[4])
# # print(numbers[5])
# # print(numbers[6])
# # print(numbers[7])

# # print(numbers[-1])
# # print(numbers[-2])
# # print(numbers[-3])
# # print(numbers[-4])
# # print(numbers[-5])
# # print(numbers[-6])
# # print(numbers[-7])
# # print(numbers[-8])

# # numbers = [10,20,30,40]
# # numbers[1] = 25
# # numbers.insert(0,15)
# # print(numbers)
# # numbers[3] = 35
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.remove(80)
# # print(numbers)

# # numbers.pop(1)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.pop(0)
# # numbers.pop(1)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.append(15)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # del numbers[2]
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.clear()
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.sort(reverse=True)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # count = numbers.count(40)
# # print(f"Count of 40: {count}")

# # count = numbers.count(100)
# # print(f"count of 100: {count}")

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.reverse()
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers_copy = numbers.copy()
# # print(numbers_copy)

# # numbers = [10,20,30,40,50,60,70,80]
# # index = numbers.index(50)
# # print(f"Index of 50: {index}")

# # numbers = [10,20,30,40,50,60,70,80]
# # print(numbers.count(10))
# # print(numbers.index(60))

# # numbers.sort()
# # print(numbers)

# # numbers.sort(reverse=True)
# # print(numbers)

# # numbers = [10,20,30,40,50,60,70,80]
# # numbers.reverse()
# # print(numbers)

# # # list_name = [start:end:step]

# # numbers = [10,20,30,40,50,60,70,80]
# # print(numbers [1:4])
# # print(numbers [ :3])
# # print(numbers [2:])
# # print(numbers[ : ])
# # print(numbers[::2])
# # print(numbers[:: -1])
# # print(numbers[1:4:6])

# # numbers = [1,2,3,4,5]
# # result = [num for num in numbers if num % 2 == 0]
# # print(result)

# # numbers = [10,20,30,40,50]
# # result = [num for num in numbers if num > 40]
# # print(result)

# # numbers = [1,2,3,4,5,6]
# # result = [num for num in numbers if num % 2 != 0]
# # print(result)

# # numbers = []

# # # insert elements
# # numbers.append(10)
# # numbers.append(20)
# # numbers.append(30)

# # # Access
# # print("List:", numbers)
# # print("First element:", numbers[0])

# # # update
# # numbers[1] = 25
# # print("Updated List:", numbers)

# # # delete
# # numbers.remove(20)
# # print("After Deletion:", numbers)

# # # length
# # print("Length of List:", len(numbers))

# # print("Final List:", numbers)

# numbers = tuple([10, 20, 30, 40, 50])
# print(numbers)

# numbers =()
# print(numbers)

# numbers = tuple()
# print(numbers)

# a = (10,)
# print(type(a))

# a= (10)
# print(type(a))

# numbers = (10, 20, 30, 40, 50)
# numbers = numbers + (60, 70,80,90)
# print(numbers)

# numbers = (10,20,30,40)
# result = list(numbers)
# result.append(50)

# numbers = tuple(result)
# print(numbers)

# numbers = (10,20,30,40,50)
# print(numbers[0])
# print(numbers[2])
# print(numbers[-1])

# numbers = (10,20,30,40,50)
# del numbers[2]
# print(numbers)  # This will raise an error since 'numbers' is deleted

# numbers = (10,20,30,40,50)  
# numbers = ()
# print(numbers)  # This will print an empty tuple

# numbers = (10,20,30,40,50)
# print(numbers.count(30))
# print(numbers.index(20))
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))

# student = ("sai", 25, "HYDERBAD")
# name, age , city = student
# print(name)
# print(age)
# print(city)

# numbers = (10,20,30,40,50)

# print("original tuple:", numbers)
# print("First element:",numbers[0])
# print("Length:", len(numbers))
# print("Count:", numbers.count(10))
# print("index:", numbers.index(30))
# print("Reverse:", numbers[::-1])

# numbers = {10,20,30,10,30}
# print(numbers)

# numbers = set([10,20,30])
# print(numbers)

# numbers = set()
# print(numbers)

# a = set()
# print(a)

# numbers = {10,20,30}
# numbers.add(40)
# print(numbers)

# numbers = {10,20}
# numbers.update([30,40,50])
# print(numbers)

# numbers = {10,20,30}

# # print(numbers[0]) # TypeError

# numbers = {10,20,30}
# for num in numbers:
#     print(num)

# numbers = {10,20,30,40}
# numbers.remove(40)
# print(numbers)

# numbers = {10,20,30,40}
# numbers.discard(100)
# print(numbers)

# numbers = {10,20,30}
# numbers.pop()
# print(numbers)

# numbers = {10,20,30}
# numbers.clear()
# print(numbers)

# a = {10,20,30,40}
# b = {30,40,50,60}

# print(a.union(b))

# print(a|b)
# print(a.intersection(b))

# print(a & b)
# print(a.difference(b))

# print(a - b)

# print(a.symmetric_difference(b))
# print(a^b)

# a = [1,2,3,]
# a[1] = 5
# print(a)

# a = (1,2,3)
# a[1] = 5
# print(a)

# numbers = [10,20,80,30,40,50]
# unique_numbers = sorted(set(numbers))
# print(unique_numbers[-3])


# numbers = [10,30,20,40,50,30,40]
# result = set(numbers)
# print(result)


# student = {
#      "name" : "sai",
#      "age"  : 25,
#      "city" : "Hyd"
#     }
# print(student)

# student = {}

# student["name"] = "sai"
# student["age"] = "22"
# student["city"] = "HYD"
# print(student)


# student = {
#     "name" : "SAI",
#     "age"  : 25
# }
# print(student["name"])
# print(student["age"])
# print(student.get("salary"))
# print(student.get("city"))


# student = {
#     "name" : "sai",
#     "age"  : "20"
# }
# # student["age"] = 25
# # print(student)

# student.update = ({"city" : "hyd", "age" : 25})
# print(student)

# student = {
#     "name" : "sai",
#     "age" : 25,
#     "city" : "hyd"
# }
# # student.pop("age")
# # print(student)

# # student.popitem()
# # print(student)

# # del student["name"]

# # student.clear()
# # print(student)

# print(student.keys())
# print(student.values())
# print(student.items())


# student = {
#     "name" : "sai",
#     "age" :25
#     }
# # student.pop("age")
# # print(student)

# # del student["name"]
# # print(student)

# # student.clear()
# # print(student)

# student.update({"city" : "Hyd", "age" : 25})
# print(student)

# student = {"name" : "sai", "age" : 25}

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for key,values in student.items():
#     print(key,values)

# student = {
#     "name" : "sai",
#     "age" : 25,
#     "city" : "Hyd"
# }

# print(student.keys())
# print(student.values())
# print(student.items())

# students = {
#     "student1" : {
#         "name" : "sai",
#         "age" : "24"
#     },
#     "student2" : {
#         "name" : "Ravi",
#         "age" : 25
#     }
# }

# print(students["student1"]["name"])
# print(students["student2"]["age"])


# numbers = [1,2,3,4,5]

# result = {num:num * num for num in numbers}
# print(result)

# name = "python"
# print(name)

# name = 'python'
# name = "python"
# name = """python"""
# name = str()
# print(name)

# name = "PYTHON"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:3])
# print(name[2:])
# print(name[::-1])

# name = "M" + name[1:]
# print(name)

# name = "python programming"

# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.replace("Java", "python"))
# print(name.split())

# data = "Python,SQL,AWS"
# result = data.split(",")
# print(result)

# data = ["python","sql","aws"]
# result = ",". join(data)
# print(result)

# name = "sai"
# age = 25
# print(f"my name is {name} and my age is {age}")
# print(f"my name is {name} and my age is {age}")

# name = "python is love"
# print(name[::-1])

# numbers = range(1,6)
# print(tuple(numbers))

# a = range(5)
# print(list(a))

# a = range(1,6)
# print(list(a))

# a = range(1, 20, 5)
# print(list(a))

# a = range(1, 10, 2)
# print(list(a))

# for i in range(1,6):
#     print(i)

# a = 100
# print(type(a))

# a = 20.5
# print(type(a))

# a = 10 + 5j
# print(type(a))
# print(a.real)
# print(a.imag)

# a = complex()
# print(a)

# a = True
# b = False
# print(a)
# print(b)
# print(type(a))

# a = bool()
# print(a)

# age = 25
# # result = age >= 18
# result = age<= 18
# print(result)

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not b)

# a = None 
# print(type(a))

# def student():
#     pass
# result = student()
# print(result)

# name = None
# if name is None:
#     print("No name available")

# numbers = frozenset([10, 20, 30, 10])
# print(numbers)

# numbers = frozenset()
# print(numbers)

# a = frozenset([10,20,30,50])
# b = frozenset([20,30,10,40,70])

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# data = bytes()
# print(data)

# data = b"python"
# print(data)
# print(type(data))

# data = b"ABC"
# print(data[0])
# print(data[1])
# print(data[2])

# name = "Python"
# result = name.encode("utf-8")
# print(result)

# data = b'python'
# result = data.decode("utf-8")
# print(result)

# data = bytearray([65,66,67])
# print(data)

# data = bytearray()
# print(data)

# data = bytearray(b"ABC")
# data[0] = 90
# print(data)

# data = bytearray(b"python")
# result = memoryview(data)
# print(result)
# print(result[0])

# data = memoryview(b"")
# print(data)

# data = bytearray(b"ABC")
# view = memoryview(data)
# view[0] = 90
# print(data)

# a = (10,20,[30,40])
# a[2].append(50)
# print(a)

# a = [10,20,10,30,20,40]
# result  = tuple(a)
# print(result)

# a = (10,20,30,50,10,20)
# result = list(a)
# print(result)

# a = [10,20,30,40,20,10]
# result = set(a)
# print(result)

# a = "programming"
# result = list(a)
# print(result)

# a = [("name", "sai"),("age",25)]
# result = dict(a)
# print(result)

# a = (10,20,[30,40])
# a[2].append(50)
# print(a)

# remove duplicates from list
# a = [10,20,30,20,20,10,50]
# result = list(set(a))
# print(result)

# find even numbers
# numbers = [1,2,3,4,5]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# find the second largest number
# numbers = [10,20,30,40,50,60,80]
# unique_numbers = sorted(set(numbers))
# print(unique_numbers[-2])

# # merge two dictinories
# a = {"name" : "sai", "age" : 25}
# b = {"city" : "HYD" }
# result = {**a,**b}
# print(result)

# reverse list 
# numbers = (1,2,3,4,5)
# print(numbers[::-1])

# # find maximum and minimum
# numbers = [10,20,30,40,50]
# result1 = max(numbers)
# result2 = min(numbers)
# print(result1)
# print(result2)

# find common elements between two lists
# a = [10,20,30,40]
# b = [50,60,80,10]
# result = list(set(a) & set(b))
# print(result)

# count frequency of elements
# numbers = [1,2,3,4,5,6,7,8]
# frequency = {}
# for num in numbers:
#     frequency[num] = frequency.get(num,0)+1
# print(frequency)