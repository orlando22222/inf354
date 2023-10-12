import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/orlando22222/inf354/main/healthcare-dataset-stroke-data.csv'
data = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
ds = data.to_numpy()
headers = ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']

if __name__=='__main__':
   print("MEDIA")
   media()
   print("MODA")
   moda()
   cuartil(1);
   cuartil(2);
   cuartil(3);
   percentil(60);
   graficar();

def cuartil(k):
  print("QUARTIL ", k)
  for i in range(len(ds[0])):
    sum = 0;
    if( type(ds[0][i]) != str):
      v = []
      for j in range(len(ds)):
        v.append(ds[j][i])

      v.sort()
      cur = k * (len(v) + 1) / 4
      pos = int(cur)
      print(headers[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(v[pos - 1])
      else:
        x1 = v[pos - 1]
        x2 = v[pos]
        total = abs(x2 + x1) / 2
        print(total)
  print()



def percentil(k):
  print("PERCENTIL ", k)
  for i in range(len(ds[0])):
    sum = 0;
    if( type(ds[0][i]) != str):
      v = []
      for j in range(len(ds)):
        v.append(ds[j][i])

      v.sort()
      cur = k * (len(v) + 1) / 100
      pos = int(cur)
      print(headers[i], end=  ' ')

      if(cur == pos):
        # quartil es exacto
        print(v[pos - 1])
      else:
        x1 = v[pos - 1]
        x2 = v[pos]
        total = abs(x2 + x1) / 2
        print(total)
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

def media():
  for i in range(len(ds[0])):
    sum = 0;
    if( type(ds[0][i]) != str):
      for j in range(len(ds)):
        sum += ds[j][i];
      sum /= len(ds)
    
    print(headers[i], sum)
  print()

def moda():
  for i in range(len(ds[0])):
    matriz = {}
    for j in range(len(ds)):
      if(ds[j][i] in matriz):
        matriz[ds[j][i]] += 1;
      else:
        matriz[ds[j][i]] = 1;
    
    lista = []
    for key, value in matriz.items():
      lista.append([value, key])
    # print(headers[i], "mapita " , len(matriz))
    lista.sort(reverse=True)
    print(headers[i], lista[0][1])
  print()


