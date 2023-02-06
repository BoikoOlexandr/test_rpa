from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import datetime

from core.logger.Logger import log


class Article:
    def __init__(self, article: WebElement):
        self.title_element: WebElement = article.find_element(By.TAG_NAME, 'h4')
        self.date_element: WebElement = article.find_element(By.TAG_NAME, "span")
        self.description_element: WebElement = article.find_element(By.XPATH, '//a/p[1]')
        self.count_of_search_phrase: int = 0
        self.has_title_or_description_any_amount_of_money: int = 0

    def save_data_to_exel(self):
        title = self.title_element.text
        date = self._get_date()
        log.info(date)
        description = self.description_element.text

    def _get_date(self):
        return datetime.datetime.strptime(self.date_element.get_attribute('aria-label'), '%m-%d-%Y')