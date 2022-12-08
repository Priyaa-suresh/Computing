'''class sample:
    def display():
        print("this is simple display statement")
    def display1():
        print("This is simple display statement 1")
a=sample         #object creation
a.display()
b=sample
b.display1()
a.display1()'''


'''class student:
    def display(self,a):
        print("empty function",a)
    def abc(self):
        print("abc function")
        
    def __init__(self,name):
        print("This is non paramterized constructor",name)
    def __init__(self,name):
        print("This is constructor",name)
    def show(self,name):
        print("Hello",name)
        
s1=student("pandi")
s2=student("oppps")
s1.display(1293)
s1.show("pandi")'''

'''class employee:
    def __init__(self,name):
        self.name=name
        print("Single parameter")
    def __init__(self,name,empno):
        self.empno=empno
        self.name=name
        print("Two parameter")
    def display(self):
        print("Id : %d \nName: %s "%(self.empno,self.name))
    def show(self):
        print(self.name)

emp1=employee("pandi")
emp1.show()
emp2=employee("selvi",102)'''

'''
class emp:
    id=1
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def dis(self):
        print("id: ",self.id)

emp1=emp(101,"pandi")
emp2=emp(102,"selvi")
emp1.dis()'''


#static and initial variable
'''class Employee:
    id=10
    name="pandi"
    count=0
    def __init__(self):
        #Employee.count=Employee.count+1
        self.count=self.count+1
    def display(self):
        print("Id: %d\nName: %s Count %d"%(self.id,self.name,self.count))
emp1=Employee()
emp1.display()
emp2=Employee()
emp2.display()
emp3=Employee()
emp3.display()
print(Employee.count)'''


#default constructor
class student:
    rollno=6
    name="pandi"
    def display(self):
        print("rollno: ",self.rollno)

s=student()
s.display()





