import sys
import os
sys.path.append('/Users/tommy/desktop/Database_Script')
import DatabaseQueries
import pprint
import matplotlib.pyplot as plt
import random

printer = pprint.PrettyPrinter()


def main():
    docs = DatabaseQueries.all_records()
    #print(len(docs))
    #DatabaseQueries.plot_recent_voltage(43)
    #for doc in docs:
      # printer.pprint(doc)
       #print()

    
    DatabaseQueries.write_to_json(docs, "/Users/tommy/desktop/Database_Script/data_files/data.json")
    #DatabaseQueries.write_to_bson(docs, "/Users/tommy/desktop/Database_Script/data_files/output.bson")

    #docs = DatabaseQueries.plot_voltage(339)
   

   


   



main()