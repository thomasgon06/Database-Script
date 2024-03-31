import datetime
import os
import string
from pymongo import MongoClient
import bson
from bson.json_util import dumps

connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo

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
    
