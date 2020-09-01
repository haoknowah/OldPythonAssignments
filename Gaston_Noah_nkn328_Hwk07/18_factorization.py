def factorization():
    '''
finds the prime factors of a given number
@param x=number to be factored
@param f=divides number to find prime factors
@param lis=list to hold prime factors
used list to hold prime factors instead of creating them in a massive column
also used else because otherwise the break would always execute after the if statement
    '''
    try:
        x=int(input("Enter a number to factor: "))
        f=2
        lis=[]
        while True:
            if x>1:
                if x%f==0:
                    lis.append(f)
                    x=x/f
                else:
                    f+=1
            else:
                break
        print("The prime factors are ",lis)
    except:
        print("Why is this important again?")


if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                factorization()
        main()
    except:
        print("The lights are on but no one is home.")

