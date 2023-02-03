from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.logger.Logger import log
from core.variables import Variables

browser_lib = Selenium()
variables = Variables()


class Bot:
    def open_the_site_by_link(self):
        browser_lib.open_chrome_browser('https://www.nytimes.com/search?dropmab=false&query=Ukraine&sort=best')

    def enter_search_phrase(self):
        # Site has adaptive layout. Search button has different position on small and large resolution
        search_button_locator_small_screen = '//button[@aria-label="Sections Navigation & Search"]'
        search_button_locator_large_screen = '//button[@data-test-id="search-button"]'
        if browser_lib.is_element_visible(search_button_locator_small_screen):
            search_button = browser_lib.find_element(search_button_locator_small_screen)
        else:
            search_button = browser_lib.find_element(search_button_locator_large_screen)
        search_button.click()

        input_field_locator = '//input[@placeholder="SEARCH"]'
        browser_lib.wait_until_page_contains_element(input_field_locator)
        browser_lib.input_text(input_field_locator, variables.search_phrase)
        browser_lib.press_keys(input_field_locator, "ENTER")

        log.info(f"Search phrase {variables.search_phrase} has been entered")

    def select_section(self):
        section_button_locator = '//div[@data-testid="section"]'
        browser_lib.wait_until_page_contains_element(section_button_locator)
        browser_lib.click_element(section_button_locator)

        sections_locator = '//label[@data-testid="DropdownLabel"]/span'
        sections = browser_lib.find_elements(sections_locator)
        for section in sections:
            section_name = self._get_section_name(section)
            if section_name.lower().strip() in variables.sections:
                section.click()

    def _get_section_name(self, section) -> str:
        numbers = section.find_element(By.XPATH, 'span')
        return section.text.replace(numbers.text, '')

    def choose_the_latest_news(self):
        pass

    def get_values(self):
        pass

    def store_in_excel_file(self):
        pass

    def download_news_picture(self):
        pass

    def store_screenshot(self):
        browser_lib.screenshot(filename='output/screenshot.png')

    def execute(self):
        try:
            self.open_the_site_by_link()
            # self.enter_search_phrase()
            self.select_section()
            self.choose_the_latest_news()
            self.store_screenshot()
        finally:
            browser_lib.close_all_browsers()
