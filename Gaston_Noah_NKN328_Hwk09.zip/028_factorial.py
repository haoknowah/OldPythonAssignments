def fact(num):
    '''
method fact continually multiplies numbers to create factorial until x reaches num
returns factor which is factorial
    '''
    try:
        x=1
        factor=1
        while x<=num:
            factor=factor*x
            x += 1
        return factor

    except:
        print("Error1")
def getN():
    '''
method getN gets an integer from user and then sees if it is actually an integer
returns num which is integer entered
    '''
    try:
        cont=True
        while cont==True:
            num=int(input("Enter a positive integer: "))
            if num != int(num):
                print("not an integer")
            else:
                cont=False
                return num
    except:
        print("Error2.")
if __name__ == "__main__":
    '''
calls the functions defined above
prints factorial
going to later add this method as a template for mains in a utility folder
    '''
    print(__name__)
    try:
        cont=True
        while cont==True:
            num=getN()
            factor=fact(num)
            print(factor)
            end=input("Continue? y or n ")
            if end.lower()=="n":
                cont=False
    except:
        print("Error.")
