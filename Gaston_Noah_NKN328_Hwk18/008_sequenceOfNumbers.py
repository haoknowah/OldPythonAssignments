def sequenceOfNumbers(m, n):
    '''
sequenceOfNumbers()=counts off numbers between m and n recursively
@param m=starting number
@param n=ending number
prints m
    '''
    try:
        if m==n:
            print(m)
        else:
            print(m)
            sequenceOfNumbers(m+1, n)
    except:
        print("Unhandled exception.")
if __name__=="__main__":
    def test_sequenceOfNumbers():
        '''
tests sequenceOfNumbers method
@param cont=determines if loop repeats
@param m=first input
@param n=second input
flair=ensures that n is greater than m
        '''
        try:
            cont=True
            while cont==True:
                try:
                    m=int(input("Type an integer: "))
                    while True:
                        n=int(input("Type another one: "))
                        if n<m:
                            print("Needs to be higher than first input.")
                        else:
                            break
                    sequenceOfNumbers(m, n)
                    end=input("Continue? y or n")
                    if end=="n":
                        cont=False
                except ValueError as exc:
                    print(exc)
                    end=input("Continue? y or n ")
                    if end=="n":
                        cont=False
        except:
            print("Unhandled exception.")
    test_sequenceOfNumbers()
