try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def changeColor():
    '''
changes color of text in button and what it says
    '''
    try:
        if box["fg"]=="blue":
            box["fg"]="black"
            box["text"]="Change text from black to blue."
        else:
            box["fg"]="blue"
            box["text"]="Change text from blue to black."
    except:
        print("Unhandled exception in changeColor.")
'''
creates a window with a color and word changing button
@param window=object of Tk
@param box=widget object
'''
try:
    window=Tk()
    window.title("Change Colors")
    global box
    box=Button(window, text="Change text from blue to black.", bg="red", fg="blue", command=changeColor)
    box.grid(padx=50, pady=15)
    window.mainloop()
except:
    print("Unhandled exception.")
