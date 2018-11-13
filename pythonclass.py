class Students:
    
   def  __init__(self,x,y):
        self.name=x
        self.rollno=y


   def printData(self):
        print("Name=" ,self.name)
        print("Rollno=" ,self.rollno)

   def getAge(self,myAge):
        print('Age is'+str(myAge))
s=Students("Sreevin",5)

x=int(input("Enter the age"))

s.printData()
s.getAge(x)