import plotly.express as px
import json


with open("data.json","r") as f:
    data = json.load(f)
age = data["age_corilation"]["male"]["age"] +data["age_corilation"]["female"]["age"]
salary = data["age_corilation"]["male"]["salary"] + data["age_corilation"]["female"]["salary"]
gender = ["male"]*len(data["age_corilation"]["male"]["age"]) + ["female"]*len(data["age_corilation"]["female"]["age"])

fig = px.scatter(x=age, y=salary,color = gender ,labels={'x':'Age', 'y':'Salary'}, title ="Age Salary Corrilation")

fig.show()
fig.write_html('agecorrilation.html')

fig = px.pie(values=data["salary_gender"], names= ["Female pay", "Extra men pay men recieve"],title="Gender wage gap")
fig.update_traces(textinfo="label+percent")
fig.show()