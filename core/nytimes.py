import datetime
import re

from RPA.Browser.Selenium import Selenium
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from core.articles import Article
from core.logger.Logger import log
from core.variables import Variables


class Nytimes:
    def __init__(self):
        self.count_of_articles: int = 0
        self.browser_lib = Selenium()
        self.variables = Variables()

    def open_the_site_by_link(self):
        # self.browser_lib.open_chrome_browser('https://www.nytimes.com/search?dropmab=false&query=Ukraine&sort=best')
        self.browser_lib.open_chrome_browser('https://www.nytimes.com')

    def enter_search_phrase(self):
        # Site has adaptive layout. Search button has different position on small and large resolution
        search_button_locator_small_screen = '//button[@aria-label="Sections Navigation & Search"]'
        search_button_locator_large_screen = '//button[@data-test-id="search-button"]'

        if self.browser_lib.is_element_visible(search_button_locator_small_screen):
            self.browser_lib.click_element(search_button_locator_small_screen)
        else:
            self.browser_lib.click_element(search_button_locator_large_screen)

        input_field_locator = '//input[@placeholder="SEARCH"]'
        self.browser_lib.input_text_when_element_is_visible(input_field_locator, self.variables.search_phrase)
        self.browser_lib.press_keys(input_field_locator, "ENTER")

        log.info(f"Search phrase {self.variables.search_phrase} has been entered")

    def select_section(self):
        section_button_locator = '//div[@data-testid="section"]'
        self.browser_lib.wait_until_page_contains_element(section_button_locator)
        self.browser_lib.click_element(section_button_locator)

        sections_locator = '//label[@data-testid="DropdownLabel"]/span'
        sections = self.browser_lib.find_elements(sections_locator)
        for input_section in self.variables.sections:
            for section in sections:
                section_name: str = section.text

                if section_name.lower().strip().startswith(input_section):
                    section.click()
                    log.info(f"Section {section_name} has been selected")
                    break
            else:
                raise ValueError(f"Section '{input_section}' not found")

    def _get_section_name(self, section) -> str:
        numbers = section.find_element(By.XPATH, 'span')
        return section.text.replace(numbers.text, '')

    def choose_the_latest_news(self):
        self.browser_lib.select_from_list_by_value("//select[@data-testid='SearchForm-sortBy']", 'newest')
        log.info("Latest news has been chosen")

    def set_date_range(self):
        date_range_locator = "//button[@data-testid='search-date-dropdown-a']"
        self.browser_lib.click_element(date_range_locator)
        specific_date_locator = "//button[@aria-label='Specific Dates']"
        self.browser_lib.click_element(specific_date_locator)
        end_date_field_locator = "//input[@id='endDate']"
        start_date_field_locator = "//input[@id='startDate']"
        start_date: str = self._get_start_date()
        end_date: str = datetime.date.today().strftime("%m/%d/%Y")
        self.browser_lib.input_text(start_date_field_locator, start_date)
        self.browser_lib.input_text(end_date_field_locator, end_date)
        self.browser_lib.press_keys(end_date_field_locator, "ENTER")
        self._wait_while_page_loading()
        log.info(f"Date range from {start_date} to {end_date} has been set")

    def _get_start_date(self):
        start_date = datetime.date.today() - relativedelta(months=self.variables.number_of_month)
        return start_date.strftime("%m/%d/%Y")

    def _wait_while_page_loading(self):
        status_string_locator = "//p[@data-testid='SearchForm-status']"
        status_text: str = self.browser_lib.get_text(status_string_locator)
        if status_text.startswith('Loading'):
            self.browser_lib.wait_until_element_does_not_contain(status_string_locator, status_text)

    def show_all_articles(self):
        show_more_button_locator = "//button[@data-testid='search-show-more-button']"
        article_element_locator = '//li[@data-testid="search-bodega-result"]'
        self._get_count_of_articles()
        while True:
            current_element_count = self.browser_lib.get_element_count(article_element_locator)
            if self.count_of_articles > current_element_count:
                self.browser_lib.click_element(show_more_button_locator)
                WebDriverWait(self.browser_lib, 5).until_not(
                    lambda _: self.browser_lib.get_element_count(article_element_locator) == current_element_count)
            else:
                break

        log.info(f"Found {self.count_of_articles} articles")

    def _get_count_of_articles(self):
        status_string_locator = "//p[@data-testid='SearchForm-status']"
        status_test: str = self.browser_lib.get_text(status_string_locator)
        count_of_articles = re.findall('[0-9,]+', status_test)
        self.count_of_articles = int(count_of_articles[0])

    def get_articles(self):
        article_element_locator = '//li[@data-testid="search-bodega-result"]/div'
        articles = self.browser_lib.find_elements(article_element_locator)
        for article in articles:
            Article(article).save_data_to_exel()

    def get_values(self):
        pass

    def store_in_excel_file(self):
        pass

    def download_news_picture(self):
        pass

    def store_screenshot(self):
        self.browser_lib.screenshot(filename='output/screenshot.png')

    def execute(self):
        try:
            self.open_the_site_by_link()
            self.enter_search_phrase()
            self.select_section()
            self.choose_the_latest_news()
            self.set_date_range()
            self.show_all_articles()
            self.get_articles()
            self.store_screenshot()
        finally:
            self.browser_lib.close_all_browsers()
