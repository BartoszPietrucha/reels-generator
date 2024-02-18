from assets.ReelsGenerator import ReelsGenerator
import requests
import json

# TODO:
    # 1. Instagram API in order to upload the reels
    # 2. voice scraper and the voice transformation automation
    # 3. video editing automation
    # 4. tiktok video scraper/downloader/bot




API_TEST = True

if __name__ == "__main__":
    gen = ReelsGenerator()

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