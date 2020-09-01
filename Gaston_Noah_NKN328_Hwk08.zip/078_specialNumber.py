def specialNumber():
    '''
specialNumber()=finds 4 digit number that that is same as it*4 backwards
@param num=number tested
print special number
    '''
    try:
        for num in range(1000, 9999):
            x=4*num
            parameter=""
            for ch in str(x):
                parameter=ch+parameter
            if str(num) == parameter:
                print(parameter, " is a special number.")
    except:
        print("Error")
if __name__ == "__main__":
    print(__name__)
    specialNumber()
