from pymongo import MongoClient

# Setup MongoDB here
uri = "mongodb+srv://shivakerur99:shivanand99805257@cluster0.usva3cf.mongodb.net/webhook"





database_data = {
    "eventType" : "",
    "author":"",
    "fromBranch":"",
    "toBranch":"",
    "timestamp":""
}





mongo_schema = {
    'eventType' : {
        'type' : 'string',
        'required' : True,
    },
    'author' : {
        'type' : 'string',
        'required' : True,
    },
    'fromBranch' : {
        'type' : 'string',
        'required' : True,
    },
    'toBranch' : {
        'type' : 'string',
        'required' : True,
    },
    'timestamp' : {
        'type' : 'string',
        'required' : True,
    }
}


def parse_Info_for_mongo(infoModel):
    try:
        latest_Commit = infoModel["head_commit"]
        eventType = infoModel["eventType"]
        
        authorName = latest_Commit["author"]["name"]
        fromBranch = infoModel["ref"]
        toBranch = infoModel["ref"]
        timeStamp = latest_Commit["timestamp"]

        data_mongo = {
            "eventType" : eventType,
            "author": authorName,
            "fromBranch": fromBranch,
            "toBranch" : toBranch,
            "timestamp" : timeStamp,
        }

        return data_mongo
    
    except KeyError as e:
        print(f"KeyError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def postInfoToMongo(dataModel): 

    client = MongoClient(uri)
    database = client.webhooks
    collection = database.get_collection('github-webhooks')

    
    data_mongo = parse_Info_for_mongo(dataModel)


    try:

        collection.insert_one(data_mongo)
        print("Added data_mongo to MongoDB database")
        
        client.close()
        

    except Exception as e:
        print("Error : Exception")
        print(e)    


def get_mongo_data():
    client = MongoClient(uri)
    database = client.webhooks
    try:
        collection = database.get_collection('github-webhooks')
        cursor = collection.find({})
        data = []
        for data_mongo in cursor:
            data.append(data_mongo)
        data.reverse()

        client.close()
        
        return data[0]

    except Exception as e:
        print("Error : Exception")
        print(e)    


   

