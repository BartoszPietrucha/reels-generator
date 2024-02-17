from assets.ReelsGenerator import ReelsGenerator
import requests
import json

API_TEST = False

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

    if( response.status_code != requests.codes.created):
        print("not so good")
    else:
        print(response.json())