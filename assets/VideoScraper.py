from bs4 import BeautifulSoup
import time



class VideoScraper:

    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup()
        self.links = []


    def read_html(self, file_path):
        with open(file_path, "r") as file:
            links = file.readlines()
            return links
        

    def find_links(self, html):
        pass


    # TODO:
        # 1. scrape on the html file 





    
        


        

        


    