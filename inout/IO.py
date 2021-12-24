f = open('./inout/student_names.txt')
names = f.read()
print(names)

f = open('./inout/student_names.txt', 'w')
names = names + "\nDonno what\nTo add"
f.write(names)

f = open('./inout/student_names.txt', 'r')
names = f.readlines()
n = int(input("Number of lines you want to read : "))
first = names[:n]
print(first)
last = names[-n:]
print(last)

f.close()