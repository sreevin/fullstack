# def display():
#     print("Welcome to python")

# display()

# def add(x,y):
#     z=x+y
#     return z

# a=10
# b=20
# result=add(a,b)
# print(result)
    
def reverse(d):


    x=0
    while(d>0):
        y=d%10
        x=x*10+y
        d=d//10
    print(x)

t=int(input("Enter a number"))
reverse(t)