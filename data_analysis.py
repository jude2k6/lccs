import os,csv,json

basepath = os.path.dirname(__file__)

total = 0
female_total = 0
male_total = 0

with open(basepath +"\cleaned_data.csv" , "r") as csv_file:
    csv_reader= csv.reader(csv_file)

    for row in csv_reader:
        print(row[5])
        total+=float(row[5])
        if row[1] == "Female":
            female_total+=float(row[5])
        else:
            male_total+=float(row[5])

    print(total)