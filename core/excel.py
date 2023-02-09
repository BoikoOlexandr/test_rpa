from datetime import datetime

from openpyxl import Workbook


class Excel:
    title: str = ''
    date: datetime
    description: str = ''
    picture_filename: str = ''
    count_of_search_phrase: int = 0
    has_any_amount_of_money: bool = False

    def __init__(self):
        self.book = Workbook()
        self.path = 'output/result/result.xlsx'
        self.sheet = self.book.active
        header = ('title',
                  'date',
                  'description',
                  'picture filename',
                  'count of search phrases in the title and description',
                  'True or False, depending on whether the title or description contains any amount of money')
        self.sheet.append(header)
        self.book.save(self.path)

    def add_row(self, date: datetime, title='', description='', picture_filename='', count_of_search_phrase=0,
                has_any_amount_of_money=False):
        self.sheet.append(
            (
                title,
                date.date(),
                description,
                picture_filename,
                count_of_search_phrase,
                has_any_amount_of_money
            )
        )
        self.book.save(self.path)
