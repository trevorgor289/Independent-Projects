import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# contains a class that will click each boardgame link on main webpage to access more detailed information on each game

class DifficultyScore:

    def __init__(self, url):
        self.url = url
        self.bg_links_2 = []
        self.difficulty_list = []

    def get_links(self):
        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        # finding each link for top 100 board games
        anchor_tags = soup.find_all(name="a")
        links = []
        for tag in anchor_tags:
            link = tag.get('href', None)
            if link != None:
                links.append(link)
        bg_links = []
        for item in links:
            if item == '#':
                continue
            items = item.split("/")
            for element in items:
                if element.isspace() or element == '':
                    items.remove(element)
            if items[0] == 'boardgame':
                seperator = '/'
                result = seperator.join(items)
                bg_links.append(result)

        bg_links_2 = []
        URL2 = 'https://boardgamegeek.com/'

        for link in bg_links:
            result = URL2 + link
            bg_links_2.append(result)

        bg_links_2 = bg_links_2[::2]
        self.bg_links_2 = bg_links_2
        return self.bg_links_2

    def retrieve_difficulty_score(self):
        service = Service(r"C:\Users\tgord\OneDrive\Desktop\development\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        for link in self.bg_links_2:
            driver.get(link)
            site = driver.page_source
            soup = BeautifulSoup(site, 'html.parser')
            rating = soup.find_all("script")
            n_lst = []
            x = 0
            for script in rating:
                if script.contents:
                    string = str(script)
                    n_lst.append(str(x) + string)
                    x += 1
            for item in n_lst:
                if item.find("GEEK = GEEK") != -1:
                    index_start_value = item.index("averageweight")
                    difficulty = item[(index_start_value + 15): (index_start_value + 20)]
                    self.difficulty_list.append(difficulty)
        return self.difficulty_list
