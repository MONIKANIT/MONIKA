# -*- coding: utf-8 -*-
"""Heart_disease

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qfsWEQIbNB5JFPXFp7Z9FBiAVDD0MrLs
"""

#import libary and read data
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt
filePath = '/content/drive/MyDrive/Internship/heart.csv'

data = pd.read_csv(filePath)

data.head(5)

from google.colab import drive
drive.mount('/content/drive')

#print shape and columns
print("(Rows, columns): " + str(data.shape))
data.columns

# returns the number of unique values for each variable.
data.nunique(axis=0)

#summarizes the count, mean, standard deviation, min, and max for numeric variables.
data.describe()

# Display the Missing Values

print(data.isnull().sum())

#if theirs a good proportion between our positive & negative binary predictor
data['target'].value_counts()

# calculate correlation matrix

corr = data.corr()
plt.subplots(figsize=(15,10))
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))
sns.heatmap(corr, xticklabels=corr.columns,
            yticklabels=corr.columns, 
            annot=True,
            cmap=sns.diverging_palette(220, 20, as_cmap=True))

sns.catplot(x="target", y="oldpeak", hue="slope", kind="bar", data=data);

plt.title('ST depression (induced by exercise relative to rest) vs. Heart Disease',size=25)
plt.xlabel('Heart Disease',size=20)
plt.ylabel('ST depression',size=20)

# Filtering data by POSITIVE Heart Disease patient
pos_data = data[data['target']==1]
pos_data.describe()

# Filtering data by NEGATIVE Heart Disease patient
neg_data = data[data['target']==0]
neg_data.describe()

print("(Positive Patients ST depression): " + str(pos_data['oldpeak'].mean()))
print("(Negative Patients ST depression): " + str(neg_data['oldpeak'].mean()))
print("(Positive Patients thalach): " + str(pos_data['thalach'].mean()))
print("(Negative Patients thalach): " + str(neg_data['thalach'].mean()))

#Prepare Data for Modeling
#Assign the 13 features to X, & the last column to our classification predictor,y
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
#Split: the data set into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 1)

#Normalize: Standardizing the data will transform the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Modeling /Training
from sklearn.metrics import classification_report 
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=1)# get instance of model
model.fit(x_train, y_train) # Train/Fit model 

y_pred = model.predict(x_test) # get y predictions
print(classification_report(y_test, y_pred)) # output accuracy

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

#Feature Importance
# get importance
importance = model.feature_importances_

# summarize feature importance
for i,v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i,v))

index= data.columns[:-1]
importance = pd.Series(model.feature_importances_, index=index)
importance.nlargest(13).plot(kind='barh', colormap='winter')

print(model.predict(sc.transform([[20,1,2,110,230,1,1,140,1,2.2,2,0,2]])), '-> meaning Positive Diagnosis of Heart Disease'
)

y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

data.columns

len(data.columns)

input=np.zeros(len(data.columns)-1)

"""##Test the Model Properly work or not"""

age=64	
  sex=1
  cp=3
  tres=147
  chol=233
  fbs=1
  rest=0
  thalac=150
  exang=0
  oldpeak=2.3
  slop=0
  ca=0
  thal=1

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


  print(model.predict([input]))

"""##Create Functyion to pass the value"""

def HeartDisease(age,sex,cp,tres,chol,fbs,rest,thalac,exang,oldpeak,slop,ca,thal):
  input=np.zeros(len(data.columns)-1)
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

  return model.predict([input])[0]

print(HeartDisease(65,1,3,147,233,1,0,150,0,2.3,0,0,1))

"""#Save model for deployment"""

import pickle
with open('Heart_disease.pickle','wb') as f:
  pickle.dump(model,f)

import json
columns = {'data_columns' : [col for col in data.columns]}

with open("columns.json","w") as f:
  f.write(json.dumps(columns))

