# -*- coding: utf-8 -*-
"""FirstBert_PieChart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WHniV5uBzCk5zZ_IeAXEvPLKl3OwrpSL
"""

pip install chart-studio

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

chart_data = pd.read_csv("/content/drive/MyDrive/HateSpeechDataSet/data_huang_devansh.csv")
df_chart_data_1 = chart_data[chart_data['Label']==1]
df_chart_data_0 = chart_data[chart_data['Label']==0]
print(df_chart_data_1)
print(df_chart_data_0)

df_500 =  chart_data.loc[chart_data['Content'].str.len() < 500]

labels = 'HateSpeech', 'Normol word'
# we need to change the value at here
sizes = [133694, 708641]

# configure the distand between two parts in pie chart
explode = (0, 0.1) 

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Equal aspect ratio 
plt.axis('equal') 

plt.show()

list_length = []
list_length_1000 = []
list_length_500 = []
sentence = chart_data['Content']
#842334
for i in range(0,1000):
  sentence_temp = sentence[i]
  word_list = sentence_temp.split(' ')
  len_temp = len(word_list)
  if(len_temp > 500):
    list_length_1000.append(len_temp)
  else:
    list_length_500.append(len_temp) 

#plt.bar(range(len(list_length)),list_length)

#plt.show()

labels = 'long scentence above 500 words', 'Normol scentenc below 500 words'
sizes = [len(list_length_1000), len(list_length_500)]

# configure the distand between two parts in pie chart
explode = (0, 0.1) 

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Equal aspect ratio 
plt.axis('equal') 

plt.show()