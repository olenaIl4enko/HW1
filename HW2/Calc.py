print('Welcome to calculator! Write "exit" for the end of work')
while True:
    s = input('What do you want to do? +, -, /, or *: ')
    if s == 'exit': break
    if s in ('+','-','*','/'):
        a = float(input("a="))
        b = float(input("b="))
        if s == '+':
            print("%.f" % (a+b))
        elif s == '*':
            print("%.f" % (a*b))
        elif s == '-':
            print("%.f" % (a-b))
        elif s == '/':
            if b != 0:
                print("%.2f" % (a/b))
            else:
                print('Division by zero')
    else:
                print('Invalid sign')
