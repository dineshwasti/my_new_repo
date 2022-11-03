
#to read from  a txt file in python
myfile=open("pythondemo.txt")
print(myfile.read())
#we have to close the file explicitly in this case
#so also we can use WITH process to open the file
with open("pythondemo.txt") as my_file:
    print(my_file.read())
#here close function is implicitly used by the with function itself so close function  is not necessary




