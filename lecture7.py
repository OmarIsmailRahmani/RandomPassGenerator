#create a new file "pracice.txt" using python. add the following data in it:

'''f = open("practice.txt", "w")

f.write("Hi everyone\nwe are learning file I/O\nusing Java\ni like programming in Java")

f.close

#WAF that replaces all accurrences of "Java" with "python" in the above line. 

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)    

with open("practice.txt", "w") as f:
    f.write(new_data)'''
    

#search if the word learning exists in the file or not? 
'''word = "learning"
with open("practice.txt", "r") as f:
    check_data = f.read()
    if check_data.find(word) != -1:
        print("found")
    else:
        print("no such word") '''


#put all that into a function. 

'''def check_word(word):
    with open("practice.txt", "r") as f:
        check_data = f.read()
        if check_data.find(word) != -1:
            print("found")
        else:
            print("no such word") 

check_word("learning")
check_word("hello")'''

#WAF to find in which line of the file does the word learning occur first. 
#print -1 if word not found. 

'''def check_line(word):
    with open("practice.txt", "r") as f:
        checkline = f.readline()
        if checkline.find(word) != -1:
            print("found in line 1")
        else:   
            checkline = f.readline()     
            if checkline.find(word) != -1:
                print("found in line 2")
            else:
                checkline = f.readline()     
                if checkline.find(word) != -1:
                    print("found in line 3")
                else:
                    print("no such word")

    
check_line("Python")'''
# ^above is what i did. 

#doing the same program with while loop. 

'''def check_line(word):
    data = True #it will be true untill there is some data. 
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("found in line number", line_no)
                return
               
            line_no += 1
    return -1                #for this to work we need to print the function. 
print(check_line("xlearning"))'''


#from a file containing numbers separated by comma, print the count of even numbers. 

'''with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)      

    num = ""
    count = 0
    for i in range(len(data)):
        if data[i] == "," :
            new_data = int(num)
            if new_data % 2 == 0:
                count += 1
            num = ""
        else:
            num += data[i]
#print (count)
    if num:
        new_data = int(num)
        if new_data % 2 == 0:
            count += 1

print(count)'''

#better way

'''with open("numbers.txt", "r") as f:
    data = f.read()
    list = data.split(",")
    #print(list)
    count = 0
    for i in list:
        i = int(i)
        if i % 2 == 0:
            count += 1
    print (count)'''



    
    

        