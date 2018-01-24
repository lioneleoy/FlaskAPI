#Author: Lionel Raja
#Puropose: used for external automation and workflows

#import modules
from flask import Flask,jsonify,request
import datetime
from datetime import datetime,timedelta
import wmi
import WindowsService


app = Flask(__name__)

author ="Lionel"
desc = "Used for external automation"
usage_det = "/help"
version = "v1.1"

@app.route('/',methods=['GET'])
def home():
    return jsonify({'author':author,'description':desc,'usage info': usage_det,'version':version})

@app.route('/api',methods=['GET'])
def help():
    functions =[{'service':'/service','usage':"/service/<service name>",'desc':"gives status of the service"}]
    return jsonify({'options':functions})

@app.route('/api/<string:name>',methods=['GET'])
def list_selected(name):
    if name == 'service':
        usage =[{'method':'POST','usage':"/service/<service name>",'desc':"gives status of the service"}]
        return jsonify({'usage':usage})
    else:
        return jsonify({'error': "/api for available options"})

@app.route('/service/<string:service_name>',methods=['GET'])
def serviceStatus(service_name):
    status, status_c= WindowsService.serviceStatus(service_name)
    return jsonify({'serviceName:':service_name,'status':status,'code':status_c})


if __name__ =='__main__':
    app.run(debug =True, port=8080)