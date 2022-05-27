from flask import Flask,request
import json
import math
#creating Flask App
app = Flask(__name__)
#signup route
@app.route('/signup', methods=['POST'])
def register():  
    data=request.get_json()
    #if data have mobile number and firstname and lastname
    if(data['mobile_number'][0]=='+'  and data["first_name"] and data["last_name"]):
      return {"status":"success","otp":65890}
    else:
     return {"status":"failure","response":"invalid_data"}
#validate otp
@app.route('/validate_otp', methods=['POST'])
def validateOtp():
    data=request.get_json()
    #otp verified
    if(data["otp"]==65890):
        return {"status":"verified"}
    else:
      return {"status":"invalid_otp"}
#createAccount detials required
@app.route("/createAccount", methods=['GET'])
def details_for_account():
        return {"details_required":["first_name","last_name","father_name","date_of_birth","permanent_address","current_address"]}
app.run()
