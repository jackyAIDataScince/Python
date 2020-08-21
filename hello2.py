#import necessary modules
import csv

reader = csv.DictReader(open('/file/data.csv','rt'))
for raw in reader:
        print(raw)
