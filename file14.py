import csv
with open('Giants.csv', mode ='r')as file:
csvFile = csv.reader(file)
for lines in csvFile:
		print(lines)
PROGRAM 16
string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")