a = "A"
for i in range(26):
    name = "./inout/" + a + ".txt"
    f = open(name, 'x')
    a = chr(ord(a)+1)