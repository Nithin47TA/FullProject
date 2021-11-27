from dotenv import load_dotenv
import os
load_dotenv()

def get_database():
    from pymongo import MongoClient
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv("DB_ACCESS_URL")

    # Create a connection using MongoClient. 

    client = MongoClient(CONNECTION_STRING)

    # Create the database for our app
    return client['ToDoAPP']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
