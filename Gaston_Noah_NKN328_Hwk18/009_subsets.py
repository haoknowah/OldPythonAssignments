def Accum_Coeff(pnNum):
    '''
Accum_Coeff()=compiles a list of the coefficients
@param pnNum=input number
@param RetLst=list to be returned with the coefficients
@param r=cycles through the numbers in pnNum
returns the list with the coefficients
    '''
    try:
        RetLst = []
        for r in range(0, pnNum + 1):
            RetLst.append(Gen_Coeff(pnNum, r))
        return RetLst
    except:
        print("Unhandled exception.")
def Gen_Coeff(n, r):
    '''
Gen_Coeff()=finds the coefficients of the input number
@param n=input number
@param r=number being checked
returns a coefficient (not sure how this works but it does)
    '''
    try:
        if (n == 0) or (r == 0) or (n == r):
            return 1
        else:
            return Gen_Coeff(n - 1, r - 1) + Gen_Coeff(n - 1, r)
    except:
        print("Unhandled exception.")
if __name__ == "__main__":
    def TEST_AccumCoeff():
        '''
tests the AccumCoeff method
@param Num=input number
@param vCoeff=coefficients of input number
prints the coefficients of input number
flair:makes sure that only integers are put in
        '''
        try:
            cont=True
            while cont==True:
                Num = int(input("Input an integer here: "))
                vCoeff = Accum_Coeff(Num)
                print(vCoeff)
                end=input("Do you wish to continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except ValueError as exc:
                print(exc)
                end=input("Do you wish to continue? y or n ")
                if end.lower()=="n":
                    cont=False    
        except:
            print("Unhandled exception.")
    TEST_AccumCoeff()    
        
    

      

