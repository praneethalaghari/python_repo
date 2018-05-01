# This is my first usage of classes in python

class student():

    default_name = "No_Name"  #This is class variable


   # def __init__(self,name,student_class,roll_no): #these are instance variables   # This is constructor called when ever and object is created
   #    self.name = name
   #     self.student_class = int(student_class)
   #     self.roll_no = int(roll_no)


    def __init__(self,name,student_class=5,roll_no=6): #these are instance variables   # This is constructor called when ever and object is created
        self.name = name                               # if we assign default values as above, it will take it take into consideration only if parameters are not passed while creating object and if parameters are passed it will take them in consideration
        self.student_class = int(student_class)
        self.roll_no = int(roll_no)



student_1 = student("Praneeth", 10, 1)   #These are instance variables
student_2 = student("Thanmai", 9, 2)
student_3 = student("Bhavana")
student_4 = student("Nivedita")

print(student_1.__dict__)  # This is the syntax to print all the contents in an whole object

student_1.name = "Praneeth Alaghari"

print(student_1.__dict__)
print(student_2.__dict__)
print(student_3.__dict__)
print(student_4.__dict__)

#DIFFERENCE BETWEEN CLASS AND INSTANCE VARIABLE

#default name is the class variable(GLOBAL)
#name is the instance variable(LOCAL)

#Class Objects which have common value can be assigned as class variable
#Class Objects which have varible value is to be assigned as instance variables

student.default_name="Name missing"  #As class variable share same variable the name will be assigned to both the objects
print (student_1.default_name)
print (student_2.default_name)

student.name="Praneeth A"   # As instance variables have individual copies name is no assigned to either student_1.name or student_2.name
print (student_1.name)
print (student_2.name)
