import json
import sys
import premiseHypothesisPrompter
import approachPremiseHypothesisPrompterOne
import approachPremiseHypothesisPrompterTwo
import approachPremiseHypothesisPrompterThree



def chatGPTPrompter(prompterName):
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


