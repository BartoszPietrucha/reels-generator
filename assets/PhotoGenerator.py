
from instabot import Bot

class PhotoGenerator:
    App_ID = "748625023889082"
    App_Secret = "71f4dad9d8d84071a634790d35069acd"

    def __init__(self):
        self.bot = Bot()

    def login(self, log_pass):
        self.bot.login(*log_pass)

    def upload_photo(self, photo_path, caption):
        self.bot.upload_photo(photo_path, caption)

    def logout(self):
        self.bot.logout()

