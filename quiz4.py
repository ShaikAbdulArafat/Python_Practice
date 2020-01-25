import csv
def main():
    rows=[]
    with open('test.csv', 'r+') as csvfile:
        file_reader = csv.reader(csvfile,delimiter = ',')
        for row in file_reader:
            rows.append(row)
    print(rows)
    with open('test1.csv','w', newline='') as csvfile:
        file_writer = csv.writer(csvfile,delimiter=',')
        for row in rows:
            if row[0] == 'Rohit':
                row[3] = 'A'
            file_writer.writerow(row)
# main()

test=[['Name', 'Class', 'Subject', 'Grade'], ['Ajay', '10', 'English', 'A'], ['Rohit', '9', 'English', 'B'], ['Chaman', '10', 'English', 
'A'], ['Rudra', '9', 'English', 'C'], ['Rajesh', '10', 'English', 'B']]
with open( 'test.csv' ,'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile,delimiter=',')
        for row in test:
            file_writer.writerow(row)