#Var 1
#print('I help you to find a minimum of your three numbers')
#a=int(input("a="))
#b=int(input("b="))
#c=int(input("c="))

#if a < b < c:
#    print(a)
#elif b < a < c:
#    print(b)
#elif c < a < b:
#    print(c)
#input("Success!")

#Var 2
print('I help you to find a minimum of your three numbers')
while True:
    x=int(input("x="))
    y=int(input("y="))
    z=int(input("z="))
    a = [x, y, z]
    i = 1
    result = x
    while i < len(a):
        if result > a[i]:
            result = a[i]
        i += 1
    print(result)
