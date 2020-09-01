try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def usPresidents():
    '''
creates a window with list of presidents
@param window=object of Tk
@param presidentBox=list variable for window
@param box=widget object
@param presidents=list of presidents
    '''
    try:
        presidents=createList()
        window=Tk()
        window.title("USpresidents")
        presidentBox=StringVar()
        box=Listbox(window, width=20, height=5, fg="red", listvariable=presidentBox)
        box.grid(padx=20, pady=15)
        presidentBox.set(tuple(presidents))
        window.mainloop() 
    except:
        print("Unhandled exception.")
def createList():
    '''
creates and sorts a list of presidents from USpres.txt
@param infile=object holding data from text file
@param presidents=list containing data from file
returns sorted list
    '''
    try:
        infile=open("USpres.txt", 'r')
        presidents=[line.rstrip() for line in infile]
    except FileNotFoundError as exc:
        print(exc)
    finally:
        infile.close()
    try:
        presidents.sort(key=lambda name: name.split()[-1])
        return presidents
    except:
        print("Unhandled exception in createList.")
if __name__=="__main__":
    def test_usPresidents():
        '''
tests the usPresidents class
        '''
        try:
            usPresidents()
        except:
            print("Unhandled exception.")
    test_usPresidents()
