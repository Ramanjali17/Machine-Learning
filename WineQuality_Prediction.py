#Importing libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import  GradientBoostingClassifier
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
# from sklearn import metrics
# from sklearn.metrics import recall_score, confusion_matrix, precision_score, f1_score, accuracy_score, classification_report, roc_curve
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')


def winequalityPrediction(input_data):
  # loading wine quality dataset to pandas data frame
  df = pd.read_csv('winequality.csv')
  print(input_data)
  # help
  # pd.read_csv?

  # printing first 5 row of dataset
  # print("head")
  # print(df.head())

  # number of rows and colums in this dataset
  # print("shape")
  # print(df.shape)

  # getting statictical meausure of data
  # print("describe")
  # print(df.describe())

  df=df.fillna(df.alcohol.mean())
  
  df['best quality'] = [1 if x > 6 else 0 for x in df.quality]
  df.replace({'white': 1, 'red': 0}, inplace=True)
  X = df.drop(['quality', 'best quality'], axis=1)
  y = df['best quality']
  
  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.30, random_state = 40, stratify=y)

  num_cols = ["alcohol", 'fixed acidity', 'pH']
  scaler= StandardScaler()

  X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
  X_test[num_cols] = scaler.transform(X_test[num_cols])

  """Train Test Split"""
  gb = GradientBoostingClassifier()
  gb.fit(X_train, y_train)
  gb_pred = gb.predict(X_test)

  # changing input data into numpy array
  np_array = np.asarray(input_data)

  # changing the input data to a numpy array
  input_data_as_numpy_array = np.asarray(input_data)

  # reshape the data as we are predicting the label for only one instance
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = gb.predict(input_data_reshaped)
  print(prediction)

  if(prediction == 0):
    print("Bad Quality Wine")
    return False
  else:
    print("Good Quality Wine")
    return True