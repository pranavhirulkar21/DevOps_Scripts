import csv

with open('databook.csv','r') as datafile:  # for reading or displaying the data of file 
    file_reader = csv.reader(datafile)
    
    with open('newdatabook.csv', 'w') as newdatafile:  # for writing the data to new file
        file_writer = csv.writer(newdatafile, delimiter='-') # you can also use \t as a delimiter
        
        for line in file_reader:
            file_writer.writerow(line)


# Using Dictioanry

with open('databook.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('newdata.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email'] # for not displaying the email row
            csv_writer.writerow(line)
  
            
            