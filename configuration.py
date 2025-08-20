import json

class Config: 
    def __init__(self, prefix:str, password:str, video_id:str, source_name:str):
        self.prefix = "Oyun:"
        self.host = "localhost"
        self.port = 4455
        self.password = password
        self.video_id = video_id
        self.source_name = source_name

    def update_config(self, path:str):
        final = dict()
        for k, v in self.__dict__.items():
            final[k] = v
        with open(path, "w") as f:
            json.dump(final, f)
    
    def ask_for_config(self):
        prefix = input("Enter the prefix for the chat messages: ")
        if prefix != "":
            self.prefix = prefix
        password = input("Enter the OBS password: ")
        if password != "":
            self.password = password
        video_id = input("Enter the video ID: ")
        if video_id != "":
            self.video_id = video_id 
        source_name = input("Enter the source name: ")
        if source_name != "":
            self.source_name = source_name
        self.update_config("config.json")

    def __str__(self):
        return f"Prefix: {self.prefix}\nPassword: {self.password}\nVideo ID: {self.video_id}\nHost: {self.host}\nPort: {self.port}\nSource Name: {self.source_name}"

def load_config(path:str):
        with open(path, "r") as f:
            return json.load(f)