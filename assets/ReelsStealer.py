from assets.VideoScraper import VideoScraper
from assets.VideoDownloader import VideoDownloader, get_desktop_path
from assets.ReelsGenerator import ReelsGenerator
import os
import shutil
from time import sleep

DESKTOP_PATH = get_desktop_path()

class ReelsStealer:

    def __init__(self, html_file : str, output_dir: str = f"{DESKTOP_PATH}\\StolenReels", temp_dir: str = f"{DESKTOP_PATH}\\TikTokVideos"):
        self.output_dir = output_dir
        self.temp_dir = temp_dir
        self.video_links = VideoScraper(html_file).links
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


    def steal_reel(self):
        downloader = VideoDownloader(self.temp_dir)
        gen = ReelsGenerator(self.output_dir, self.temp_dir)
        for link in self.video_links[:2]:           # TEMPORARY FOR FIRST 3 VIDEOS
            print(link)
            downloader.download_video(link)
            print("DOWNLOADED, ", os.listdir(self.temp_dir)[0])
            gen._edit_video(f"{self.temp_dir}\\{os.listdir(self.temp_dir)[0]}")
            sleep(1)
            if len(os.listdir(self.temp_dir)) < 6:
                print("DELETING")
                shutil.rmtree(self.temp_dir)
            sleep(1)
        return True


