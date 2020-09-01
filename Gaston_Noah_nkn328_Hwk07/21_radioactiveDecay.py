def radioactiveDecay():
    '''
finds how long it will take for 100g of strontium 90 to reduce to 1g
@param m=mass of strontium
@param y=years
    '''
    try:
        m=float(100)
        y=0
        while m>= 1:
            y+=28
            m=m/2
        print("The decay time would be ", y, sep="", end=" years.")
    except:
        print("It breaks apart faster in a blender.")

if __name__ == "__main__":
    print(__name__)
    radioactiveDecay()
