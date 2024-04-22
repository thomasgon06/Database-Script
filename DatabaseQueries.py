import datetime
import os
import string
from pymongo import MongoClient
import bson
from bson.json_util import dumps
import matplotlib.pyplot as plt


connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo
meta = current_db.Metadata

#docs is a list of dictionaries

def all_records():
    docs = list(collection.find({}, {'_id': 0}).sort('Date Recorded', 1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')
    return docs 

def specific_day(month: int, day: int, year: int):
    start_of_day = datetime.datetime(year, month, day, hour=0, second=0, microsecond=0)
    end_of_day = datetime.datetime(year, month, day, hour=23, second=59, microsecond=999999)
    docs = list(collection.find({ "Date Recorded" : {'$gte': start_of_day,'$lte': end_of_day} }, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')
    return docs 

def exact_time(requestedtime: datetime): 
    docs = list(collection.find({ "Date Recorded" : requestedtime }, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')
    return docs

def time_range(startofrange: datetime, endofrange: datetime):
    docs = list(collection.find({ "Date Recorded" : {'$gte': startofrange,'$lte': endofrange} }, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')

    return docs

def find_voltage(voltage: float):
    docs = list(collection.find({ "Voltage" : voltage }, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')

    return docs

def voltage_range(start: float, end: float):
    docs = list(collection.find({ "Voltage" : {'$gte': start,'$lte': end} }, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')

    return docs

def write_to_bson(docs: list, file_path: string):
    open(file_path, 'w').close()
    for doc in docs:
        bson_data = bson.BSON.encode(doc)
        with open(file_path, "ab") as bfile:
            bfile.write(bson_data)
    bfile.close()

def write_to_json(docs: list, file_path: string):
    json_data = dumps(docs, indent = 2)
    with open(file_path, 'w') as file:
        file.write(json_data)
    file.close()

def plot_recent_voltage(ModuleNumber: float):
    metacollec = meta.find()
    for m in metacollec:
        mostrecent = m["Most Recent"]
        print(type(mostrecent))

    startofrange = mostrecent.replace(hour=0, minute=0, second=0, microsecond=0)
    endofrange = mostrecent.replace(hour=23, minute=59, second=59, microsecond=999999)

    docs = list(collection.find({ "Module #" : ModuleNumber, "Date Recorded" : {'$gte': startofrange,'$lte': endofrange}}, {'_id': 0}).sort('Date Recorded', -1))
    for doc in docs:
        if 'Date Recorded' in doc:  
            doc['Date Recorded'] = doc['Date Recorded'].strftime('%m/%d/%Y %I:%M:%S.%f %p')
    x = []
    y = []

    for doc in docs:
        x.append(doc.get("Date Recorded"))
        y.append(doc.get("Voltage"))

    # Plotting the data with dots
    plt.scatter(x, y, color='blue', marker='o')
    plt.xticks([])
    #plt.yticks(range(0, int(max(y)) + 2, 1))

    # Adding labels and title
    plt.ylabel('Voltage')
    plt.title('Voltage Plot for Module ' + str(ModuleNumber))

    # Display the plot
    plt.show()

    return docs

def misbehaving():
    metacollec = meta.find()
    for m in metacollec:
        mostrecent = m["Most Recent"]

    startofrange = mostrecent.replace(hour=0, minute=0, second=0, microsecond=0)
    endofrange = mostrecent.replace(hour=23, minute=59, second=59, microsecond=999999)

    badtemps = list(collection.find({"Temperature": {"$not": {"$gte": 18, "$lte": 28}}, "Date Recorded" : {'$gte': startofrange,'$lte': endofrange}},{'_id': 0}).sort('Date Recorded', -1))
    print(len(badtemps))
    badvoltages = list(collection.find({"Voltage": {"$not": {"$gte": 1000, "$lte": 1400}}, "Date Recorded" : {'$gte': startofrange,'$lte': endofrange}},{'_id': 0}).sort('Date Recorded', -1))
    print(len(badvoltages))
    badadc = list(collection.find({"ADC": {"$not": {"$gte": 1200, "$lte": 1250}}, "Date Recorded" : {'$gte': startofrange,'$lte': endofrange}},{'_id': 0}).sort('Date Recorded', -1))
    print(len(badadc))
    combined = badtemps + badvoltages + badadc
    unique = []
    [unique.append(x) for x in combined if x not in unique]
    return unique

    


    




    

    
