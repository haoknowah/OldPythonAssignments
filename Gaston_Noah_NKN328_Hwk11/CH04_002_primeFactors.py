def primeFactors():
    '''
primeFactors()=runs the factorization function, sorts it, and checks first and last numbers in the list from in
@param recycledGoods=returned list from factorization function that was reused
@param small=the smallest number in the given list
@param large=the biggest number in the factor list
prints the smallest and the largest numbers in the list
    '''
    try:
        recycledGoods = factorization()
        recycledGoods.sort()
        small=recycledGoods[0]
        large=recycledGoods[len(recycledGoods)-1]
        print("The smallest prime factor is ",small, " and the largest is "\
              ,large, sep="")
    except:
        print("Error.")
def factorization():
    '''
copied and pasted directly from homework 7
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
        return lis
    except:
        print("Why is this important again?")
if __name__ == "__main__":
    def test_primeFactors():
        '''
test_primeFactors()=tests the primeFactors() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                primeFactors()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error.")
    test_primeFactors()
