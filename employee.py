class Employee:
   def  __init__(self,a,b,c,d):
        self.name=a
        self.emcode=b
        self.salary=c
        self.age=d
   def printData(self):
        print("Name=" ,self.name)
        print("emcode=" ,self.emcode)
        print("Salary=",self.salary)
        print("age"=,self.age)
    

u=Employee("Sreevin","ABC123",50000,22)
v=Employee("akhil","ABC124",40000,23)
w=Employee("anoop","ABC125",30000,24)
x=Employee("gokul","ABC126",20000,25)
u.printData()
