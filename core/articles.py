import datetime
import os
import re
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.excel import Excel
from core.variables import Variables


class Article:
    title: str
    description: str
    picture_path: str = ''
    count_of_search_phrase: int = 0
    has_any_amount_of_money: int = 0

    def __init__(self, article: WebElement, variables: Variables, excel: Excel):
        self.title_element: WebElement = article.find_element(By.TAG_NAME, 'h4')
        self.date_element: WebElement = article.find_element(By.TAG_NAME, "span")
        self.description_element: WebElement = article.find_element(By.CLASS_NAME, 'css-16nhkrn')
        self.picture_element = article.find_element(By.TAG_NAME, "img")
        self.excel = excel
        self.date: datetime = datetime.date.today()
        self.variables = variables

    def get_values(self):
        self.title = self.title_element.text
        self.description = self.description_element.text
        self.convert_date_to_datetime()
        self.calculate_count_of_search_phrase()
        self.find_mentioning_money()

    def convert_date_to_datetime(self):
        text_date = self.date_element.get_attribute('aria-label')
        today_date_re = '[0-9]{1,2} (minutes|hours) ago'
        this_year_date_re = '[A-Za-z]+ [0-9]{1,2}$'
        other_date_re = '^[A-Za-z]+ [0-9]{1,2}, [0-9]{4}$'
        if re.findall(today_date_re, text_date):
            self.date = datetime.datetime.today()
        elif re.findall(this_year_date_re, text_date):
            text_date = f'{text_date}, {datetime.date.today().year}'
            self.date = datetime.datetime.strptime(text_date, '%B %d, %Y')
        elif re.findall(other_date_re, text_date):
            self.date = datetime.datetime.strptime(text_date, '%B %d, %Y')

    def calculate_count_of_search_phrase(self):
        self.count_of_search_phrase += re.findall(self.variables.search_phrase.lower(), self.title.lower()).__len__()
        self.count_of_search_phrase += re.findall(self.variables.search_phrase.lower(),
                                                  self.description.lower()).__len__()

    def find_mentioning_money(self):
        money_re = '(\$([0-9]+[,])*[0-9]+[.][0-9]+)|([0-9]+ (dollar[s]?|USD))'
        if re.findall(money_re, self.title):
            self.has_any_amount_of_money = True
        elif re.findall(money_re, self.description):
            self.has_any_amount_of_money = True
        else:
            self.has_any_amount_of_money = False

    def save_to_excel(self):
        self.excel.add_row(
            title=self.title,
            date=self.date,
            description=self.description,
            picture_filename=f'=HYPERLINK("{self.picture_path}", "Picture")',
            count_of_search_phrase=self.count_of_search_phrase,
            has_any_amount_of_money=self.has_any_amount_of_money
        )

    def download_news_picture(self):
        picture_filename = str(uuid.uuid4()) + '.png'
        self.picture_path = f"image/{picture_filename}"
        self.picture_element.screenshot(f'result/{self.picture_path}')
