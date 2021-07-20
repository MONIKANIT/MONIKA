import pickle
import json
import numpy as np
import datetime
current_time = datetime.datetime.now()

_data_columns = None
_model = None

def read_artifacts():   
    global _data_columns
    global _model
    print('Accessing Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data_columns']
    print(_data_columns)

    with open('./Heart_disease.pickle','rb') as f:
        _model = pickle.load(f)
    
    print('Loading Artifacts Done...')

    
def Heart_Disease(age,sex,cp,tres,chol,fbs,rest,thalac,exang,oldpeak,slop,ca,thal):
  input = np.zeros(len(_data_columns))
  input[0]=age
  input[1]=sex
  input[2]=cp
  input[3]=tres
  input[4]=chol
  input[5]=fbs
  input[6]=rest
  input[7]=thalac
  input[8]=exang
  input[9]=oldpeak
  input[10]=slop
  input[11]=ca
  input[12]=thal

  return _model.predict([input])[0]
  
def show_data_columns():
    return _data_columns

#show_data_columns()
read_artifacts()
print(Heart_Disease(65,1,3,147,233,1,0,150,0,2.3,0,0,1))
