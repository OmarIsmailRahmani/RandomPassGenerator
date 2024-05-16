#function definition 
'''def cal_sum(a , b): #parameters
    sum = a + b 
    print(sum)
    return


cal_sum(24 , 28)  #function call ; arguments

cal_sum(100, 13131)'''

# average of 3 numbers. 

'''def avg_3(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return

avg_3(4,5,6)

avg_3(20,10,2)

avg_3(1,2,3)

avg_3(98,97,95)'''

# WAF to print the lenght of a list. (list the parameter)

'''def len_list(a):
    print(len(a))
    return

list = [1, 2, 3, 4, 5, 6]

len_list(list)'''

# WAF to print the elements of a list in a single line. list is the parameter 

'''def print_inline(list):
    length = len(list)
    for i in list:
        print(i, end=" ")

    return
    
list1 = [1, 2, 3, 4, 5, 6]

print_inline(list1)
print()'''

#write the function to write the factorial of n: (n is the parameter)

'''def fact(a):
    fact0 = 1
    for i in range(1,a+1):
        fact0 *= i
    print(fact0)
    return

fact(5)

fact(3)'''

#WAF to convert Euro to inr. 

'''def euro_inr(euro):
    inr = euro* 89.90
    print(inr)
    return

euro_inr(400)'''


#HomeWork write a function which takes input from the user as an interger and checks wheather it is odd or even and print string that its "odd" or "even"

'''def odd_even(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
    return

odd_even(6)    '''

# Write a recursive function to calculate the sum of first n natural numbers.

'''def sum_first(n):
    if (n==0):
        return 0
    return sum_first(n-1) + n 

s = sum_first(5)

print(s)'''

#write a recursive function to print all elements in a list. 
#Hint: use list & index as parameters

'''def print_list(list, idx=0):
        if(idx == len(list)):
                return
        print(list[idx])
        print_list(list,idx+1)   


print_list([5,4,3,4,5])'''


def pani_me(i):
    for x in range(i):
        print("pani me gai")
    for b in range(i):
        print("chapak")
    return

'''def machli(i):
    
    for a in range(i):
        print(i,"machli")
    pani_me(i)   
    return'''

'''print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
machli(5)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")'''

i = 1 

while i > 0  :
    for a in range(i):
        print(i, "machli")
    pani_me(i)    
    i +=1




        

