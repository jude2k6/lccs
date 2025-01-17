import plotly.express as px
import json,os
basepath = os.path.dirname(__file__)

#opens the json file converts it to a dictionary called data
with open("data.json","r") as f:
    data = json.load(f)

#joins the male anf female ages into a single age list does the same with salarys
age = data["age_corilation"]["male"]["age"] +data["age_corilation"]["female"]["age"]
salary = data["age_corilation"]["male"]["salary"] + data["age_corilation"]["female"]["salary"]
#generates a gender list based of the lenght of the male and female age lists this is to add colours
gender = ["male"]*len(data["age_corilation"]["male"]["age"]) + ["female"]*len(data["age_corilation"]["female"]["age"])
#creates a scatter plot based on ages and salarys and writes the html to a file in /website/graphs
fig = px.scatter(x=age, y=salary,color = gender ,
                 labels={'x':'Age', 'y':'Salary',"color":"Gender"},
                title ="Age Salary Corrilation",)

fig.write_html(basepath+'/website/graphs/agegraph.html', full_html= False, div_id = "graph")


fig = px.pie(values=data["salary_gender"], names= ["Female pay", "Extra men pay men recieve"],title="Gender wage gap")
fig.update_traces(textinfo="label+percent")
 
fig.write_html(basepath+'/website/graphs/gendergraph.html', full_html= False, div_id = "graph")


fig = px.bar(x=["Bachlors","Masters","Phd"],y=data["education"]["median"],
             title="Median Salary by level of Education",
             labels={'x':'Education', 'y':'Salary'},
             color=["Bachlors","Masters","Phd"])

fig.write_html(basepath+'/website/graphs/educationgraph.html', full_html= False, div_id = "graph")

#top and bottom 10%




fig = px.histogram( x=data["education"]["top_bottom"]["education"], y=data["education"]["top_bottom"]["salary"],
             color=data["education"]["top_bottom"]["type"], barmode='group',
             histfunc='avg',title='Top and bottom 10% by salary')

fig.write_html(basepath+'/website/graphs/top_bottomgraph.html', full_html= False, div_id = "graph2")