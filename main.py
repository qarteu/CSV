import csv


#reading a file
with open('some.csv' , newline = '', ) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing a file
with open('some.csv','w', newLine = '') as file:
    writer = csv.writer(file)
    for row in reader:
        print(row)
