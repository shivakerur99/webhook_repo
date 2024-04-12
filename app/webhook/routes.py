from flask import Blueprint, json, jsonify, request, render_template
import sched, time, datetime


from app.extensions import *


info = 'data from api'

webhook = Blueprint('Webhook', __name__)


@webhook.route('/', methods=["GET"])
def get_root():
    return render_template('index.html')



@webhook.route('/github', methods=['GET','POST'])
def get_gh_api():
    global info

    if(request.method == 'POST'):
        
        if(request.headers["Content-Type"]) == "application/json":
            eventType = request.headers["X-Github-Event"]
            
            dumpData = json.dumps(request.json)
            info = json.loads(dumpData)
            info["eventType"] = eventType
    
            postInfoToMongo(info)

            return "Success"
    else:
        
        return info


from flask import jsonify
import datetime

@webhook.route('/get-data', methods=['GET', 'POST'])
def get_data():
    data = get_mongo_data()

    author = data.get('author')
    event_type = data.get('eventType')
    from_branch = data.get('fromBranch', 'N/A')  
    to_branch = data.get('toBranch')
    timestamp = data.get('timestamp')

    if timestamp:
        timestamp = datetime.datetime.fromisoformat(timestamp)
        timestamp_str = timestamp.strftime("%A %B %d %Y %H:%M:%S")
    else:
        timestamp_str = 'N/A'

    data_mongo = {
        "author": author,
        "eventType": event_type,
        "fromBranch": from_branch,
        "toBranch": to_branch,
        "timestamp": timestamp_str
    }
    print(data_mongo)

    return jsonify(data_mongo)

