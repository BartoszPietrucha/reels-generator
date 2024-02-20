from assets.VideoScraper import VideoScraper
from assets.VideoDownloader import VideoDownloader, get_desktop_path
from assets.ReelsGenerator import ReelsGenerator
import os
import shutil

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
        for link in self.video_links[:3]:           # TEMPORARY FOR FIRST 3 VIDEOS
            downloader.download_video(link)
            gen._edit_video(f"{self.temp_dir}\\{os.listdir(self.temp_dir)[0]}")
            if len(os.listdir(self.temp_dir)) < 6:
                shutil.rmtree(self.temp_dir, ignore_errors=True)
        return True

