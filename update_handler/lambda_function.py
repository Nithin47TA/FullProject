import json
import database


db = database.get_database()

collection = db['Activity']


def lambda_handler(event, context):

    new_data={}
    query={}
    for item in event['queryStringParameters']:
        if item=="update":
            to_update= event['queryStringParameters']["update"]
            query={"title":to_update}
        else:
            new_data[item]=event['queryStringParameters'][item]
    new_values={"$set":new_data}
    collection.update_one(query,new_values)

    return {
        
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps("updated")
    }
