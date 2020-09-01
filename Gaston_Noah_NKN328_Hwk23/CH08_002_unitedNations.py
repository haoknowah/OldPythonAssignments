try:
    from tkinter import *
    import pickle
except ImportError as exc:
    print(exc)
def displayInfo(event):
    '''
displays info of nation in relevant entry boxes
@param nation=selected nation
@param cont/pop/areaVar=variable containing relevant information
    '''
    try:
        nation=nationsListBox.get(nationsListBox.curselection())
        contVar.set(nationsDict[nation]["cont"])
        popVar.set(nationsDict[nation]["popl"]*1000000)
        areaVar.set(nationsDict[nation]["area"])
        continentEntry["textvariable"]=contVar
        populationEntry["textvariable"]=popVar
        areaEntry["textvariable"]=areaVar
    except:
        print("Unhandled exception in displayInfo.")
try:
    '''
creates a window that lists nations of the UN and displays their info
@param infile=holds data from UNDict.dat
@param nationsDict=dictionary holding information of UNDict.dat
@param nations=alphabetized list containing names of nations
@param window=object of Tk
@param nationsList=variable holding nations for listbox
@param yscroll=scrollbar widget
@param nationsListBox=listbox widget displaying nations
@param continent, population, area=label widget for relevant info
@param continent/population/areaEntry=readonly widgets displaying relevant info
    '''
    infile=open("UNDict.dat", "rb")
    global nationsDict
    nationsDict=pickle.load(infile)
    infile.close()
    nations=[]
    for nation in nationsDict.keys():
        nations.append(nation)
    nations.sort()
    window=Tk()
    window.title("United Nations")
    yscroll=Scrollbar(window, orient=VERTICAL)
    yscroll.grid(row=0, column=1, rowspan=4, padx=(0,5), pady=0, sticky=NS)
    nationsList=StringVar()
    nationsListBox=Listbox(window, fg="red", listvariable=nationsList, yscrollcommand=yscroll.set)
    nationsListBox.grid(row=0, column=0, rowspan=4, padx=0, pady=0, sticky=W)
    nationsList.set(tuple(nations))
    continent=Label(window, fg="red", text="Continent:")
    continent.grid(row=0, column=2, padx=5, pady=5, sticky=E)
    continentEntry=Entry(window, state="readonly", fg="red")
    continentEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
    population=Label(window, fg="red", text="Population:")
    population.grid(row=1, column=2, padx=5, pady=5, sticky=E)
    populationEntry=Entry(window, fg="red", state="readonly")
    populationEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
    area=Label(window, fg="red", text="Area (sq. miles):")
    area.grid(row=2, column=2, padx=5, pady=5, sticky=E)
    areaEntry=Entry(window, fg="red", state="readonly")
    areaEntry.grid(row=2, column=3, padx=5, pady=5, sticky=W)
    contVar=StringVar()
    popVar=StringVar()
    areaVar=StringVar()
    nationsListBox.bind("<<ListboxSelect>>", displayInfo)
    window.mainloop()
except:
    print("Unhandled exception.")
