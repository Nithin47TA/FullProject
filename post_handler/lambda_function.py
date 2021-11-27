import json
import database
import datetime



db = database.get_database()

collection = db['Activity']


def lambda_handler(event, context):
    print("down")

    print(event['queryStringParameters']['title'],event['queryStringParameters']['description'],event['queryStringParameters']['importance'])
    
    newTile = {
        "title": event['queryStringParameters']['title'],
        "description": event['queryStringParameters']['description'],
        "importance": event['queryStringParameters']['importance'],
        "date": datetime.datetime.today()
    }

    collection.insert_one(newTile)

    return {
        
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps("Succesfully updated the list")
    }
