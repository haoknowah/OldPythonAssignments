try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def displayName():
    '''
displays full name
@param name=full name
    '''
    try:
        name=firstInput.get()+" "+lastInput.get()
        nameVar.set(name)
        fullDisplay["textvariable"]=nameVar
    except:
        print("Unhandled exception in displayName.")
'''
creates window that takes first and last name, then gives full name
@param window=object of Tk
@param last/firstName=label widgets for appropriate types
@param last/firstInput=entry widgets for given types
@param display=button widget to get full name
@param fullName=label widget for fullDisplay
@param nameVar=string object for fullDisplay
@param fullDisplay=entry widget of type readonly that displays full name
'''
try:
    window=Tk()
    window.title("Full Name")
    lastName=Label(window, text="Last Name: ", fg="red")
    lastName.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky=E)
    lastInput=Entry(window, fg="red", width=20)
    lastInput.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky=W)
    firstName=Label(window, text="First Name: ", fg="red")
    firstName.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    firstInput=Entry(window, fg="red", width=20)
    firstInput.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    display=Button(window, text="Display full name", fg="red", bg="black", command=displayName)
    display.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    fullName=Label(window, text="Full Name: ", fg="red")
    fullName.grid(row=3, column=0, padx=5, pady=5)
    global nameVar
    nameVar=StringVar()
    fullDisplay=Entry(window, width=30, fg="red", state="readonly")
    fullDisplay.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    window.mainloop()
except:
    print("Unhandled exception.")
