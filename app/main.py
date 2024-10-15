from pymongo import MongoClient
from datetime import datetime


def get_database():
    client = MongoClient('mongodb://root:example@db:27017/')
    return client['mydatabase']


def insert_document(db):
    collection = db['mycollection']
    document = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "timestamp": datetime.now()
    }
    inserted_id = collection.insert_one(document).inserted_id
    print(f"Inserted document with id: {inserted_id}")


def find_documents(db):
    collection = db['mycollection']
    documents = collection.find()
    for doc in documents:
        print(f"Found document: {doc}")


if __name__ == "__main__":
    db = get_database()
    insert_document(db)
    find_documents(db)
