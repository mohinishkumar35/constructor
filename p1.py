# class Student:
#     x=10
#     y=30
#     def __init__(self):
#         print("This is from Constructor")
        
#     def display():
#         print("This is from display")
# obj=Student
# print(obj.x)
# obj.display()

#-----------------------------------------------------------------

# class Student:
#     x=10
#     y=30
#     def __init__(self):
#         print("id(self)")
#     @staticmethod
#     def display():
#         print("This is from display")
# obj1=Student()
# print(id(obj1))
# obj2=Student()
# print(id(obj2))

#-----------------------------------------------------------------

class Student:

    def __init__(self,x):
        print("Mohit")
    def __init__(self,x,y):
        print("Cybrom")
    def __init__(self,x,y,z):
        print("Coaching")
obj=Student(10,20,30)