from flask import Flask, render_template
from flask import request, escape
from chatgpt_wrapper import ChatGPT
import json
import xmltodict
import premiseHypothesisPrompter
import approachPremiseHypothesisPrompterOne
import approachPremiseHypothesisPrompterTwo
import approachPremiseHypothesisPrompterThree
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    approach = str(escape(request.args.get("approachSelection", "")))
    test_data = str(escape(request.args.get("test_data", "")))

    return ("""
    <div id="homepage-general">
        <h1 id="homepage-title">Automatic ChatGPT Prompter</h1>
        <h3 id="homepage-section-title">Instructions</h3>
        <p class="homepage-text" style="text-indent: 25px;">
            Welcome to Automatic ChatGPT Prompter! 
            
            This prompter generates legal question prompts from your uploaded test file, feeds the prompts to ChatGPT, streams the responses, 
            and stores the test result as a JSON file in your local <b>/chatGPTPrompterResults</b> folder.
        </p>
        
        <p class="homepage-text" style="text-indent: 25px;">
            We have enabled prompting methods that makes ChatGPT answer the legal questions using specific approaches. 
            
            You can use the <b>"Approach Selection"</b> drop-down to set the approach you want chatGPT to use in answering your questions. 
            
            We are currently providing <b>four options</b>, representing <mark>four distinct approaches</mark>:
        </p> 
            
        <ul id="approach-explanation-list">
                <li><i>Zero</i>: Zero-shot approach. 
                <br>The question asked is simply "Please determine if 
                the following hypothesis is True or False based on the given premise."</li>
                <li><i>One</i>: Approach One is the TRRAC (Thesis, 
        rule, rule, application, conclusion) Format. The question asked is "Please analyze if the hypothesis is
        True or False according to the given legal reasoning approach. Thesis, 
        rule, rule, application, conclusion."</li>
                <li><i>Two</i>: Approach Two is the IRRAC (Issue, 
        rule, reasoning, application, conclusion) Format. The question asked is "Please analyze if the hypothesis is
        True or False according to the given legal reasoning approach. Issue, 
        rule, reasoning, application, conclusion."</li>
                <li><i>Three</i>: Approach Three is the IRREAC (Issue, 
        rule, reasoning, application, conclusion) Format. The question asked is "Please analyze if the hypothesis is
        True or False according to the given legal reasoning approach. Issue, 
        rule, reasoning, application, conclusion."</li>
        </ul>
            
        <p>After selecting an approach, please upload an <mark>.xml</mark> file containing your test data.
            <br><br>Then, press <b>"Prompt"</b> to see chatGPT's response.
        </p>
        
        <form action="/prompt-response" method="post" enctype = "multipart/form-data">
        
        <h3 id="homepage-section-title">Approach Selection</h3>
        <label for="approachSelection">Select an approach:</label>
        <select name="approachSelection" id="approachSelection">
          <option value="approachZeroPrompter">Approach Zero</option>
          <option value="approachOnePrompter">Approach One</option>
          <option value="approachTwoPrompter">Approach Two</option>
          <option value="approachThreePrompter">Approach Three</option>
        </select>

        <h3 id="homepage-section-title">Upload Test File</h3>
        <input type="file" name="test_data" id="test_data" accept=".xml">
        <input type="submit" value="Prompt">
        </form>
    </div>""" + approach + test_data)

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
    socketio.run(app, debug=True)
