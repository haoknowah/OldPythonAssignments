import pickle
from nation import Nation

def main():
    ## Display information about a country.
    ##@param nationDict=dictionary of nations
    ##@param country=input country
    ##prints information about input country
    try:
        while True:
            nationDict = pickle.load(open("nationDict.dat", "rb"))
            country = input("Enter a country: ")
            if country in nationDict:
                print("Continent:", nationDict[country].getContinent())
                print("Population: {0:,.0f}".
                      format(1000000 * nationDict[country].getPopulation()))
                print("Area: {0:,.2f} square miles".
                      format(nationDict[country].getArea()))
                cont=input("Continue? y or n ")
                if cont.lower()=="n":
                    break
            else:
                print("Not a country.")
    except KeyError as exc:
        print(exc)
    except AttributeError as exc:
        print(exc)
    except ValueError as exc:
        print(exc)
    except:
        print("Unhandled exception.")
main()

