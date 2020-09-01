def militaryTime():
    '''
translates military time to standard time
@param miltime=military time
@param m=AM or PM
@param time=standard time
    '''
    try:
        miltime=int(input("Enter a military time 0000 to 2359: "))
        if miltime >=1200 and miltime<2400:
            m="PM"
            if miltime >=1300:
                time=miltime-1200
                time=str(time)
                time=time[:len(time)-2] + ":" + time[len(time):-2] + m
                print(time)
                return time
            time=str(miltime)
            time=time[:len(time)-2] + ":" + time[len(time)-2:] + m
            print(time)
            return time
        m="AM"
        miltime=str(miltime)
        time=miltime[:len(miltime)-2] + ":" + miltime[len(miltime)-2:] + m
        print(time)
    except:
        print("Error.")
if __name__ == "__main__":
    print(__name__)
    try:
        def main():
            while(True):
                militaryTime()
        main()
    except:
        print("The lights are on but no one is home.")
