#Function that returns whether a char is in the alphabet or not
def Alpha(c):
    c = c.lower()
    if (ord(c) > 96 and ord(c) < 123):
        return True
    else: return False

#A function that removes all non alphabet chars from a string
def norm(s):
    res = ""
    for i in range(0,len(s)):
        if (Alpha(s[i]) == True):
            res = res + s[i]
    return res

#A function that verefies whether a string is palindrome or not
def palindrome(s):
    res = True
    for i in range(0, len(s)//2): #We could use the reverse function and check whether the reverse equals the original
        if (s[i] != s[- i - 1]):
            res = False
    return res

#A function that verefies whether a number is prime or not
def prime(n):
    v = True
    if(n < 0): n = -1 * n
    for i in range(2, n//2):
        if (n % i == 0): v = False
    if (n == 1) : v = False
    return v

#A function that checks whether a number is in a given range or not
def rg(n, a, b):
    if ((n <= b) and (n >= a)): v = True
    else: v= False
    return v

#A function that calculates the factorial of an integer
def fac(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res

#A function that reverses a string
def reverse(s):
    res = ""
    for i in range(1, len(s) + 1):
        res = res + s[-1 * i]
    return res

#A function that sums all numbers in a list
def sum(s):
    res = 0
    for i in range(len(s)):
        res = res + s[i]
    return res

#A function that finds the max between three numbers
def max(a, b, c):
    max = a
    if(b > a): max = b
    if(c > max): max = c
    return max

rep = "yes"
while(rep == "yes"):  
    #Menu
    print("Choose the number of the function you want to test : ")
    print("1. Palindrome function")
    print("2. Prime function")
    print("3. Range function")
    print("4. Factorial function")
    print("5. Reverse a string")
    print("6. The sum of all numbers in a list")
    print("7. The max of three numbers")

    choice = int(input("Your choice : "))

    if (choice == 1): 
        phrase = input(" Enter a sentence : \n")
        if (palindrome(norm(phrase))): print("It is palindrome")
        else: print("It's not palindrome")
    elif (choice == 2):
        num = int(input("Enter an integer: "))
        if(prime(num)): print("This number is prime")
        else:print("This number is not prime")
    elif (choice == 3):
        num = float(input("Enter an integer: "))
        a = float(input("Enter the start of the range: "))
        b = float(input("Enter the end of the range: "))
        if (a > b):
            print("The range is wrong (the start is bigger than the end).")
        else:
            if(rg(num, a, b)): print("This number is in the given range.")
            else: print("This number is not in the given range.")
    elif(choice == 4):
        num = int(input("Enter a positive integer: "))
        print("the factorial of this number is : ", fac(num))
    elif(choice == 5):
        s = input("Enter a sentence: ")
        print("The reverse of this sentence is : ", reverse(s))
    elif(choice == 6):
        num = int(input("How many numbers do u wanna put in the list ? "))
        ls = []
        for i in range(num):
            n = int(input("number : "))
            ls.append(n)
        print("The sum of its items is : ", sum(ls))
    elif(choice == 7):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the 3rd number: "))
        print("The max is : ", max(a, b, c))
    else: print("Wrong choice")

    rep = input("Do you wanna try again ? (yes/no)")
    rep = rep.lower()