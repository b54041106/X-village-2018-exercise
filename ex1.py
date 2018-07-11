##Function Basics
#Exercise1: MxM_multiplication
def h(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i, '*', j, '=', i* j, sep='', end='\t')
        print("\n")
h(4)

#Exercise2: swap
def q(a,b):
    tmp = a
    a = b
    b= tmp
    return (a,b)
a=1
b=2
(a,b)=q(a,b)
print (a,b)

#Exercise3: judge_big_lower
def ff(a, b):
    calculate = a-b
    if calculate < 0:
        result = 'a<b'
        return result
    elif calculate > 0:
        result = 'a>b'
        return result
    else:
        result='a=b'
        return result
   
a = 1
b = 2
y = ff(a, b)
print("result: ", y) 

##Scopes
#Exercise1: N^X
def maker(n):
    def action(x):  
        return (n)**(x) 
    return action

f = maker(9) 

print(f)
print(f(5)) 

##Arguments
#Exercise2: carbon_foot_Method1
def maker(n):
    def action(x): # Generate and return action
        return x * n # action retains N from enclosing scope return action
    return action

b= maker(0.03) # Pass 2 to argument N
print(b(100))
c= maker(0.24)
print(c(100))
s= maker(0.06)
print(s(100))

#Exercise2: carbon_foot_Method2
#way = carbon_foot('car')
def carbon_foot(way,km):
    if way=="bus":
        result = 0.03*km
        return result
    if way=="car":
        result = 0.24*km
        return result
    if way=="scooter":
        result = 0.06*km
        return result


way = 'car'
km  = 100
Car= carbon_foot(way,km)
print('Car:',Car)


#Recursive Function
#exercise1:recursive_1
def f(n):
    print('n:',n) # Trace recursive levels
    if n==1:
        return 1 
    else:
        return f(n-1)*n

print('answer: ',f(10))

#exercise2: recursive_2 
def F(n):
    if (n==0):
        return 0
    if (n==1):
        return 1 
    else:
        return (F(n-1)+F(n-2))
n=20
print('answer: ',F(n-1))

