try:
    from tkinter import *
except ImportError as exc:
    print(exc)
def abbreviation(event):
    '''
displays abbreviation of selected state
@param state=state curently selected
@param spot=where it is in the list
@param stateList=list holding data to be displayed on widget
    '''
    try:
        state=box.get(box.curselection())
        spot=stateList.index(state)
        stateList[spot]=stateList[spot]+" ("+states[spot][1]+")"
        stateBox.set(tuple(stateList))
    except:
        print("Unhandled exception in abbreviation.")
        
def createList():
    '''
exact same as in USpresidents except it doesn't sort
    '''
    try:
        infile=open("StatesANC.txt", 'r')
        states=[line.split()[0] for line in infile]
    except FileNotFoundError as exc:
        print(exc)
    finally:
        infile.close()
    try:
        return [x.split(",") for x in states]
    except:
        print("Unhandled exception in createList.")
global states
states=createList()
'''
creates a window with list of states and displays selected state's abbreviation
@param window=object of Tk
@param stateBox=list variable for window
@param box=widget object
@param stateList=list of states
'''
try:
    window=Tk()
    window.title("States")
    stateBox=StringVar()
    global box
    box=Listbox(window, width=20, height=40, fg="red", listvariable=stateBox)
    box.grid(padx=20, pady=25)
    stateList=[]
    for data in states:
        stateList.append(data[0])
    stateBox.set(tuple(stateList))
    box.bind("<<ListboxSelect>>", abbreviation)
    window.mainloop() 
except:
    print("Unhandled exception.")

