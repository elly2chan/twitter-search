import json
from pathlib import Path
from pymongo import MongoClient


def main():
    # Connect to MongoDB Cloud
    client = MongoClient("mongodb+srv://admin:admin@cluster0.mxr4yut.mongodb.net/?retryWrites=true&w=majority",
                         tls=True, tlsAllowInvalidCertificates=True)
    database = client["twitter_search"]
    collection = database["tweets"]

    # Open initial data folder and insert jsons into database
    path = Path("samples").glob("*.json")

    for json_file in path:
        json_data = json.load(open(json_file))

        # Use "replace_one" to ensure no duplicates will be inserted if script is ran multiple times with the same data
        collection.replace_one(json_data, json_data, upsert=True)


if __name__ == "__main__":
    main()






