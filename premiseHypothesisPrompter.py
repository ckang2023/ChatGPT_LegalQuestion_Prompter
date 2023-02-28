from chatgpt_wrapper import ChatGPT
import json

class approachZeroPrompter(object):
    def __init__(self):
        self.bot = ChatGPT()

    def promptData(self, prompt_data):
        print("Number of prompts: ", len(prompt_data))

        for prompt_obj in prompt_data:
            premise = prompt_obj["t1"]
            hypothesis = prompt_obj["t2"]
            response = self.bot.ask("Please determine if the following hypothesis is True or False based on the given premise. \n Premise: \n"
                + premise + "\nHypothesis: \n" + hypothesis)
            print(response)
            prompt_obj["ChatGPT_output"] = response

        # write to result file
        result_json = json.dumps(prompt_data)
        result_json_file = open("./results/resultsDataJson.json", "w")
        result_json_file.write(result_json)
        result_json_file.close()