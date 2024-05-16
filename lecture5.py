# print numbers from 1 to 100.

'''a = 1

while a <= 100 :
    print(a)
    a += 1'''

# print numbers from 100 to 1. 

'''a = 100

while a > 0:
    print(a)
    a -= 1'''

# print the multiplication table of number n.

'''n = int(input("what is the number: "))

p = 1

while p <= 20:
    print(n,"X", p, "=", p*n)
    p += 1'''


# print the elements of the following list using a loop:

'''list1 = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]

a = 0

while a < len(list1):
    print(list1[a])
    a += 1'''

# search for a number x in this tuple using loop:

'''tup = (1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100, 25)

x = int(input("what is x: "))

a = 0 

while a < len(tup):
    if tup[a] == x:
        print("!!Hurray",x, "found on index","[",a,"]!!")
    else:
        print("still finding...")    
    a += 1'''

# Print the elements of the following list using a for loop. 

'''list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in list1:
    print(num)'''

# Search for a number X in tuple using for loop. 

'''tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64)
x = int(input("what is the number you want to find: "))
idx= 0
for num in tup1:
    if num == x:
        print(num, "found at indx", idx) 
        #break # we can add "break" here if we want to stop the program after just finding first value.   
    idx +=1'''

#using for and range:
#print numbers from 1 to 100: 

'''for i in range(1,101):
    print(i)'''

#print numbers from 100 to 1: 

'''for i in range(100, 0, -1):
    print(i)'''

#print the multiplication table of the number n. 

'''n = int(input("which number: "))

for i in range(1,11):
    print(n, "X",i,"=", n*i)'''

# WAP to find the sum of first n numbers(using while):

'''n = int(input("what is n ? : "))


sum1 = 0
for i in range(1, n+1):
    #while i <= n:
    sum1 = i + sum1
print(sum1)'''

# WAP to find the factorial of first n number. (using for)

n = int(input("what is n ? : "))

fact1 = 1

for i in range(1, n+1):
    fact1 *= i
print(fact1)    