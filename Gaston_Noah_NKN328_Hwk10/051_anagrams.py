def getLetters(string):
    '''
getLetters(string)=removes any characters from the string that aren't letters
by going through each one individually
@param string=string being checked for letters
@param sRet=new string being returned with just letters
returns sRet or string of just letters
    '''
    try:
        string=str(string)
        sRet = ""
        for char in string:
            if char.isalpha():
                sRet += char
        return sRet
    except:
        print("Subfunction error")
def areAnagrams(string1,string2):
    '''
areAnagrams(string1, string2)=compares two strings to see if they are anagrams
by first using getLetters to remove all nonletters from the strings and then
sorting them to check if their values are the same
@param string1=first input string
@param string2=second input string
@param ret=whether or not the strings are anagrams
returns ret which is boolean of whether or not strings are anagrams
    '''
    try:
        string1=getLetters(string1)
        string2=getLetters(string2)
        string1.lower()
        string1 = "".join(sorted(string1))
        string2.lower()
        string2="".join(sorted(string2))
        ret=False
        if string1 == string2:
            ret = True
        return ret
    except:
        print("Error.")
if __name__ =="__main__":
    print(__name__)
    '''
main function that tests areAnagrams()
@param ana=returned boolean saying whether or not strings are anagrams
@param cont=determines if program repeats
@param end= user input to change status of cont
    '''
    try:
        cont=True
        while cont==True:
            string1=input("Type a word or phrase here: ")
            string2=input("Type another word or phrase here: ")
            ana=areAnagrams(string1, string2)
            if ana == True:
                print("They are anagrams.")
            else:
                print("They are not anagrams.")
            end=input("Continue? y or n ")
            if end.lower()=="n":
                cont=False
    except:
        print("Error.")
