#import necessary modules
import csv
with open('/home/jackyjcck/hello/data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)
