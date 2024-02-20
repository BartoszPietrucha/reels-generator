from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

COOKIES_BUTTON_CLASS = "fc-button-label"
COOKIES_BUTTON_XPATH = "/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/button[1]/p"

INPUT_ID = "main_page_text"
INPUT_XPATH = "/html/body/main/section[1]/div/div/form/div[2]/input[1]"

BUTTON_ID = "submit"
BUTTON_XPATH = "/html/body/main/section[1]/div/div/form/div[2]/button[3]"

NO_WATERMARK_XPATH = "/html/body/main/section[1]/div/div/div[3]/div/div/div[2]/a[1]"

TEST_LINK = "https://www.tiktok.com/@scalingstories/video/7336009476165700906?lang=en"

options = Options()
options.add_extension('assets/data/extensions/adblock.crx')  # Ścieżka do pliku rozszerzenia



class VideoDownloader:
    ENDPOINT = "https://ssstik.io/pl"
    
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://google.com")
        sleep(10)
        self.driver.get(self.ENDPOINT)
        self._accept_cookies()
        self._fill_input(TEST_LINK)
        self._click_submit()
        sleep(5)
        self._click_no_watermark()
        sleep(10)
        
    def _accept_cookies(self) -> bool:
        try:
            self.driver.find_element(By.CLASS_NAME, COOKIES_BUTTON_CLASS).click()
        except Exception:
            return False
        return True
    
    def _fill_input(self, link: str) -> bool:
        try:
            self.driver.find_element(By.ID, INPUT_ID).send_keys(link)
        except Exception:
            return False
        return True
    
    def _click_submit(self) -> bool:
        try:
            self.driver.find_element(By.ID, BUTTON_ID).click()
        except Exception:
            return False
        return True
    
    def _click_no_watermark(self) -> bool:
        try:
            self.driver.find_element(By.XPATH, NO_WATERMARK_XPATH).click()
        except Exception:
            return False
        return True



