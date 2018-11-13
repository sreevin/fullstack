# myfile=open("hello.txt","w")
# myfile.write("ICTA full stack class")
# myfile.close()
# print("File generated successfully")

myfile=open("hello.txt","r")
s=myfile.read()
print(s)
myfile.close()