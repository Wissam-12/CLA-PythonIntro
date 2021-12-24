f = open('./inout/student_names.txt')
names = f.read()
print(names)

f = open('./inout/student_names.txt', 'w')
names = names + "\nDonno what\nTo add"
f.write(names)

f = open('./inout/student_names.txt', 'r')
namesnew = f.readlines()

n = int(input("Number of lines you want to read : "))
first = namesnew[:n]
print(n, "first lines")
print(first)
print(n, "last line")
last = namesnew[-n:]
print(last)

x = input("The name that you want to check whether it exists in the file : ")
print(x in names)
f.close()