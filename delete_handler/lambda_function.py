import json
import database


db = database.get_database()

collection = db['Activity']


def lambda_handler(event, context):

    todelete=event['queryStringParameters']['remove']

    collection.delete_one({"title":todelete})

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body':json.dumps(todelete)
    }
