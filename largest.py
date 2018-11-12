num1=int(input("enter first no"))
num2=int(input("enter second no"))
num3=int(input("enter third no"))
if(num1>num2):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2>num3):
        print(num2)
    else:
        print(num3)