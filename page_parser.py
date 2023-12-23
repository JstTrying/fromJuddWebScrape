import time

from bs4 import BeautifulSoup
from page_source import PageSource

class PageParser:

    __html = None

    def __init__(self, keyword):
        text = PageSource(search_keyword=keyword)
        time.sleep(1)
        self.__html = BeautifulSoup(str(text), 'html5lib')


    def get_all_questions(self):
        list = []
        container = self.__html.find_all('span', attrs={"class": "C7GS5b rkGIWe"})
        for entry in container:
            list.append(entry.find_next("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).text)
        return list

    def get_all_answers(self):
        list = []
        container = self.__html.find_all('span', attrs={"class": "C7GS5b rkGIWe"})
        for entry in container:
            try:
                answer = entry.find_next_sibling("div", attrs={"class": "kCrYT"}).find_next("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"}).find_next("div", attrs={"class": "BNeawe s3v9rd AP7Wnd"})
                list.append(answer.text)
            except AttributeError:
                pass
        return list

    def get_all_url(self):
        list = []
        container = self.__html.find_all("div", attrs={"class": "BNeawe UPmit AP7Wnd UwRFLe"})
        for entry in container:
            try:
                answer = entry.text
                list.append(answer)
            except AttributeError:
                pass
        return list