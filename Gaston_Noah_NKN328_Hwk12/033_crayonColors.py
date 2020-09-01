def crayonColors():
    '''
crayonColors=checks the file with the 1990 crayon colors, removes the ones
listed in the file that were discontinued, and adds the ones listed in
the file that were added to production
@param original=file with the list of colors in 1990
@param removed=file with list of colors discontinued
@param added=file with list of colors added to production
@param final=new file with list of colors in production after 1990's
@param colorList=list holding all the colors from original
@param removeList=list of colors from removed to take from original
note:book says that there is an almond but there is no almond in the file and
the color Apricot was on both the original list and the list of colors added
so I added a bit to remove repeated colors
    '''
    try:
        original=open("Pre1990.txt", 'r')
        removed=open("Retired.txt", 'r')
        added=open("Added.txt", 'r')
        final=open("final.txt", 'w')
        colorList=[line.rstrip() for line in original]
        for line in added:
            if colorList.count(line.rstrip())==0:
                colorList.append(line.rstrip())
        removeList=[line.rstrip() for line in removed]
        for color in colorList:
            for noncolor in removeList:
                if color == noncolor:
                    colorList.remove(color)
        colorList.sort()
        for sep in range(len(colorList)):
            colorList[sep]=colorList[sep] + "\n"
        final.writelines(colorList)
        original.close()
        removed.close()
        added.close()
        final.close()
    except:
        print("Error.")
if __name__ == "__main__":
    def test_crayonColors():
        '''
test_crayonColors()=tests the crayonColors() method
@param cont=boolean that determines if program repeats
        '''
        try:
            cont=True
            while cont==True:
                crayonColors()
                end=input("Continue? y or n ")
                if end.lower()=="n":
                    cont=False
        except:
            print("Error, test.")
    test_crayonColors()
