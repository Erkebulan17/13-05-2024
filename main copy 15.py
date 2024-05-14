# class Person:
#     def __init__(self, name):
#         self.name = name
#     def get_info  (self):
#         print("atu:",self.name)

# class Employee (Person):
#     def job(self,job_name):
#         print ("atu:",self.name,"jumusy:" ,job_name ) 
# emploeyee_obj = Employee("Yerkebulan")
# emploeyee_obj.job("programmer")   

class Color:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        print("Фигура түсі:", self.color)

class Triangle(Color):
    def __init__(self, color, side0="", side1="", side2=""):
        Color.__init__(self,color)
        self.side0 = side0
        self.side1 = side1
        self.side2 = side2
        self.kosindu = side0 + side1 + side2
    def get_perimeter(self):
        print("Perimeter:", self.kosindu)
obj1 = Triangle(color="Red", side0=7, side1=12, side2=9)
obj1.get_color()
obj1.get_perimeter()
