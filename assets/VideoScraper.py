from bs4 import BeautifulSoup


class VideoScraper:
    """
    Finds all the links to the videos on the tiktok profile.

    This class filters the html file saved from the tiktok page //account// and finds all the links to the videos.
    Used to feed the ReelsGenerator database with links to the videos.
    """

    def __init__(self, url):
        self.url = url
        self.links = []
        self.find_links(self.url)


    def read_html(self, file_path: str) -> str:
        """Reads the html file and returns the content as a string."""
        with open(file_path, "r", encoding="utf8") as file:
            links = file.read()
            return links
        

    def find_links(self, html: str) -> None:
        """Filters for the links to the videos and saves them in the links list."""
        data = self.read_html(html)
        soup = BeautifulSoup(data, "html.parser")
        links = soup.find_all("a")
        for link in links:
            if "/video/" in link["href"] and link["href"] not in self.links:
                self.links.append(link["href"])






    
        


        

        


    