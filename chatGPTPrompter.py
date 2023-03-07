import json
import sys
import premiseHypothesisPrompter
import approachPremiseHypothesisPrompterOne
import approachPremiseHypothesisPrompterTwo
import approachPremiseHypothesisPrompterThree



def chatGPTPrompter(prompterName):
    '''
    Sends the processed data in processedData/processedJsonData.txt to ChatGPT,
    and you will see outputs listed here as they're processed. 

    Execute this function by typing
        python3 <FUNCTION NAME> <approach>
    where <approach> can be "Zero", "One", "Two", or "Three". The difference
    between these approaches is listed below:

    Zero: Zero-shot approach. The question asked is simply "Please determine if 
    the following hypothesis is True or False based on the given premise."

    One: TRRAC Format. The question asked is "Please analyze if the hypothesis is
    True or False according to the given legal reasoning approach. Thesis, 
    rule, rule, application, conclusion."

    Two: IRRAC Format. The question asked is "Please analyze if the hypothesis is
    True or False according to the given legal reasoning approach. Issue, 
    rule, reasoning, application, conclusion. 

    Three: IRREAC Format. The question asked is "Please analyze if the hypothesis is
    True or False according to the given legal reasoning approach. Issue, 
    rule, reasoning, application, conclusion. 
    '''
    # get processed data
    with open("./processedData/processedJsonData.txt") as read_file:
        file_data_list = read_file.readlines()

        #initialize a list of test data for prompting
        test_data = []
        for file_data in file_data_list:
            file_data_json = json.loads(file_data)
            curr_file_data = file_data_json["dataset"]["pair"]
            test_data.extend(curr_file_data)

    if prompterName == "approachZeroPrompter":
        prompter = premiseHypothesisPrompter.approachZeroPrompterPrompter()
        prompter.promptData(test_data)
    elif prompterName == "approachOnePrompter":
        prompter = approachPremiseHypothesisPrompterOne.approachOnePrompter()
        prompter.promptData(test_data)
    elif prompterName == "approachTwoPrompter":
        prompter = approachPremiseHypothesisPrompterTwo.approachTwoPrompter()
        prompter.promptData(test_data)
    elif prompterName == "approachThreePrompter":
        prompter = approachPremiseHypothesisPrompterThree.approachThreePrompter()
        prompter.promptData(test_data)
    else:
        print("Invalid prompter name")
        return

if __name__ == "__main__":
    chatGPTPrompter(str(sys.argv[1]))


