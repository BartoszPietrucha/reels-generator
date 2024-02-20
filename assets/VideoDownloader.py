import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from time import sleep


class VideoDownloader:
    ENDPOINT = "https://ssstik.io/pl"

    def __init__(self):
        self.driver = Chrome()
        self.driver.get(self.ENDPOINT)
        sleep(30)

