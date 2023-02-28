# Approach Two: Issue, rule, rule, application, conclusion
from chatgpt_wrapper import ChatGPT
import json

with open("./processedData/processedJsonData.txt") as read_file:
    file_data_list = read_file.readlines()

    #initialize a list for prompt data
    prompt_data = []
    for file_data in file_data_list:
        file_data_json = json.loads(file_data)
        curr_file_data = file_data_json["dataset"]["pair"]
        prompt_data.extend(curr_file_data)

    print("Number of prompts: ", len(prompt_data))

    # go through the list of all prompts, ask each one to ChatGPT and get the answer
    bot = ChatGPT()
    for prompt_obj in prompt_data:
        premise = prompt_obj["t1"]
        hypothesis = prompt_obj["t2"]
        response = bot.ask("Please analyze if the hypothesis is True or False according to the given legal reasoning approach. "
                           + "\n Approach: Issue, rule, rule, application, conclusion.  \n\n Premise: \n"
                           + premise + "\nHypothesis: \n" + hypothesis)
        print(response)
        prompt_obj["ChatGPT_output"] = response

    # write to result file
    result_json = json.dumps(prompt_data)
    result_json_file = open("./results/resultsDataJson.json", "w")
    result_json_file.write(result_json)
    result_json_file.close()