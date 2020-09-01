def primeFactors():
    try:
        x=int(input("Enter a number to factor: "))
        prime=True
        count=2
        while count < x:
            if x%count!=0:
                count+=1
            else:
                prime=False
                break
        print("Is the input number ", x, " a prime number? ",prime, sep="")
    except:
        print("Error.")
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
'''
output:
Enter a number to factor: 73
Is the input number 73 a prime number? True
Continue? y or n n
>>>
'''
