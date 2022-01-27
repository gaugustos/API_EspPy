
from operator import truediv
from flask import Flask, request, jsonify


from main import ConfirmRequestData ,ReadDB ,DBwrite

app = Flask(__name__)


@app.route('/')
def homepage():
    
    return "render_template"


@app.route('/GET_Output_Staus', methods =['GET'])

#       Recive
#   ID_User
#   ID_Board - ID_BD
#   HASH

#       Output
#   JSON - {
#            ID_Outputs         : Value 
#            Value_Sensor_1     : Value
#            Value_Sensor_2     : Value
#            Value_Sensor_3     : Value
#            Last_Update        : Value
# }

def GetOutputStatus():

    Data = request.get_json()
    print(Data)
    
    #confirmation = ConfirmRequestData(Data["ID_User"], Data["ID_Board"], Data["HASH"])

   # if(ConfirmRequestData(confirmation)):

  #      DBanswer = ReadDB(Data["ID_Board"])
#
  #      return DBanswer
    return "OK"


@app.route('/POST_Output_Staus', methods =['POST'])


#       Send
#   ID_User
#   ID_Board
#   ID_Outputs
#   ID_HASH
#   Value_Sensor_1
#   Value_Sensor_2
#   Value_Sensor_3
#   Last_Update

#       Output
#   JSON - {"OK"}


def PostOutputStatus():

    Data = request.get_json()

    print(Data)
    DBwrite(Data)
    return "ok"

    

app.run()