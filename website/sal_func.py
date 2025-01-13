def avg_sal(form):
    import pandas as pd
    import os

    basepath = os.path.dirname(__file__)
    basepath = basepath.strip("\website")
    print(basepath)
    df = pd.read_csv(basepath+'s\cleaned_data.csv',header=None)
    df.columns=['age','gender','education','job','experience','salary']
    print(df)

    filtered_df = df[(df.age <= form['age']+5)&(df.age >= form['age']-5)  & (df.gender == form['gender']) & (df.education == form['education'])]
    average = filtered_df["salary"].mean()
    return average 


form = {
    "age":45,
    "gender":"Male",
    "education":"PhD",
}

print(avg_sal(form))