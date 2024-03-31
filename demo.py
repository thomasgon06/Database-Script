import sys
import os
#change paths to appropriate paths for your system...
sys.path.append('.../Database_Script')
import DatabaseQueries
import pprint

printer = pprint.PrettyPrinter()


def main():
    docs = DatabaseQueries.find_voltage(9.554253567558156)
    DatabaseQueries.write_to_json(docs, ".../data_files/data.json")
    DatabaseQueries.write_to_bson(docs, ".../data_files/output.bson")

    for doc in docs:
        printer.pprint(doc)
        print()



main()
