import csv

csv1 = "" # the filepath
csv2 = "" # the filepath

def compare2csv(a,b):
    # compares the values from two csv lists and returns values in list a that are not in list b
    listA = openUnpackCSV(a)
    listB = openUnpackCSV(b)

    differencesList = list(set(listA).difference(listB))

    # this outputs the list in a more human format
    for i in differencesList:
        print(i)


def openUnpackCSV(n):
    # transfers the contents of a csv document into a list
    file = open(n, "r")
    csv_reader = csv.reader(file)

    # this comes out as a list of lists
    initialList = []
    for row in csv_reader:
        initialList.append(row)

    # so this turns the list of lists into a simple list
    unpackedList = []
    for sublist in initialList:
        for item in sublist:
            unpackedList.append(item)

    return unpackedList

compare2csv(csv1,csv2)
