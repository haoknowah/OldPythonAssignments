def quadraticEquation():
    '''
quadraticEquation()=solves quadratic equation
prints solutions or nothing if there is none
    '''
    try:
        a=float(input("Enter a value for a: "))
        b=float(input("Enter a value for b: "))
        c=float(input("Enter a value for c: "))
        if a!=0:
            if (b**2-4*a*c)==0:
                print("The solution is ",(-b)/(2*a))
            else:
                x=(-b+(b**2-4*a*c)**0.5)/(2*a)
                y=(-b-(b**2-4*a*c)**0.5)/(2*a)
                print("The solutions are ",x, " and ",y)
    except:
        print("Error.")
if __name__ == "__main__":
    print(__name__)
    quadraticEquation()
