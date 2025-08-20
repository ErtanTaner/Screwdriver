from obswebsocket import obsws, requests
import sys
import time


class OBSWebsocketManager:
    ws = None

    def __init__(self, host:str, port:int, password:str):
        self.ws = obsws(host, port, password, authreconnect=1)
        try:
            print(f"Connecting to {host}:{port}!")
            self.ws.connect()
            print("Connected!")
        except:
            print("Connection failed")
            time.sleep(5)
            sys.exit()
    
    def disconnect(self):
        self.ws.disconnect()
    
    def set_text(self, source_name:str, new_text:str):
            self.ws.call(requests.SetInputSettings(inputName=source_name, inputSettings = {'text': new_text}))

    def register(self, callback):
        self.ws.register(callback)