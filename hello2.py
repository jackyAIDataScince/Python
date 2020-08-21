#import necessary modules
import csv

reader = csv.DictReader(open('/home/jackyjcck/hello/data.csv','rt'))
for raw in reader:
        print(raw)
