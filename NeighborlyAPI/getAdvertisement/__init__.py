import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            url = "mongodb://nd2hospitalcosmos:AfxPATz1CbyX6S8jSZZl7raUblTkB6OLjeWJYsXqxFAgYumFzt9AHeFpGd3GGscLoGyjdItswYA2P30xm6hA0w==@nd2hospitalcosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@nd2hospitalcosmos@"
            client = pymongo.MongoClient(url)
            database = client['nd2hospitaldb']
            collection = database['advertisements']
           
            query = {'_id': str(id)}
            result = collection.find_one(query)
            print("----------result--------")

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)