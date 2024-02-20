from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import winreg
import os
import shutil

COOKIES_BUTTON_CLASS = "fc-button-label"
COOKIES_BUTTON_XPATH = "/html/body/div[4]/div[2]/div[1]/div[3]/div[2]/button[1]/p"

INPUT_ID = "main_page_text"
INPUT_XPATH = "/html/body/main/section[1]/div/div/form/div[2]/input[1]"

BUTTON_ID = "submit"
BUTTON_XPATH = "/html/body/main/section[1]/div/div/form/div[2]/button[3]"

NO_WATERMARK_XPATH = "/html/body/main/section[1]/div/div/div[3]/div/div/div[2]/a[1]"

TEST_LINK = "https://www.tiktok.com/@scalingstories/video/7336009476165700906?lang=en"

KEYPATH = "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders"

def get_desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYPATH, 0, winreg.KEY_READ)
    try:
        value, _ = winreg.QueryValueEx(key, "Desktop")
        return value
    except Exception as e:
        print(f"Error: {e}")
    finally:
        winreg.CloseKey(key)
    return None


# TODO:
    # Add the synchronization, and waiting for the current process to finish.



class VideoDownloader:
    """
    Downloads the video from the tiktok link.

    Creates a temporary directory on the user's desktop and downloads the video from the given link.
    """
    ENDPOINT = "https://ssstik.io/pl"
    
    
    def __init__(self, output_dir: str):
        self.desktop_path = get_desktop_path()
        self.output_dir = output_dir
        self.options = Options()
        self.options.add_extension('assets/data/extensions/adblock.crx')  # Path to the adblock CRX file
        prefs = {
            "download.default_directory": f"{self.output_dir}",
            "download.prompt_for_download": False,  
            "download.directory_upgrade": True,  
            "safebrowsing.enabled": True  
        }
        self.options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=self.options)
        self.ext_installed = False

    
    def download_video(self, link: str) -> bool:
        """Runs the download process."""
        self._initialize_download()             # Creating a temporary directory for the downloads
        if not self.ext_installed:
            self.driver.get("https://google.com")   # Pre-opening in order to install the adblock extension
            sleep(10)
            self.ext_installed = True

        self.driver.get(self.ENDPOINT)
        self._accept_cookies()
        self._fill_input(link)
        if self._click_submit():
            sleep(3)
            if self._click_no_watermark():
                while not self._is_downloaded():        # Waiting for the download to finish
                    sleep(3)
        #if len(os.listdir(self.output_dir)) == 1:
            #shutil.rmtree(self.output_dir, ignore_errors=True)  # Removing the temporary directory
        return True

        

    def _accept_cookies(self) -> bool:
        """Accepts the cookies."""
        try:
            self.driver.find_element(By.CLASS_NAME, COOKIES_BUTTON_CLASS).click()
        except Exception:
            return False
        return True
    
    
    def _fill_input(self, link: str) -> bool:
        """Fills the input with the link to the video."""
        try:
            self.driver.find_element(By.ID, INPUT_ID).send_keys(link)
        except Exception:
            return False
        return True
    

    def _click_submit(self) -> bool:
        """Clicks the button to submit the link."""
        try:
            self.driver.find_element(By.ID, BUTTON_ID).click()
        except Exception:
            return False
        return True
    

    def _click_no_watermark(self) -> bool:
        """Clicks the button to download the video without the watermark."""
        try:
            self.driver.find_element(By.XPATH, NO_WATERMARK_XPATH).click()
        except Exception:
            return False
        return True
    

    def _initialize_download(self) -> None:
        """Creates a temporary directory for the downloads."""
        if not os.path.exists(f"{self.output_dir}"):
            os.mkdir(f"{self.output_dir}")


    def _is_downloaded(self) -> bool:
        """Checks if the video is downloaded."""
        for f in os.listdir(f"{self.output_dir}"):
            if f.endswith(".mp4"):
                return True
        return False
    

    def set_output_dir(self, dir):
        self.output_dir = dir


