import eventlet

from flask import Flask, render_template
from flask import request

import json
import xmltodict
import premiseHypothesisPrompter
import approachPremiseHypothesisPrompterOne
import approachPremiseHypothesisPrompterTwo
import approachPremiseHypothesisPrompterThree
from flask_socketio import SocketIO

eventlet.monkey_patch()
app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("homePage.html")

@app.route("/prompt-response", methods = ['GET', 'POST'])
def chatGPTPrompter():
    '''
    Prompting to chatGPT using uploaded test_data.
    '''

    approach = request.form.get("approachSelection")
    if request.method == "POST":
        test_data = request.files["test_data"]
        xml_file = test_data.read()
        # get json-structure-like dictionary from xml_file
        data_dict = xmltodict.parse(xml_file)
        # get list of objects
        data_list = data_dict["dataset"]["pair"]

    if approach == "approachZeroPrompter":
        prompter = premiseHypothesisPrompter.approachZeroPrompter()
        result = prompter.promptData(data_list)
    elif approach == "approachOnePrompter":
        prompter = approachPremiseHypothesisPrompterOne.approachOnePrompter()
        result = prompter.promptData(data_list)
    elif approach == "approachTwoPrompter":
        prompter = approachPremiseHypothesisPrompterTwo.approachTwoPrompter()
        result = prompter.promptData(data_list)
    elif approach == "approachThreePrompter":
        prompter = approachPremiseHypothesisPrompterThree.approachThreePrompter()
        result = prompter.promptData(data_list)
    else:
        return "Invalid prompter name"

    resultJson = json.loads(result)
    numResponses = len(resultJson)

    return render_template("responsePage.html", numResponses=numResponses, result=resultJson)


if __name__ == "__main__":
    local_ip = "127.0.0.1"  # Use the loopback address
    local_port = 5000  # The default Flask port is 5000

    print(f"Running on http://{local_ip}:{local_port}/")

    socketio.run(app, host=local_ip, port=local_port)
