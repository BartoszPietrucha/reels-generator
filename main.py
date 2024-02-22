from assets.ReelsGenerator import ReelsGenerator
from assets.PhotoGenerator import PhotoGenerator
from assets.VideoScraper import VideoScraper
from assets.VideoDownloader import VideoDownloader, get_desktop_path
from assets.ReelsStealer import ReelsStealer
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
VIDEO_TEST = True
SCRAPER_TEST = False
STEALER_TEST = False

if __name__ == "__main__":
    if VIDEO_TEST:
        gen = ReelsGenerator()
        gen._create_srt()
    
    

    if API_TEST:

        mail = "faday62620@tospage.com"
        password = "Nowyroczek2003"
        caption = "#sad,#story_of_my_life,#blackie"
        
        bot = Bot()
        bot.login()
        bot.upload_photo("C:/Users/DELL/Downloads/sad.jpg",caption)
        bot.logout()

    if SCRAPER_TEST:
        desktop_path = get_desktop_path()
        scraper = VideoScraper("assets/data/tiktok.txt")
        downloader = VideoDownloader(f"{desktop_path}\\TikTokVideos")
        for link in scraper.links[:3]:
            downloader.download_video(link)

    if STEALER_TEST:
        stealer = ReelsStealer("assets/data/stories.txt")
        stealer.steal_reel()

        

