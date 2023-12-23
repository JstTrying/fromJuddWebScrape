import threading
from crawler import Crawler

class QueryManager:

    question_list = []
    entry_set = set()
    current_index = 0;
    keyword = ""

    def __init__(self, keyword):
        QueryManager.question_list.append(keyword)

    def start(self):
        for i in range(20):
            x = threading.Thread(target=self.__spawn_crawler())
            x.start()
            x.join()

    def get_entries(self):
        return QueryManager.entry_set

    def __spawn_crawler(self):
        crawler = Crawler(QueryManager.question_list[-1])
        crawler.crawl()
        for entry in crawler.get_entries():
            QueryManager.question_list.append(entry.question)
            QueryManager.entry_set.add(entry)
        QueryManager.current_index = len(QueryManager.entry_set)

