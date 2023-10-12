import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/orlando22222/inf354/main/healthcare-dataset-stroke-data.csv'
data = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
ds = data.to_numpy()
headers = ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']

def media():
  for i in range(len(ds[0])):
    if( type(ds[0][i]) != str): 
      print(headers[i], np.mean(data[headers[i]]))
  print()

def moda():
  print("\nMODA")
  for i in range(len(ds[0])):
    print(headers[i], stat.mode(data[headers[i]]))
  print()

def cuartil(k):
  print("CUARTIL VERSION NUMPY", k)
  data1 = pd.DataFrame(data)
  data2 = data1.select_dtypes(include=[np.number])
  print(np.percentile(data2, k, axis = 0))
  print()

def cuartilP(k):
  print("CUARTIL VERSION PANDA", k)
  df = pd.DataFrame(data)
  text_cols = []
  for col in df.columns:
      if df[col].dtype == object:
          text_cols.append(col)

  df = df.drop(text_cols, axis=1)
  q1 = df.quantile(k)
  print(q1)
  print()

def percentil(k):
  print("PERCENTIL", k)
  df = pd.DataFrame(data)
  text_cols = []
  for col in df.columns:
      if df[col].dtype == object:
          text_cols.append(col)

  df = df.drop(text_cols, axis=1)
  q1 = df.quantile(k)
  print(q1)
  print()

def graficar():
   print('GRAFICAS UTILIZANDO LA LIBRERIA MATPLOTLIB')
   x = data['age']
   y = data['avg_glucose_level']

   plt.bar(x,y)

   plt.title("NIVEL DE GLUCOSA POR EDAD")
   plt.xlabel("age")
   plt.ylabel("avg_glucose_level")

   plt.show()
 

if __name__=='__main__':
   print("MEDIA")
   media()
   moda()
   cuartil(25);
   cuartil(50);
   cuartil(75);
   cuartilP(.25);
   cuartilP(.50);
   cuartilP(.75);
   percentil(.6);
   graficar();