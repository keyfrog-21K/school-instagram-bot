# instagram_uploader.py
from instagrapi import Client
import dotenv
import os

dotenv.load_dotenv()
name = os.getenv('INSTAGRAM_USERNAME')
pw = os.getenv('INSTAGRAM_PASSWORD')

client = Client()


class instagramUploader:
    def __init__(self, path, caption):
        self.path = path
        self.caption = caption
        client.login(username=name, password=pw)

    def upload(self):
        client.photo_upload(self.image_path, self.caption)
