from obs_websocket import OBSWebsocketManager
from youtube_chat import YoutubeChatHandler
from configuration import Config, load_config
import os
import logging
import time
import sys

config = load_config("config.json")
config = Config(config["prefix"], config["password"], config["video_id"], config["source_name"])
config.ask_for_config()

logging.basicConfig(level=logging.CRITICAL)
if len(sys.argv) > 1 and sys.argv[1] == "--debug":
    logging.basicConfig(level=logging.DEBUG)

def on_event(message):
    print("Got message: {}".format(message))

obs_handler = OBSWebsocketManager(config.host, config.port, config.password)
youtube_handler = YoutubeChatHandler(config.video_id)

obs_handler.register(on_event)

try:
    while youtube_handler.chat.is_alive():
        for c in youtube_handler.chat.get().sync_items():
            if (c.author.isChatModerator or c.author.isChatOwner) and (config.prefix in c.message ):
                game_title = c.message.split(":")[1]
                print(f"Title changed to {game_title.lstrip()}")
                youtube_handler.update_game_title(obs_handler, "Yazı6", config.prefix, game_title.lstrip())

except KeyboardInterrupt:
    print("Exiting...")
    obs_handler.disconnect()
    youtube_handler.terminate()

