from flask import Flask , jsonify , request

app = Flask(__name__)
contacts_list = [{
    'id' : 1,
    'contact' : u"984453106685",
    'name' : u"M.Chellakumar",
    'done' : False
},
{
    'id' : 2,
    'contact' : u"994302366685",
    'name' : u"C Devasena",
    'done' : False
}]
@app.route("/")

def helloWorld():
    return "helloWorld !! This is a software created trough flask "

@app.route("/add-data", methods=["POST"]) 
def add_task(): 
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400) 
        
    contacts = { 
     'id': contacts_list[-1]['id'] + 1,
     'contact': request.json['contact'], 
     'name': request.json.get('name', ""), 
     'done': False 
    } 
    contacts_list.append(contacts) 
    return jsonify({ "status":"success", "message": "Task added succesfully!" })
        
@app.route("/get-data") 

def get_task(): 
    return jsonify({ "data" : contacts_list })

if (__name__ == "__main__"):
    app.run(debug= True)



