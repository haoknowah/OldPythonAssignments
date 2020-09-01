def inputValidation():
    '''
tells whether or not input letter is capitalized
@param LET=letter entered
made it seem like I was teaching a dog or small child
    '''
    try:
        LET=input("Type a single upper case letter: ")
        if LET.isupper() and len(LET)==1:
            print("Good boy.")
            return LET
        print("Follow directions and we can get through this.")
    except:
        print("No one writes letters anymore, guess the mailman's job is easier.")
if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                inputValidation()
        main()
    except:
        print("The lights are on but no one is home.")
        
