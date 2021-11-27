import json
import database

db = database.get_database()

collection = db['Activity']


def lambda_handler(event, context):
    output={}
    list = collection.find({},{'_id': False}).sort( "date",-1 )
    for item in list:
        output[item['title']]=item
    output={k: v for k, v in sorted(output.items(), key=lambda item: item[1]['importance'],reverse=True)}
    print(output)
    
    return {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps(output, default=str)
} 
    
