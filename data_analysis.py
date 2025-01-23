import os,csv,json,statistics
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
            #adds all female salarys and ages to file
            if row[1] == "Female":
                age = int(row[0])
                salary = int(row[5])
                data["age_corilation"]["female"]["age"].append(age)
                data["age_corilation"]["female"]["salary"].append(salary)
            else:
                #adds all male salarys and ages to file
                age = int(row[0])
                salary = int(row[5])
                data["age_corilation"]["male"]["age"].append(age)
                data["age_corilation"]["male"]["salary"].append(salary)
    #caclulates male r value
    male_salarys =pd.Series(data["age_corilation"]["male"]["salary"]) 
    male_ages = pd.Series(data["age_corilation"]["male"]["age"])
    male_coefficient = male_ages.corr(male_salarys)
    data["age_corilation"]["male"]["corilation"] = male_coefficient
    

    
    #caclulates male r value adds 
    female_salarys =pd.Series(data["age_corilation"]["female"]["salary"]) 
    female_ages = pd.Series(data["age_corilation"]["female"]["age"])
    female_coefficient = female_ages.corr(female_salarys)
    data["age_corilation"]["female"]["corilation"] = female_coefficient
    


    
    with open(basepath +"\cleaned_data.csv" , "r") as csv_file:
        csv_reader= csv.reader(csv_file)
        for row in csv_reader:
            if row[2] == "PhD":
                data["education"]["PhD"].append(int(row[5]))
            elif row[2] == "Master's":
                data["education"]["Master's"].append(int(row[5]))
            else:
                data["education"]["Bachelor's"].append(int(row[5]))

    median = {
        "Bachelor's" : statistics.median(data["education"]["Bachelor's"]),
        "Master's" : statistics.median(data["education"]["Master's"]),
        "PhD" : statistics.median(data["education"]["PhD"])
    }

    data["education"]["median"] = median
    
    #top and bottom from each education
    def top_bottom(salarys,education):

        ten_percent = round(len(salarys)/10)

        for i in range(ten_percent):
            data["education"]["top_bottom"]["salary"].append(salarys[i])
            data["education"]["top_bottom"]["type"].append('Bottom 10%')
            data["education"]["top_bottom"]["education"].append(education)
        for i in range(len(salarys)-ten_percent,len(salarys),1):
            data["education"]["top_bottom"]["salary"].append(salarys[i])
            data["education"]["top_bottom"]["type"].append('Top 10%')
            data["education"]["top_bottom"]["education"].append(education)

    
    bachlors_sorted = sorted(data["education"]["Bachelor's"])
    
    masters_sorted = sorted(data["education"]["Master's"])
    phd_sorted = sorted(data["education"]["PhD"])

    top_bottom(bachlors_sorted,"Bachelor's")
    top_bottom(masters_sorted,"Master's")
    top_bottom(phd_sorted,"PhD")



#dumps dictionary back to json file format 
with open("data.json","w") as f:
    json.dump(data,f,indent=4, separators=(",", ":"))