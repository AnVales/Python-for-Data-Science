# Q1: What is the result of the following operation 3+2*2?
print(3+2*2)

# Q2: What is the type of the following variable: a = True?
print(type(True))

# Q3: What is the result of the following operation int(3.2)?
print(int(3.2))

# Q4: Consider the string A = '1234567', what is the result of the following operation:
A='1234567'
print(A[1::2])

# Q5: Consider the string, what is the result of the following operation:
Name="Michael Jackson"
print(Name.find('el'))

# Q6: The variables A = '1' and B = '2', what is the result of the operation A+B?
A='1'
B='2'
print(A+B)

# Q7: Consider the variable F='You are wrong', convert the values in the varible F
# to uppercase?
F="You are wrong"
print(F.upper())

# Q8: Consider the tuple tuple1, what is the result of the following operation:
tuple1=("A","B","C" )
print(tuple1[-1])

# Q9:Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. 
# What is the result of the following operation A[1]:
A=((11,12),[21,22])
print(A[1])

# Q10: Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. 
# What is the result of the following operation A[0][1]:
A=((11,12),[21,22])
print(A[0][1])

# Q11:What is the result of the following operation ‘1,2,3,4’.split(‘,’)
print('1,2,3,4'.split(','))

# Q12:Concatenate the following lists A=[1,’a’] and B=[2,1,’d’]:
A=[1,'a']
B=[2,1,'d']
print(A+B)

# Q13: How do you cast the list ‘A’ to the set ‘a’?
a=set(A)

# Q14: Consider the Set: V={‘A’,’B’}, what is the result of V.add(‘C’)?
V={'A','B'}
V.add('C')
print(V)

# Q15: Consider the Set: V={‘A’,’B’,’C’ }, what is the result of V.add(‘C’)?
V={'A','B', 'C'}
V.add('C')
print(V)

# Q16: What is the output of the following lines of code:
x='Go'
if(x!='Go'):
    print('Stop')
else:
    print('Go' )
print('Mike')

# Q17: What is the output of the following lines of code:
x='Go'
if(x=='Go'):
    print('Go')
else:
    print('Stop' )
print('Mike')

# Q18: How many iterations are performed in the following loop?
for n in range(3):
    print(n)

# Q19: What does the following loop print?
for n in range(3):
    print(n+1)

# Q20: What is the output of the following few lines of code ?
A=['1', '2', '3']
for a in A:
    print(2*a)

# Q21: Consider the function add, what is the result of calling the following Add(‘1′,’1’) 
# (look closely at the return statement )
def Add(x,y):
    z=y+x
    return(y)
print(Add('1','1'))

# Q22: Consider the class Points, what are the data attributes:
class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x, 'y=',self.y)

# self.x self.y

# Q23: What is the result of running the following lines of code ?
class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def print_point(self):
        print('x=',self.x, 'y=',self.y)

p1=Points(1,2)
p1.print_point()

# Q24: What is the result of running the following lines of code ?
class Points(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def print_point(self):
        print('x=',self.x, 'y=',self.y)

p2=Points(1,2)
p2.x=2
p2.print_point()

# Q25:Consider the following line of code: with open(example1,”r”) as file1:
# What mode is the file object in?
# read

