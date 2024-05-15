
# MongoDB Queries Module Documentation

This Python module provides several functions that query a MongoDB database. The database stores sensor data and metadata. The module has queries that retrieve all records, retrieve records from a specific day,retrieve records at an exact time, retrieve records within a time range, retrieve records with a certian voltage, retrieve records within a voltage range, . 

## Connection Setup

The module connects to a MongoDB database using the following connection string:
```python
connection_string = "mongodb://localhost:27017/" #Replace with "mongodb://ip_of_database:27017" if database is not on local machine.
client = MongoClient(connection_string)
current_db = client.SensorData
collection = current_db.SensorInfo
meta = current_db.Metadata
```
## External Tools Used
    - **Pymongo**:
        -Pymongo is the Object-Document Mapping Library used to access the database. Its documentation can be found [here](https://pymongo.readthedocs.io/en/stable/).
        
    -**Pyplot**:
        -Pyplot, which is part of matplotlib, is used to generate graphs. Its documentation can be found [here](https://matplotlib.org/stable/tutorials/pyplot.html)
        
    
## Functions

- **all_records()**:

    - Retrieves all records from the `SensorInfo` collection, sorted by the `Date Recorded` field in decending order.

    - **Returns:**: 
        - `docs` (list): A list of dictionaries containing all records.


- **specific_day(month: int, day: int, year: int)**:

    - Retrieves records for a specific day.

    - **Parameters:**
        - `month` (int): Month of the desired day.
        - `day` (int): Day of the desired day.
        - `year` (int): Year of the desired day.
        
    **Returns:**
        - `docs` (list): A list of dictionaries containing records for the specified day.

- **exact_time(requestedtime: datetime)**:

    - Retrieves records for an exact time.

    - **Parameters:**
        - `requestedtime` (datetime): The exact time for which records are to be retrieved.

    - **Returns:**
        - `docs` (list): A list of dictionaries containing records for the specified exact time.

- **time_range(startofrange: datetime, endofrange: datetime)**:

    - Retrieves records within a specified time range.

    - **Parameters:**
        - `startofrange` (datetime): The start time of the range.
        - `endofrange` (datetime): The end time of the range.

    **Returns:**
        - `docs` (list): A list of dictionaries containing records within the specified time range.
        
- **find_voltage(voltage: float)**:

    - Retrieves with a specific voltage

    - **Parameters:**
        - 'voltage' (float): The voltage attribute that you want retrieved records to have.

    **Returns:**
        - `docs` (list): A list of dictionaries containing records with the requested voltage.
        
        
- **voltage_range(start: float, end: float)**:

    - Retrieves with a specific voltage

    - **Parameters:**
        - 'start' (float): The starting voltage of the range.
        - 'end' (float): The ending voltage of the range.
    **Returns:**
        - `docs` (list): A list of dictionaries containing records with the requested voltage.
        
- write_to_bson(docs: list, file_path: string)**:

    - Takes in a list of python dictionaries containing the query results and writes the query results to a bson file.  

    - **Parameters:**
        - 'docs' (list) A list of dictionaries containing the query results that you would like to write to a bson file.
        - 'file_path' (string) Where you would like the bson file to be saved.
        
    **Returns:**
        - `docs` (list): Returns the docs attribute that was passed to it.
        
- write_to_json(docs: list, file_path: string)**:

    - Takes in a list of python dictionaries containing the query results and writes the query results to a json file.  

    - **Parameters:**
        - 'docs' (list) A list of dictionaries containing the query results that you would like to write to a json file.
        - 'file_path' (string) Where you would like the json file to be saved.
        
    **Returns:**
        - `docs` (list): Returns the docs attribute that was passed to it.
        
        
- plot_recent_voltage(ModuleNumber: float)**:

    - Takes in a module number and generates a graph of all voltages for documents with a Date Recorded attribute that matches the Metadata document's most recent attribute.

    - **Parameters:**
        - 'ModuleNumber' (float) Module that you would like to graph the results of.
        
    **Returns:**
        - `docs` (list): Returns list of what it graphed.
        

### misbehaving()

Identifies and retrieves records that are misbehaving based on certain criteria for temperature, voltage, and ADC values.

    **Returns:**
        - `unique` (list): A list of dictionaries containing misbehaving records. All records in the list are unique, duplicates are eliminated for clarity. 
