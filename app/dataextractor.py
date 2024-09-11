import csv

def createDataset():
    #path to local sample data file 
    path= 'C:\\Users\\devesh.trivedi\\Desktop\\Hackathon\\app\\sampledata.csv'  
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        dataset=[]
        # Iterate through the rows in the CSV
        for row in csv_reader:
            temp={
                'Request': row[0],
                'Response':row[1]
            }
            dataset.append(temp)
        return dataset
