
from instabot import Bot
import requests

graph_url = 'https://graph.facebook.com/v19.0/'

class PhotoGenerator:

    

    def post_reel(caption='', media_type ='',share_to_feed='',thumb_offset='',video_url='',access_token = '',instagram_account_id=''):
        
        print(instagram_account_id)
        url = graph_url + instagram_account_id + '/media'
        #config.???
        print(url)
        param = dict()
        param['access_token'] = access_token
        param['caption'] = caption
        param['media_type'] = media_type
        param['share_to_feed'] = share_to_feed
        param['thumb_offset'] = thumb_offset
        param['video_url'] = video_url
        response =  requests.post(url,params = param)
        print("\n response",response.content)
        response = response.json()
    
        if 'id' in response:
            ig_container_id = response['id']
            return ig_container_id
        else:
            print("Odpowiedź nie zawiera identyfikatora 'id'.")
            return None
    
        #tu masz przypisac wartosc dobra do ig_container_id

    #{ wynik akurat tego 2 kroku, ale id masz przypisywac
    #  "status_code": "FINISHED",
    #  "id": "17889615691921648"
    #}

    def status_of_upload(ig_container_id = '',access_token=''):
        
        url = graph_url + ig_container_id
        param = {}
        param['access_token'] = access_token
        param['fields'] = 'status_code'
        response = requests.get(url,params=param)
        response = response.json()
        return response #if "FINISHED" to zajebscie, przypisac id do creation_id

    def publish_container(creation_id = '',access_token = '',instagram_account_id=''):
        
        url = graph_url + instagram_account_id + '/media_publish'
        param = dict()
        param['access_token'] = access_token
        param['creation_id'] = creation_id
        response = requests.post(url,params=param)
        response = response.json()
        return response   


