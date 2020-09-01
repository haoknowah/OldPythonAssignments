def soundexSystem():
    '''
soundexSystem()=changes word into series of numbers
@param word=word input
@param code=word in soundex
print word in soundex
    '''
    try:
        word=input("Enter a word: ")
        code=word[0]
        word=word[1:]
        for ch in word:
            if ch == "b" or ch== "f" or ch == "p" or ch == "v":
                add="1"
                code = code + add
            elif ch == "c" or ch == "g" or ch == "j" or ch == "k" or ch == "q" or ch == "s" or ch == "x" or ch == "z":
                add="2"
                code = code + add
            elif ch == "d" or ch == "t":
                add="3"
                code = code + add
            elif ch == "l":
                add="4"
                code = code + add
            elif ch == "m" or ch == "n":
                add="5"
                code = code + add
            elif ch == "r":
                add="6"
                code = code + add
        print("The encoded word is ", code)
    except:
        print("Error")
if __name__ == "__main__":
    print(__name__)
    soundexSystem()
