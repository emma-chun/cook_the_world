import csv

def print_hi():

    results = []
    with open('NationalityList.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row)

    print(results)

if __name__ == '__main__':
    print_hi()