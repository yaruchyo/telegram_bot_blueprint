from pymongo import MongoClient, DESCENDING
from pymongo.errors import ConnectionFailure
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()


class MongoDB:

    def __init__(self, db_name: str, MONGO_DB_USER: str, MONGO_DB_PASS: str, MONGO_DB_REST_URL: str):
        """
        Initializes the MongoDB helper class.
        :param db_name: Database name.
        :param collection_name: Collection name.
        """
        uri = f"mongodb+srv://{MONGO_DB_USER}:{MONGO_DB_PASS}{MONGO_DB_REST_URL}"
        self.client = MongoClient(uri, server_api=ServerApi('1'))

        # Check connection
        try:
            self.client.admin.command('ping')
            print("Connected to MongoDB")
        except ConnectionFailure as e:
            print("Could not connect to MongoDB", e)
        self.db = self.client[db_name]

    def insert_document(self, collection_name: str, document: dict):
        """
        Inserts a single document into the collection.
        :param collection_name:
        :param document: Dictionary representing the document.
        :return: Inserted ID.
        """
        result = self.db[collection_name].insert_one(document)
        return result.inserted_id

    def insert_many_documents(self, collection_name: str, documents: list):
        """
        Inserts multiple documents into the collection.
        :param documents: List of dictionaries representing documents.
        :return: List of inserted IDs.
        """
        result = self.db[collection_name].insert_many(documents)
        return result.inserted_ids

    def find_document(self, collection_name: str, query: dict):
        """
        Finds a single document matching the query.
        :param query: Dictionary representing the query.
        :return: Matching document or None if not found.
        """
        return self.db[collection_name].find_one(query)

    def find_documents(self, collection_name: str, query: dict, limit: int = 0):
        """
        Finds multiple documents matching the query.
        :param query: Dictionary representing the query.
        :param limit: Limit the number of documents returned (default is 0, meaning no limit).
        :return: List of matching documents.
        """
        return list(self.db[collection_name].find(query).limit(limit))
    def find_sorted_documents(self, collection_name: str, query: dict, limit: int = 0, skip=0):

        return list(self.db[collection_name].find(query).sort("date_posted", DESCENDING).skip(skip).limit(limit))

    def update_document(self, collection_name: str, query: dict, update_data: dict):
        """
        Updates a single document that matches the query.
        :param query: Dictionary representing the query.
        :param update_data: Dictionary representing the fields to update.
        :return: The updated document.
        """
        result = self.db[collection_name].update_one(query, {'$set': update_data})
        return result.modified_count

    def delete_document(self, collection_name: str, query: dict):
        """
        Deletes a single document matching the query.
        :param query: Dictionary representing the query.
        :return: Number of documents deleted.
        """
        result = self.db[collection_name].delete_one(query)
        return result.deleted_count

    def delete_documents(self, collection_name: str, query: dict):
        """
        Deletes multiple documents matching the query.
        :param query: Dictionary representing the query.
        :return: Number of documents deleted.
        """
        result = self.db[collection_name].delete_many(query)
        return result.deleted_count

    def count_documents(self, collection_name: str, query: dict = {}):
        """
        Counts the number of documents in the collection that match the query.
        :param query: Dictionary representing the query.
        :return: Number of matching documents.
        """
        return self.db[collection_name].count_documents(query)

    def get_max_id(self, collection_name: str, query: dict):
        max_id_doc = self.db[collection_name].find(query).sort("_id", -1).limit(1)
        try:
            max_id = max_id_doc.next()["_id"] if max_id_doc.alive else 0
        except:
            max_id = 0
        return max_id

    def close_connection(self):
        """
        Closes the MongoDB connection.
        """
        self.client.close()
