def verbalizeNumber(number):
    '''
verbalizeNumber(number)=displays the number in seperate pieces alonside what group they are a part of
@param digit=digits in input number
@param number=number inputed and being verbalized
@param start=digit that the slice starts at
@param end=digit after slice ends
@param numList=list to hold the input numbers as string so they can be reversed
@param part=element of list containing what group the numbers belong to
@ param word=list containing the individual number groups
@param hundred=holds hundred group
@param thousand=houlds thousands group
@param million=holds millions group
@param billion=you get the idea
etc.
prints the verbalized number, excluding any groups that were empty and cuts off the extra 0's from the left side of the numbers if applicable
    '''
    try:
        numList=[]
        for digit in number:
            numList.append(digit)
        numList.reverse()
        start=0
        end=3
        word = []
        while True:
            if end>len(numList):
                part=numList[start:]
                part.reverse()
                part="".join(part)
                word.append(part)
                break
            else:
                part=numList[start:end]
                part.reverse()
                part="".join(part)
                word.append(part)
                start += 3
                end += 3
        word.reverse()
        hundred=word[len(word)-1]
        hundred.lstrip("0")
        hundred=int(hundred)
        thousand=""
        million=""
        billion=""
        trillion=""
        quadrillion=""
        quintillion=""
        sextillion=""
        septillion=""
        if len(word) > 1:
            thousand=word[len(word)-2]
            thousand.lstrip("0")
        if len(word) > 2:
            million=word[len(word)-3]
            million.lstrip("0")
        if len(word) > 3:
            billion=word[len(word)-4]
            billion.lstrip("0")
        if len(word) > 4:
            trillion=word[len(word)-5]
            trillion.lstrip("0")
        if len(word) > 5:
            quadrillion=word[len(word)-6]
            quadrillion.lstrip("0")
        if len(word) > 6:
            quintillion=word[len(word)-7]
            quintilion.lstrip("0")
        if len(word) > 7:
            sextillion=word[len(word)-8]
            sextillion.lstrip("0")
        if len(word) > 8:
            septillion=word[len(word)-9]
            septillion.lstrip("0")
        if septillion!="":
            print(septillion.ljust(5), "septillion".ljust(20), sep="")
        if sextillion!="":
            print(sextillion.ljust(5), "sextillion".ljust(20), sep="")
        if quintillion!="":
            print(quintillion.ljust(5), "quintillion".ljust(20), sep="")
        if quadrillion!="":
            print(quadrillion.ljust(5), "quadrillion".ljust(20), sep="")
        if trillion!="":
            print(trillion.ljust(5), "trillion".ljust(20), sep="")
        if billion!="":
            print(billion.ljust(5), "billion".ljust(20), sep="")
        if million!="":
            print(million.ljust(5), "million".ljust(20), sep="")
        if thousand!="":
            print(thousand.ljust(5), "thousand".ljust(20), sep="")
        print(hundred)
    except:
        print("Error.")
if __name__ == "__main__":
    def test_verbalizeNumber():
        '''
test_verbalizeNumber()=tests the verbalizeNumber(number) method
@param cont=boolean that determines if the function repeats
@param number=input number of up to 27 digits
        '''
        try:
            cont=True
            while cont==True:
                number=int(input("Enter a positive number with up to 27 digits: "))
                number=str(number)
                if len(number) > 27:
                    print("Wrong answer.")
                else:
                    verbalizeNumber(number)
                    end=input("Continue? y or n ")
                    if end.lower()=="n":
                        cont=False
        except:
            print("Error, main.")
    test_verbalizeNumber()
