import pickle
import nation
def main():
    while True:
        createDictionayOfNations()
        cont=input("Go again? y or n ")
        if cont.lower()=="n":
            break
    
def createDictionayOfNations():
    '''
creates a dictionary of nations
@param odNation=dictionary of nations
returns the dictionary of nations
    '''
    try:
        odNation = {}
        for sLine in open("UN.txt", 'r'):
            vNationData = sLine.split(',')
            onCountry = nation.Nation()
            onCountry.setName(vNationData[0])
            onCountry.setContinent(vNationData[1])
            onCountry.setPopulation(float(vNationData[2]))
            onCountry.setArea(float(vNationData[3].rstrip()))
            odNation[onCountry.getName()] = onCountry
        # Save list as binary file that can be easily used in other programs
        pickle.dump(odNation, open("nationDict.dat", 'wb'))
        return odNation
    except:
        print("Unhandled exception.")
main()    
