# Convert to pig latin
def GetVowelPos(psWord):
    '''
@param vowel=different vowels possible
@param psWord=word being converted
    '''
    try:
        vowel= "aeiou"
        return psWord in vowel
    except:
        print("Oink Oink!")
def pigLatin(psWord):
    '''
calls on GetVowelPos to help move letters for pig latin translation
    '''
    try:
        if not psWord.isalpha():
            print("Not letters.")
            return None
        psWord=psWord.lower()
        if GetVowelPos(psWord[0]):
            return psWord + "way"
        for let in range(1, len(psWord)):
            if psWord[let] in "aeiou":
                psWord=psWord[let:]+psWord[:let]+"ay"
                break
        return psWord
    except:
        print("Oink Oink.")
if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                print(pigLatin(input("Enter word to translate to pig latin: ")))
        main()
    except:
        print("The lights are on but nobody is home.")
