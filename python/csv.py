import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(test.csv, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
