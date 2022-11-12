import csv

from sklearn.metrics import SCORERS
f= open("middle.csv",'r',encoding = 'utf-8')
data = csv.reader(f)
print(data)
f.close()