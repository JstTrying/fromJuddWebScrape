from page_source import PageSource
from page_parser import PageParser
from entry import Entry

class Crawler:

    spawns = 0
    __keyword = None
    __parser = None
    __questions = []
    __answers = []
    __url = []
    __entries = []

    def __init__(self, search):
        self.__parser = PageParser(keyword=search)
        Crawler.spawns = Crawler.spawns + 1

    def get_entries(self):
        return self.__entries

    def crawl(self):
        self.__questions = self.__parser.get_all_questions()
        self.__answers = self.__parser.get_all_answers()
        self.__url = self.__parser.get_all_url()
        self.__pack()

    def __pack(self):
        for i in range(0, len(self.__questions)):
            try:
                self.__entries.append(Entry(question=self.__questions[i], answer=self.__answers[i], url=self.__url[i]))
            except IndexError:
                pass

