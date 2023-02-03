from RPA.Browser.Selenium import Selenium

from core.logger.Logger import log
from core.variables import Variables

browser_lib = Selenium()
variables = Variables()


class Bot:
    def open_the_site_by_link(self):
        browser_lib.open_chrome_browser('https://www.nytimes.com')

    def enter_search_phrase(self):
        search_button_locator_small_screen = '//button[@aria-label="Sections Navigation & Search"]'
        search_button_locator_large_screen = '//button[@data-test-id="search-button"]'
        if browser_lib.is_element_visible(search_button_locator_small_screen):
            search_button = browser_lib.find_element(search_button_locator_small_screen)
        else:
            search_button = browser_lib.find_element(search_button_locator_large_screen)
        search_button.click()
        input_field = '//input[@placeholder="SEARCH"]'
        browser_lib.wait_until_page_contains_element(input_field)
        browser_lib.input_text(input_field, variables.search_phrase)
        browser_lib.press_keys(input_field, "ENTER")
        log.info(f"Search phrase {variables.search_phrase} has been entered")

    def select_a_news_category(self):
        pass

    def choose_the_latest_news(self):
        pass

    def get_values(self):
        pass

    def store_in_excel_file(self):
        pass

    def download_news_picture(self):
        pass

    def execute(self):
        self.open_the_site_by_link()
        self.enter_search_phrase()
        self.select_a_news_category()
        self.choose_the_latest_news()

