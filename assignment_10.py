#Q.1- Write a Python program to read n lines of a file

f=open('Output.txt','r')
f.seek(0)
n=int(input("Enter number of lines :-"))
print(f.readlines(n))
f.close

#Q.2- Write a Python program to count the frequency of words in a file.

f=open('Out.txt','r')
f.seek(0)
c=0
word=(input("Enter the word that needs to be searched :-"))
for i in f:
    words=i.split()
    for j in words:
        if(j==word):
            c=c+1
print(c)
f.close()

#Q.3- Write a Python program to copy the contents of a file to another file

with open('Vol-1.txt', 'r') as f1:
    with open('Vol-2.txt', 'a') as f2:
        for line in f1:
            f2.write(line)
f2=open('Vol-2.txt','r')
data=f2.read()
print(data)

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('Vol-1.txt', 'r+') as f1:
    with open('Vol-2.txt', 'r+') as f2:
        line1=f1.readlines()
        line2=f2.readlines()       
l=[]
for i in line1:
    for j in line2:
        l.append(i+j)
print(l)
           
#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

with open('Vol-1.txt', 'r+') as f:
    for i in range (0,10):
        num=input("Enter a random number :- ")
        f.writelines(num+'\n')
with open('Vol-1.txt', 'r') as f:
    l=f.readlines()
    l.sort()
with open('Vol-2.txt', 'r+') as f1:
    f1.writelines(l)
    data=f1.read()
    print(data)


