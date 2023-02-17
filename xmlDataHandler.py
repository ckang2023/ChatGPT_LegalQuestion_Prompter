import xmltodict
import os
import json


class xmlDataHandler():
    def __init__(self):
        self.directory = "./xmlData"

    def xmlToJson(self):
        json_obj_list_file = open("./processedData/processedJsonData.txt", "w")

        for filename in os.listdir(self.directory):
            f = os.path.join(self.directory, filename)

            if os.path.isfile(f):
                with open(f) as xml_file:
                    # convert to dict first
                    data_dict = xmltodict.parse(xml_file.read())
                    json_data = json.dumps(data_dict)

                    # write json obj to text tile
                    json_obj_list_file.write(json_data)
                    json_obj_list_file.write("\n")

        json_obj_list_file.close()