def maker1(n):   #n=4-->maker1(4)=b
    def action(x): #x=2 
        return x**n 
    return action

b= maker1(4) 
#print(b(2))


##印1~100奇數
a = 1
while a < 100:
    #print(a, end = ' ')
    a += 2
#print("end")
##比較
#a = 1
#while a < 100:    #loop 
#    print(a, end = ' ')
#print("end")= 1 1 1 1 1 1 1 ... 

#n = 100
#iterate = 0
#while iterate != n:
    #iterate += 1
    #print(iterate, end = ' ')

#n = 100
#iterate = 0
#total = 0
#while iterate != n:
#    iterate += 1    #inteate+1
#    total += iterate #interate+interate
#print(total)


#a = 5
#while a < 7:
#    if (a % 2 == 0):
#        print(a, "is even")
#    else:
#        print(a, "is odd")
#    a += 1
##frontward
#n = 0
#ans = 0
#while n <= 1000:
#    if (n % 11 == 0):
#        ans = n
#    n += 1
#print(ans)
##backward+break停止
#n = 1000
#flag = True
#while n > 0:
#    if (n % 11 == 0) and flag:
#        print("correct", n)
#        flag = False
#        break
#    print(n)
#    n -= 1

# def number(n):
import random
number=random.randint(1,100)  #電腦隨機選一個幸運號碼
#print(number)
guess_number=23
while guess_number!=number:
    if number<guess_number:  
        #print(guess_number)
        #print ("too small")
        guess_number-=1
    elif number>guess_number: 
        #print(guess_number)
        #print ("too large")
        guess_number+=1
    #print("Correct")

i = 1   # 被乘數
j = 1   # 乘數
while i <= 9:
    while j <= 9:
        #print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
    #print("")
    j = 1
    i += 1

n = 9
i = 1
j = 1
while i <= n:
    while j <= 5:
    #    print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
   # print("")
    j = 1
    i += 1

n = 9
i = 1
j = 1
while i <= n:
    while j <= n:
    #    print(i, j)
        j += 1
    #print("")
    j = 1
    i += 1

#i = 1
#j = 1
#while i <= 9:
#    while j <= 9:
#        if i*j < 50:
#           print(i, '*', j, '=', i* j, sep='', end='\t')
#        j += 1
#    print("")
#    j = 1
#    i += 1

i = 1
j = 1
while i <= 9:
    while j <= 9:
        if i*j > 50:
            break
        #print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
    #print('')
    j = 1
    i += 1

while i <= n:
    while j <= 5:
    #    print(i, '*', j, '=', i* j, sep='', end='\t')
        j += 1
   # print("")
    j = 1
    i += 1
