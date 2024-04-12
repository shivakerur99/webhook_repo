from flask import Blueprint, json, request
from app import create_app
# from app.extensions import *


info = 'data from api'



app = create_app()

if __name__ == '__main__': 
    app.run(host="localhost",port=3000,debug=False)
    
    # always  put debug = False for logs







# Sometimes webhook was causing problems, 
# so keeping it for safety


# @app.route('/', methods=["GET"])
# def get_root():
#     return "All OK! in routes"

# @app.route('/github', methods=['GET','POST'])
# def gh_api():
#     global info

#     if(request.method == 'POST'):
#         print("1")
#         if(request.headers["Content-Type"]) == "application/json":
#             print("2")

#             dumpData = json.dumps(request.json)
#             info = json.loads(dumpData)
#             print("model data  : run.py \n :: ")
#             print(info)
#             postInfoToMongo(info)

#             return "Success"
#     else:
#         print("get")
#         print("0")
#         return info








