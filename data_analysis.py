import os,csv,json
import pandas as pd

basepath = os.path.dirname(__file__)

#open json file into dictionary data
with open("data_template.json","r") as f:
    data = json.load(f)


    #open cleand csv to analysie gender pay ratio
    with open(basepath +"\cleaned_data.csv" , "r") as csv_file:
        csv_reader= csv.reader(csv_file)

        total = 0
        female_total = 0
        male_total = 0
        n_women =0
        n_men = 0

        #totals pay 
        for row in csv_reader:
            print(row[5])
            total+=float(row[5])
            if row[1] == "Female":
                n_women+=1
                female_total+=float(row[5])
            else:
                n_men+=1
                male_total+=float(row[5])

        
        #gets avrage
        female_avg = female_total/n_women
        male_avg = male_total/n_men
        #ratio of womens to mens pay
        female_payratio = round(female_avg/male_avg *100)
        remainder = 100 - female_payratio
        data["salary_gender"]["female_ratio"] = female_payratio
        data["salary_gender"]["remainder"] = remainder

     #open cleand csv to analysie gender pay ratio
    with open(basepath +"\cleaned_data.csv" , "r") as csv_file:
        csv_reader= csv.reader(csv_file)

        for row in csv_reader:
            if row[1] == "Female":
                age = int(row[0])
                salary = int(row[5])
                data["age_corilation"]["female"]["age"].append(age)
                data["age_corilation"]["female"]["salary"].append(salary)
            else:
                age = int(row[0])
                salary = int(row[5])
                data["age_corilation"]["male"]["age"].append(age)
                data["age_corilation"]["male"]["salary"].append(salary)

    male_salarys =pd.Series(data["age_corilation"]["male"]["salary"]) 
    male_ages = pd.Series(data["age_corilation"]["male"]["age"])
    male_coefficient = male_ages.corr(male_salarys)
    data["age_corilation"]["male"]["corilation"] = male_coefficient
    print(male_coefficient)

    female_salarys =pd.Series(data["age_corilation"]["female"]["salary"]) 
    female_ages = pd.Series(data["age_corilation"]["female"]["age"])
    female_coefficient = female_ages.corr(female_salarys)
    data["age_corilation"]["female"]["corilation"] = female_coefficient

    print(female_coefficient)


with open("data.json","w") as f:
    json.dump(data,f,indent=4, separators=(",", ":"))