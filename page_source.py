from selenium import webdriver
from selenium.webdriver.common.by import By

class PageSource:

    __driver = None
    __keyword = None

    def __init__(self, search_keyword):
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        options.add_argument('--disable-javascript')
        options.add_argument("--headless=new")
        prefs = {}
        prefs["webkit.webprefs.javascript_enabled"] = False
        prefs["profile.content_settings.exceptions.javascript.*.setting"] = 2
        prefs["profile.default_content_setting_values.javascript"] = 2
        prefs["profile.managed_default_content_settings.javascript"] = 2
        options.add_experimental_option("prefs", prefs)
        self.__driver = webdriver.Chrome(options=options);
        self.__driver.get("https://www.google.com")
        self.__keyword = search_keyword
        self.__get_search_field().send_keys(self.__keyword)
        self.__get_search_button().submit()

    def __get_html(self):
        return str(self.__driver.page_source)

    def __get_search_field(self):
        return self.__driver.find_element(by=By.NAME, value="q")

    def __get_search_button(self):
        return self.__driver.find_element(by=By.NAME, value="btnK")

    def __str__(self):
        return str(self.__get_html())
