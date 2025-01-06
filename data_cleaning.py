import csv,os

basepath = os.path.dirname(__file__)

with open(basepath+'\salary_data.csv', "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(basepath+'\cleaned_data.csv', "w",newline='', encoding="utf-8") as cleaned_file:
        csv_writer = csv.writer(cleaned_file)
        counter = 0
        next(csv_reader)
        for line in csv_reader:
            counter +=1
            print(counter)
            row = line
            striped = round(int(line[5].replace("€","").replace(",","").replace(".",""))/100)
            row[5] = striped
            csv_writer.writerow(row)
        
        