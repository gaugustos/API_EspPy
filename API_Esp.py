
from operator import truediv
from flask import Flask, request, jsonify


from main import ConfirmRequestData ,ReadDB ,DBwrite

app = Flask(__name__)


@app.route('/')
def homepage():
    
    return "render_template"


@app.route('/GET_Output_Staus', methods =['POST'])

#       Recive
#   ID_User
#   ID_Board - ID_BD
#   HASH

#       Output
#   JSON - {"OUTPUT[x]" : "value"}

def GetOutputStatus():

    Data = request.get_json()
    #print(Data)
    
    confirmation = ConfirmRequestData(Data["ID_User"], Data["ID_Board"], Data["HASH"])

    if(ConfirmRequestData(confirmation)):

        DBanswer = ReadDB(Data["ID_Board"])

        return DBanswer
    #return "OK"


@app.route('/POST_Output_Staus', methods =['POST'])


#       Send
#   ID_User
#   ID_Board
#   HASH
#   Outputs

#       Output
#   JSON - {"OUTPUT[x]" : "OK"}


def PostOutputStatus():

    Data = request.get_json()

    print(Data)
    DBwrite(Data)
    return "render_template"

    

app.run()