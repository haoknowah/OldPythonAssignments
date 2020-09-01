def countFunction(words):
    '''
method countFunction counts number of times a substring appears in a given string
returns number of times the substring appeared
    '''
    try:
        find=input("Type a letter or set of letters to find: ")
        leng=len(find)
        x=0
        y=leng
        times=0
        while y<=len(words):
            check = words[x:y]
            if check == find:
                times += 1
            x += 1
            y += 1
        return times
    except:
        print("Loading...")
if __name__ == "__main__":
    '''
@ param words=input string
@ param x=decides whether or not to restart
prints times substring was repeated
    '''
    print(__name__)
    try:
        cont=True
        while cont == True:
            words=input("Type some words here: ")
            print("The given substring occurs ",countFunction(words), " times.",sep="")
            x=input("Type end to end or anything else to restart: ")
            if x.lower() == "end":
                break
    except:
        print("_____")
        
