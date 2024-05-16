#create a student class that that takes name and marks of three subjects as arguments in the constructor.
#Then create a method to print the average.

'''class student:
    def __init__(self, name , subject_1, subject_2, subject_3):
        self.name = name
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3

    def avg(self):
        average = ((self.subject_1+self.subject_2+self.subject_3)/3)
        print(average)
        

s1 = student("omar", 98, 67, 83)

print(s1.name)

s1.avg()'''

#create an account class with 2 attributes - balance and account no. 
#create methods for debit, credit and printing the balance. 

'''class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, debitAmount):
        self.balance -= debitAmount
        print("an ammount of", debitAmount, "has been debited from account no. ", self.account_no)


    def credit(self, creditAmount):
        self.balance += creditAmount
        print("an ammount of", creditAmount, "has been credited to account no. ", self.account_no)

    def balanceCheck(self):
        print("your balance is", self.balance) 

a1 = Account(10000, 1505)

a1.debit(2500)
a1.credit(100)
a1.balanceCheck()
a = "hello"'''



#make a student management system. 

'''class Student:
    school = "code acad"
    def __init__(self, name ,age , grade, score_card):
        self.name= name 
        self.age = age 
        self.grade = grade
        self.score_card = score_card

    def avg(self):
        av_g = 0
        for i in self.grade:'''

'''class Sports:
    outdoor = True

    def __init__(self, sports_name, sports_team):
        self.sports_name = sports_name
        self.sports_team = sports_team

    #### Do not change before this
    def print_info(self):
        if self.sports_name == "Golf" and self.sports_team == "America":
            print("Golf - America")
        else:
            print("-")
        
s1 = Sports("hello", "America")
s1.print_info()           '''


'''class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, number):
        newReal = self.real + number.real
        newImg = self.img + number.img
        return Complex(newReal, newImg)
    def __sub__(self, number):
        newReal = self.real - number.real
        newImg = self.img - number.img
        return Complex(newReal, newImg)

c1 = Complex(3,4)
c2 = Complex(5,6)
c1.show_number()

c2.show_number()
             
c3 = c1+ c2

c3.show_number()

c4 = c3 - c1

c4.show_number()'''

#define a Circle class to create a circle with radius r using the constructor.
#define an Area() method of the class which calculates the area of circle. 
#define a parimeter() method of the class which allows you to claculate the paremeter of circle. 

'''class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius**2
    def parimeter(self):
        return 2*(22/7)*self.radius

c1 = Circle(30)

print(c1.Area())
print(c1.parimeter())'''

'''class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role: ", self.role)
        print("department: ", self.department)
        print("salary: ", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("site engineer", "civil", 25000)

            
a1 = Employee("accountant", "finance", 50000)
a1.showDetails()

a2 = Engineer("omar", 24)


print(a2.salary)'''

#create a class called order which stores item & its price. 
#use dunder function __get__() to convey that:
# order1 > order2 if price of order 1 is greater than price of order 2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self,odr2):
        return self.price > odr2.price
           
odr1 = Order("laptop", 15000)
odr2 = Order("monitor", 10000)

print (odr1 < odr2)


