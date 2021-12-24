list = []
for i in range(1, 299):
    if i%2 == 0 :
        list.append(i)

print("The length of the list is :", len(list))

print("The squared values of the list are:")
for i in list:
    print(i**2)

print( 57 in(list))