import json
from pathlib import Path
from pymongo import MongoClient


def main():

    # Connect to MongoDB Cloud by providing your connection string and credentials
    client = MongoClient("Provide your connection string here")
    # Provide your database name
    database = client["twitter_search"]
    # Provide your database collection
    collection = database["tweets"]

    # Open initial data folder and insert jsons into database
    path = Path("samples").glob("*.json")

    for json_file in path:
        json_data = json.load(open(json_file))

        # Use "replace_one" to ensure no duplicates will be inserted if script is ran multiple times with the same data
        collection.replace_one(json_data, json_data, upsert=True)


if __name__ == "__main__":
    main()






