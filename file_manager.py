import json
import os.path

class FileManager:

    def write_to_file(self, file_name, text):
        file = open(file_name, "w")
        file.write(text)

    def read_from_file(self, file_name):
        file = open(file_name, "r")
        return file.read()

    def get_json(self, file_name):
        return json.loads(self.read_from_file(file_name))

    def write_to_json(self, file_name, data):
        self.write_to_file(file_name, json.dumps(data))


    def check_if_file_exists(self, file_name):
        return os.path.exists(file_name)


