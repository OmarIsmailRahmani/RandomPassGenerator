# Store following word meanings in the python dictionary. 
# table : "a peice of furniture" , "list of facts & figures"
# cat: "a small animal"

'''dict1 = {
    "table" : ("a peice of furniture" , "list of facts & figures"),
    "cat" : "a small animal"
}

print(dict1["table"])'''

# You are given a list of subjects for students. Assume one classroom is required for one subject.
# How many classrooms are needed by all the students.

# "python" , "java" , "C++" , "python" , "javascript" , "java" , "python" , "java" , "C++" , "C"

'''subjects = {"python" , "java" , "C++" , "python" , "javascript" , "java" , "python" , "java" , "C++" , "C"} #sets

classrooms = len(subjects)

print("classrooms required :", classrooms)'''

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one.
# Use subject name as key and marks as value. 

'''subMarks = {}

subject = input("subject1: ")
marks = input("marks1: ")

subMarks.update({subject : marks})

subject = input("subject2: ")
marks = input("marks2: ")

subMarks.update({subject : marks})          #dont forget to put {}

subject = input("subject3: ")
marks = input("marks3: ")

subMarks.update({subject : marks})

print(subMarks)
print(subMarks.keys())'''


# Figure out a way to store 9 & 9.0 as separate values in set.
#(you can take help of built-in data types)

set1 = {9 , (9.0,)}

print(set1)


