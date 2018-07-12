#Exercise>>終極密碼
#def number(n):
import random
number=random.randint(1,100)  #電腦隨機選一個幸運號碼
print(number)
guess_number=23
while guess_number!=number:
    if number<guess_number:  
        print(guess_number)
        print ("too small")
        guess_number-=1
    elif number>guess_number: 
        print(guess_number)
        print ("too large")
        guess_number+=1
    print("Correct")

#Exercise>>9*9乘法表
i = 1   # 被乘數
j = 1   # 乘數
while i <= 9:
    while j <= 9:
        print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
    print("")
    j = 1
    i += 1

#Exercis>>nested while loop_Method1
n = 5
i = 1   # 被乘數
while i <= 5:
    j= 1
    while j <= n:
        print('*',sep='',end='\t')
        j += 1
    print('\n')
    n -=1
    i +=1
#Exercise>>nested while loop_Method2_square
n=5
a=99999
while a>0:
    a=n
    b=n
    while b>0:
        print("*",sep="\t",end=" ")
        b-=1
    print("\n")
    n-=1

n=5
a=0
while a<n:
    b=0
    while(b<n):
        if b<=(a-1):
            print(" ",end="")
        else:
            print("*",end="")
        b+=1
    print("\n")
    a+=1

for i in range(1, 5):
     for j in range(1, 5):
         if j>=i:
            print("*"),
     print("\n")

for i in range(1,7):
    for j in range(6-i):
        print(" ",end="")
    for j in range(1,1*i):
        print("*",end="")
    print("\n")

for i in range(1,7):
    for j in range(i-6):
        print(" ",end="")
    for j in range(1,1*i):
        print("*",end="")
    print("\n")

##Exercise>> for loop  50以內的質數  
num=[]
i=2
for i in range(2,50):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
