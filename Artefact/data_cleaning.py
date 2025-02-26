import csv,os

basepath = os.path.dirname(__file__)

with open(basepath+'\salary_data.csv', "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(basepath+'\cleaned_data.csv', "w",newline='', encoding="utf-8") as cleaned_file:
        csv_writer = csv.writer(cleaned_file)
        counter = 0
        next(csv_reader)
        for line in csv_reader:
            row = line
            striped_sal = round(int(line[5].replace("$","").replace(",","").replace(".",""))/100*0.93)
            row[5] = striped_sal
            stripped_age = int(line[0].strip(" Y/O"))
            row[0]=stripped_age
            csv_writer.writerow(row)
        
        