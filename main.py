from assets.ReelsGenerator import ReelsGenerator
from assets.PhotoGenerator import PhotoGenerator
import requests
import json
from instabot import Bot

# TODO:
    # 1. Instagram API in order to upload the reels
    # 2. voice scraper and the voice transformation automation
    # 3. video editing automation
    # 4. tiktok video scraper/downloader/bot




API_TEST = False

if __name__ == "__main__":
    #gen = ReelsGenerator()
    #gen._change_voice("assets/test_audio/test.wav")
    #gen._extract_audio("assets/test_audio/video.mp4")
    gen._replace_audio("assets/test_audio/video.mp4", "assets/test_audio/output.mp3")

    #gen._extract_audio("assets/test_audio/video.mp4")
    
    mail = "faday62620@tospage.com"
    password = "Nowyroczek2003"
    caption = "#sad,#story_of_my_life,#blackie"
    
    bot = Bot()
    bot.login()
    bot.upload_photo("C:/Users/DELL/Downloads/sad.jpg",caption)
    bot.logout()

if API_TEST:

    url = "http://api.convertio.co/convert"
    api_key = str('499d241aabe69c6edd749137b873e869')
    data = {
        'apikey' : api_key,
        'input' : 'upload'
    }
    files = { 'file' : 'C:/Users/DELL/Downloads/ssstik.io_1708124524510.mp4' }
    response = requests.post(url, json=data, files=files)

    response.raise_for_status()