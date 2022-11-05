"""
#to read from  a txt file in python
myfile=open("pythondemo.txt")
print(myfile.read())
#we have to close the file explicitly in this case
#so also we can use WITH process to open the file
with open("pythondemo.txt") as my_file:
    print(my_file.read())
#here close function is implicitly used by the with function itself so close function  is not necessary
#to write something in the file
"""
""""
with open("pythondemos.txt" , "w") as my_file:
    my_file.write("i am in love")
    print(my_file.read())
"""
#to append the file or to append the words or letter in the file we use a+ mode
#but the cursor also goes very below so while we apply the print method nothing is printed
#so we need to use the my_file.seek() method to make the cursor to the top
import os
with open("pythondemo.txt","a+")as my_file:
    if os.path.exists("pythondemo.txt"):
        my_file.write("\nhi dinesh")
        my_file.seek(0)
        print(my_file.read())





