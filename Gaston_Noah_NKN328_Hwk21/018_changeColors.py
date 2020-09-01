try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def changeColor(event):
    '''
changes color of text and what it says
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
creates a window with color and text changing label
@param window=object of Tk
@param box=widget object
'''
try:
    window=Tk()
    window.title("Change Colors")
    global box
    box=Label(window, text="Change text from blue to black.", bg="red", fg="blue")
    box.grid(padx=50, pady=15)
    box.bind("<Button-1>", changeColor)
    window.mainloop()
except:
    print("Unhandled exception.")
