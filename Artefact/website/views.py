from flask import Blueprint,render_template,request
import os,json,pandas as pd




views = Blueprint('views',__name__)

#sets basepath so file paths will always be right 
base_path = os.path.dirname(__file__)

def avg_sal(form):
    #sets basepath so file paths will always be right 
    basepath = os.path.dirname(__file__)
    basepath = basepath.replace("\website", "")
    #opens file as df
    df = pd.read_csv(basepath+'\cleaned_data.csv',header=None)
    df.columns=['age','gender','education','job','experience','salary']
    #filters the df based on the form
    filtered_df = df[(df.age <= int(form['age'])+5)&(df.age >= int(form['age'])-5)  & (df.gender == form['gender']) & (df.education == form['education'])]
    
    #if the df is empty returns this
    if filtered_df.empty:
          average = "No data"
          percentage = "No data"

    else:
        #calculates the average average on the filtered form
        average = round(filtered_df["salary"].mean())
        # calculates the percentage compared to the filtered df
        percentage = str(abs(100  - round(int(form['salary'])/average*100)))
        if int(form['salary'])>average:
             percentage = percentage + "% more"
        else:
             percentage = str(percentage) + "% less"
    return average,percentage

#saves graphs as variables as if I open the file when rendering it takes too long this uses extra memory but is faster
with open(base_path+"/graphs/educationgraph.html","r",encoding="utf-8") as f:
        education_graph = f.read()
        
with open(base_path+"/graphs/gendergraph.html","r",encoding="utf-8") as f:
            gender_graph = f.read()
            
with open(base_path+"/graphs/agegraph.html","r",encoding="utf-8") as f:
        age_graph = f.read()
with open(base_path+"/graphs/top_bottomgraph.html","r",encoding="utf-8") as f:
        top_bottomgraph = f.read()



#defines the urls and passes templates and graphs through 

@views.route('/')
def home_site():
    
    return render_template('home.html', active_page = 'home')

@views.route('/education')
def education():
    
    return render_template('education.html',graph1=education_graph,graph2=top_bottomgraph, active_page = 'education')

@views.route('/gender')
def gender():

    return render_template('gender.html',graph=gender_graph, active_page = 'gender')

@views.route('/age')
def age():
    
    return render_template('age.html',graph=age_graph, active_page = 'age')

@views.route('/help')
def help():
    
    return render_template('help.html', active_page = 'help')


@views.route('/predictions', methods=['POST','GET'])
def predictions():
    #if form is sent
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        #forms data is written to variable data
        data=request.form
        #passes through data into the fuction that returns average and perecnt
        average,percent = avg_sal(data)
        

        #opens the commentsjson and assignes it to variable comments
        with open(basepath+"/comments.json","r") as f:
            comments = json.load(f)
        #writes users data to comments if they agree
        if data["collect"] == "yes":
            #checks how many comments there are and writes new comment to next 
            comments[len(comments)+1] = data
            with open(basepath+"/comments.json","w") as f:
                json.dump(comments,f,indent=4, separators=(",", ":"))
        return render_template('predictions.html',average=average,percent=percent,comments=comments ,active_page = 'predictions')
    else:
          
        return render_template('predictions.html', active_page = 'predictions')


