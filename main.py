from assets.ReelsGenerator import ReelsGenerator
from assets.PhotoGenerator import PhotoGenerator
from assets.VideoScraper import VideoScraper
import requests
import json
from instabot import Bot

# TODO:
    # 1. Instagram API in order to upload the reels
    # 2. voice scraper and the voice transformation automation
    # 3. video editing automation
    # 4. tiktok video scraper/downloader/bot



ENDPOINT = "https://www.tiktok.com/@scalingstories"
API_TEST = False
VIDEO_TEST = False
SCRAPER_TEST = True

if __name__ == "__main__":
    if VIDEO_TEST:
        gen = ReelsGenerator()
        gen._change_voice("assets/test_audio/test.wav")
        gen._extract_audio("assets/test_audio/video.mp4")
        gen._replace_audio("assets/test_audio/video.mp4", "assets/test_audio/output.mp3")
    
    

    if API_TEST:

        mail = "faday62620@tospage.com"
        password = "Nowyroczek2003"
        caption = "#sad,#story_of_my_life,#blackie"
        
        bot = Bot()
        bot.login()
        bot.upload_photo("C:/Users/DELL/Downloads/sad.jpg",caption)
        bot.logout()

    if SCRAPER_TEST:
        scraper = VideoScraper("https://www.tiktok.com/@scalingstories")