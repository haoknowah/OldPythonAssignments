def palindrome():
    '''
palindrome()= finds if string is a palindrome or not
@param pal=input word
@param reverse=pal reversed 
    '''
    try:
        pal=input("Enter a word or phrase: ")
        pal.lower()
        reverse=""
        for ch in pal:
            if ch in " .?;:/,123456789":
                pal.replace(ch,"")
            reverse=ch+reverse
        if reverse == pal.lower():
            print("Is a palindrome.")
        else:
            print("not a palindrome.")
    except:
        print("Error.")
if __name__ == "__main__":
    print(__name__)
    palindrome()
