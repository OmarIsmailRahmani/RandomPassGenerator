import random
import string

len = 10

possible_char = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(possible_char) for i in range(len)]) #list comprehension 

print()
print("Your randomly password is: ", password)
print()



