# Q1: Select the values of i that produces a True for the following: i!=0
# 1, -1, 100000000

# Q2: What is the output of the following:
x='a'
if(x!='a'):
    print("This is not a.") # "This is a."
else:
    print("This is a.")

# Q3: What is the output of the following lines of code:
A=[3,4,5]
for a in A:
    print(a)
# 3 4 5

# Q4: What is the output of the following lines of code:
x=3
y=1
while(y!=x):
    print(y)
    y=y+1
# 1, 2

# Q5: What is the value of c after the following block of code is run ?

a=1
def add(b):
    return a+b
c=add(10)
print(c)
# 11

# Q6: What is the value of c after the following block of code is run with proper numerical input?
def f(*x):
    return sum(x)
# The function is not valid.

# Q7: Using the Class Car in the lab, create a Car object with the following attributes:
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 

    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)

    def sell(self):
        self.owner_number=self.owner_number+1

make="Honda"
model="Accord"
color="blue"

make="BMW"
model="M3"
color="red"

car1 = Car("Honda","Accord","blue")
car2 = Car(make="Honda",model="Accord",color="blue")
car3 = Car(model="Accord",make="Honda",color="blue")
car1.car_info()
car2.car_info()
car3.car_info()

# Q8: From the lab, how would you change the data attribute owner_number ?
# Utilising the method sell().

# Q9: What is the output of the following few lines of code?
A = ['1','2','3']
for a in A:
    print(2*a)
# '11' '22' '33'

# Q10: Consider the function Delta, when will the function return a value of 1

def Delta(x):
    if x==0:
        y=1;
    else:
        y=0;
    return(y)
# When the input is 0.

# Q11: What is the correct way to sort the list 'B' using a method? The result should not return a new list, just change the list 'B'.
# B.sort()

# Q12: What are the keys of the following dictionary: {'a':1,'b':2}?
# a,b
