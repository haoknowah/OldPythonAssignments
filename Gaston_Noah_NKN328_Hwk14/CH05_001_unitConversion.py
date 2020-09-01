def TEST_LengthConversions():
    ## Convert units of length.
    '''
@param FootConvertDict=dictionary for converting units
prints the converted unit
    '''
    FootConvertDict = PopDict("Units.txt")
    DisplayPromptChoices(FootConvertDict)
    sFrom, sTo, fLength = GetInput()
    fConversion = fLength * FootConvertDict[sFrom] / FootConvertDict[sTo]
    print("Length in {0}: {1:,.4f}".format(sTo, fConversion))


def PopDict(psFileName):
    '''
PopDict=creates and fills a dictionary
@param RetDict=returned dictionary
returns newly created and filled dictionary
    '''
    ofIN = open(psFileName, 'r')
    RetDict = {}
    for sLine in ofIN:
        vKeyVal = sLine.split(',')
        RetDict[vKeyVal[0]] = eval(vKeyVal[1])
    return RetDict

def DisplayPromptChoices(psFootConvertDict):
    '''
DisplayPromptChoices=shows what unit conversions are availlable
@param iOut=shows what each unit is in feet
prints the number of feet per input unit
    '''
    print("UNITS OF LENGTH")
    iOut = 0
    for sKey in psFootConvertDict:
        print((sKey + '\t').expandtabs(12), end="")
        iOut += 1
        if iOut % 3 == 0:
            print()
    print()
    
def GetInput():
    '''
GetInput=gets the unit types and length
@param sFrom=unit being converted from
@param sTo=unit being converted to
@param fLength=length in initial unit
returns sFrom, sTo, and fLength
    '''
    sFrom = input("Units to Convert From: ")
    sTo = input("Units to convert to: ")
    fLength = float(input("Enter length in " + sFrom + ": "))
    return sFrom, sTo, fLength
         
TEST_LengthConversions()
