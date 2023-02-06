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
        text_date = self.date_element.get_attribute('aria-label')
        if text_date.split().__len__() == 2:
            text_date = f'{text_date}, {datetime.date.today().year}'
        return datetime.datetime.strptime(text_date, '%B %d, %Y')