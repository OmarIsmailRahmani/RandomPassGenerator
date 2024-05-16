# WAP to ask the user to enter names of their 3 favorite movies & store them in a list. 

'''movieList = []

movie1 = input("favorite movie1: ")
movie2 = input("fav movie2: ")
movie3 = input("fav movie3: ")

movieList.append(movie1)
movieList.append(movie2)
movieList.append(movie3)
print(type(movieList))

print(movieList)'''

'''movieList = []

movieList.append(input("1st movie: "))
movieList.append(input("2nd movie: "))
movieList.append(input("3rd movie: "))

print(movieList)'''

# WAP to check if a list contains a palidrome of elements. (Hint: use copy() method.)

'''list1 = [1 , 2 , 2 , 1]

list1_copy = list1.copy()
list1_copy.reverse()

if list1 == list1_copy:
    print("list1 contains a palidrome")
else:
    print("No pelidrome")'''

# WAP to count the number of students with the "A" grade in the following tupple. 
    # ["C" , "D" , "A" , "A" , "B" , "B" , "A"]

marks = ("C" , "D" , "A" , "A" , "B" , "B" , "A")    

print(marks.count("A"))

# store the above values in a list & sort them from "A" to "D".

markList = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]

markList.sort()

print(markList)



