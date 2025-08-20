import pytchat
import sys
import time
from obs_websocket import OBSWebsocketManager

class YoutubeChatHandler:
    def __init__(self, video_id:str):
        try:
            print(f"Connecting to stream with ID: {video_id}")
            self.chat = pytchat.create(video_id=video_id, interruptable=False)
            print("Connected!")
        except e:
            print("Error connecting to stream")
            time.sleep(5)
            sys.exit(1)

    def update_game_title(self, obs_handler: OBSWebsocketManager, source_name: str, prefix:str, message:str ):
        obs_handler.set_text(source_name, f"{prefix}\n{message}")

    def terminate(self):
        self.chat.terminate()