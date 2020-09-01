import pickle
from nation import Nation

def main():
    ## Display information about a country.
    try:
        while True:
            nationDict = pickle.load(open("nationDict.dat", "rb"))
            continent = input("Enter a continent: ")
            countries=[]
            for country in nationDict:
                if nationDict[country].getContinent()==continent:
                    countries.append(nationDict[country])
            if countries != []:
                countries.sort(key=lambda x: x.getPopulation()/x.getArea(), reverse=True)
                i=0
                while i<5:
                    print(countries[i].getName())
                    i +=1
                cont=input("Continue? y or n ")
                if cont.lower()=="n":
                    break
            else:
                print("Not a continent.")
    except AttributeError as exc:
        print(exc)
    except ValueError as exc:
        print(exc)
    except KeyError as exc:
        print(exc)
    except:
        print("Unhandled exception.")

main()

