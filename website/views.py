from flask import Blueprint,render_template,request
import os




views = Blueprint('views',__name__)
#sets basepath so file paths will always be right 
base_path = os.path.dirname(__file__)

#saves graphs as variables as if I open the file when rendering it takes too long this uses extra memory but is faster
with open(base_path+"/graphs/educationgraph.html","r",encoding="utf-8") as f:
        education_graph = f.read()
        
with open(base_path+"/graphs/gendergraph.html","r",encoding="utf-8") as f:
            gender_graph = f.read()
            
with open(base_path+"/graphs/agegraph.html","r",encoding="utf-8") as f:
        age_graph = f.read()
with open(base_path+"/graphs/top_bottomgraph.html","r",encoding="utf-8") as f:
        top_bottomgraph = f.read()



#difines the urls and passes templates and graphs through

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
    
    if request.method== 'POST':
        
        data=request.form
        average  = avg_sal(data)
        return (f"<p>{average}</p>")
    else:
          
        return render_template('predictions.html', active_page = 'predictions')


