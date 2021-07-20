#from os import access
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

"""
@app.route('/get_feature_names')
def get_feature_names():
    response = jsonify({'Columns' : util.show_data_columns()})
    return response

@app.route('/H_D')
def H_D():
    Age = int(request.form['AGE'])
    Sex = int(request.form['SEX'])
    CP = int(request.form['CP'])
    Tres = int(request.form['TRES'])
    Chl = int(request.form['CHL'])
    Fbs = int(request.form['FBS'])
    Rest= int(request.form['REST'])
    Thalac = int(request.form['THALAC'])
    Exang = int(request.form['EXANG'])
    OldPeak = float(request.form['OLDPEAK'])
    Slop = int(request.form['SLOP'])
    Ca = int(request.form['CA'])
    Thal = int(request.form['THAL'])
        
    response ={'estimate' : util.Heart_Disease(Age,Sex,CP,Tres,Chl,Fbs,Rest,Thalac,Exang,OldPeak,Slop,Ca,Thal)}
    
    #response.headers.add('Access-Control-Allow-Origin','*')
    return response


util.read_artifacts()
"""
if __name__ == "__main__":
    app.run(debug=True)
