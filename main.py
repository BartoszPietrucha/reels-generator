from assets.ReelsGenerator import ReelsGenerator
from assets.PhotoGenerator import PhotoGenerator
from assets.VideoScraper import VideoScraper
from assets.VideoDownloader import VideoDownloader, get_desktop_path
from assets.ReelsStealer import ReelsStealer
import requests
import json
from instabot import Bot
import time

# TODO:
    # 1. Instagram API in order to upload the reels
    # 2. voice scraper and the voice transformation automation
    # 3. video editing automation
    # 4. tiktok video scraper/downloader/bot

access_token = 'EAAEDdKLp9ZBsBO1RATRORud4o1xwgLIDRYc9owHBtD7lFoFXpyL4Lcmf7f007oBiB1mJ03heetjLPrGkvZCwbNXyGFxxN9ajIrSnyn8VP5M7VlNa7k3Wn1S5Vrh6QBd24y7olflYeSbZAZCH1xfdLJqML6d0rtnZChxCUZCNy2QTAOZB2x2YKrq7XTADLNWIZAFoKUxYEOCQL8r0cLWZB5ilig9IUOFQZD'
caption = 'First_Reel'
instagram_account_id = '17841464578507975'
media_type = 'REELS'
graph_url = 'https://graph.facebook.com/v19.0/'
video_url = 'https://youtube.com/shorts/aRRghrlQxxA?si=P9CevM4Va2v2kvJx'
thumb_offset = 1
share_to_feed = True


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


        ig_container_id = PhotoGenerator.post_reel(caption, media_type,share_to_feed,thumb_offset,video_url,access_token,instagram_account_id)
        time.sleep(5)

        y = PhotoGenerator.status_of_upload(ig_container_id,access_token)
        print(y["status_code"])


        if y["status_code"] == "FINISHED":
            creation_id = y["id"]
            z = PhotoGenerator.publish_container(creation_id,access_token,instagram_account_id)

    if SCRAPER_TEST:
        desktop_path = get_desktop_path()
        scraper = VideoScraper("assets/data/tiktok.txt")
        downloader = VideoDownloader(f"{desktop_path}\\TikTokVideos")
        for link in scraper.links[:3]:
            downloader.download_video(link)

    if STEALER_TEST:
        stealer = ReelsStealer("assets/data/stories.txt")
        stealer.steal_reel()

        

