try:
    import students
except ImportError as exc:
    print(exc)
def main():
    while True:
        listOfStudents = obtainListOfStudents() # students and grades
        displayResults(listOfStudents)
        cont=input("Continue? y or n ")
        if cont.lower()=="n":
            break
def obtainListOfStudents():
    '''
lists students who recieved an A
@param listOfStudents=list containing students
@param name, midterm, final, category=student info
@param carryOn=decides if more students need to be input
returns list of students
    '''
    try:
        listOfStudents = []
        carryOn = 'Y'
        while carryOn == 'Y':
            name = input("Enter student's name: ")
            midterm = float(input("Enter student's grade on midterm exam: "))
            final = float(input("Enter student's grade on final exam: "))
            category = input("Enter category (LG or PF): ")
            if category.upper() == "LG":
                st = students.LGstudent(name, midterm, final)
            else:
                st = students.PFstudent(name, midterm, final)
            listOfStudents.append(st)
            carryOn = input("Do you want to continue (Y/N)? ")
            carryOn = carryOn.upper()
        return listOfStudents
    except:
        print("Unhandled exception.")
def displayResults(listOfStudents):
    listOfStudents.sort(key=lambda x: x.getName()) # Sort students by name.
    for pupil in listOfStudents:
            if pupil.calcSemGrade()=="A":
                print(pupil.getName())
main()
