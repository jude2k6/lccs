import csv,os

basepath = os.path.dirname(__file__)

#opens the csv file and initiates a reader
with open(basepath+'\salary_data.csv', "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

#makes new csv file and initiates writer using utf8
    with open(basepath+'\cleaned_data.csv', "w",newline='', encoding="utf-8") as cleaned_file:
        csv_writer = csv.writer(cleaned_file)

        #skips to second line
        next(csv_reader)

        #loops through csv file reading it 
        for row in csv_reader:
            #strips the salary of  $ ,. and multiplys by .93 to convert to euro
            striped_sal = round(int(row[5].replace("$","").replace(",","").replace(".",""))/100*0.93)
            #writes the salary 
            row[5] = striped_sal
            #strips the age of Y/O
            stripped_age = int(row[0].strip(" Y/O"))
            #Writes the age
            row[0]=stripped_age
            #finally writes the whole row to the file
            csv_writer.writerow(row)
        
        