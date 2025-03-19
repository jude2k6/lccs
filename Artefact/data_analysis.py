import os,csv,json,statistics
import pandas as pd


basepath = os.path.dirname(__file__)

#open json file into dictionary data
with open(basepath +"/data_template.json","r") as f:
    data = json.load(f)


    #open cleand csv to analysie gender pay ratio
    with open(basepath +"\cleaned_data.csv" , "r") as csv_file:
        csv_reader= csv.reader(csv_file)

        #initiates counters needed to do the totals
        total = 0
        female_saltotal = 0
        male_saltotal = 0
        n_women =0
        n_men = 0

        #totals pay 
        for row in csv_reader:
            
            total+=float(row[5])
            if row[1] == "Female":
                n_women+=1
                female_saltotal+=float(row[5])
            else:
                n_men+=1
                male_saltotal+=float(row[5])

        
        #gets average 
        female_avg = female_saltotal/n_women
        male_avg = male_saltotal/n_men
        #ratio of womens to mens pay
        female_payratio = round(female_avg/male_avg *100)
        remainder = 100 - female_payratio
        #writes to dictionary
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
                data["education"]["level"]["PhD"].append(int(row[5]))
            elif row[2] == "Master's":
                data["education"]["level"]["Master's"].append(int(row[5]))
            else:
                data["education"]["level"]["Bachelor's"].append(int(row[5]))

    median = {
        "Bachelor's" : statistics.median(data["education"]["level"]["Bachelor's"]),
        "Master's" : statistics.median(data["education"]["level"]["Master's"]),
        "PhD" : statistics.median(data["education"]["level"]["PhD"])
    }

    data["education"]["level"]["median"] = median
    
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

    
    bachlors_sorted = sorted(data["education"]["level"]["Bachelor's"])
    
    masters_sorted = sorted(data["education"]["level"]["Master's"])
    phd_sorted = sorted(data["education"]["level"]["PhD"])

    top_bottom(bachlors_sorted,"Bachelor's")
    top_bottom(masters_sorted,"Master's")
    top_bottom(phd_sorted,"PhD")



#dumps dictionary back to json file format 
with open(basepath +"/data.json","w") as f:
    json.dump(data,f,indent=4, separators=(",", ":"))













    