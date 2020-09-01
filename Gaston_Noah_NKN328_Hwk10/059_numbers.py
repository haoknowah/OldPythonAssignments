def numbers():
    '''
numbers()=sorts numbers by prime factor
@param f=factor being checked
@param lis=list of factors(no t at the end because list is a reserved word, so I
just took off a letter)
prints the sorted list
prime factor part was copy pasted and modified from my Hwk07
    '''
    try:
        numbers = [865, 1169, 1208, 1208, 1243, 329]
        print("Sorted by largest prime factor: ")
        anotherList=[]
        for num in numbers:
            f=2
            lis=[]
            x=num
            while True:
                if x>1:
                    if x%f==0:
                        lis.append(f)
                        x=x/f
                    else:
                        f+=1
                else:
                    break
            anotherList.append(lis)
        numbers=unfactor(anotherList)
        print(numbers)
    except:
        print("Reduce, reuse, recycle.")
def unfactor(anotherList):
    '''
Unfactor()=modified version of sumOfNumbers() from 058 to instead multiply factors
back together as integers and it sorts them by checking their sum as well
because the ones with the higher prime factor will also have the highest sums
due to how multiplication works(like how 3*2 is greater than 3+2)
@param anotherList=same as newList
    '''
    try:
        anotherList.sort(key=sum)
        finaList = []
        for subList in anotherList:
            fNum=1
            for digit in subList:
                digit = int(digit)
                fNum = fNum * digit
            finaList.append(fNum)
        return finaList
    except:
        print("Error, subfunction.")        
if __name__ == "__main__":
    print(__name__)
    try:
        cont=True
        while cont==True:
            numbers()
            end=input("Continue? y or n ")
            if end.lower()=="n":
                cont=False
    except:
        print("Error.")
