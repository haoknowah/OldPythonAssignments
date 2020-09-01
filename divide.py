def divide():
    a=3
    b=4
    try:
        print (a/0)
    except ZeroDivisionError:
        print ("Can't divide by zero")
    print (a/b)
