try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def changeSalutation():
    '''
changes text in button
    '''
    try:
        if box["text"]==" Hello ":
            box["text"]="Goodbye"
        else:
            box["text"]=" Hello "
    except:
        print("Unhandled exception in changeSalutation.")
'''
creates a window with text changing button
@param window=object of Tk
@param box=widget object
'''
try:
    window=Tk()
    window.title("Change Salutation")
    global box
    box=Button(window, text=" Hello ", width=7, bg="black", fg="red", command=changeSalutation)
    box.grid(padx=50, pady=15)
    window.mainloop()
except:
    print("Unhandled exception.")
