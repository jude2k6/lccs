import csv,os

basepath = os.path.dirname(__file__)

with open(basepath+'\salary_data.csv', "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(basepath+'\cleaned_data.csv', "w",newline='', encoding="utf-8") as cleaned_file:
        csv_writer = csv.writer(cleaned_file)

        next(csv_reader)
        for line in csv_reader:
            row = line
            striped = line[5].replace("€","").replace(",","").replace(".","")
            print(striped)
            row[5] = striped
            print(row)
            csv_writer.writerow(row)
        
        