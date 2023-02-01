from RPA.Browser.Selenium import Selenium

from core.logger.Logger import Logger
from core.variables import Variables

browser_lib = Selenium()
logger = Logger().get_logger()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def search_for(term):
    search_button = browser_lib.find_element('//header/section[1]/div[1]/div[1]/button')
    input_field = '//form/div/input'

    search_button.click()

    browser_lib.wait_until_page_contains_element(input_field)
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


def main():
    try:
        values = Variables().Execute()
        open_the_website("https://www.nytimes.com/")
        search_for(values.search_phrase)
        store_screenshot("output/screenshot.png")
    except Exception as e:
        logger.error(e)
    finally:
        browser_lib.close_all_browsers()


if __name__ == "__main__":
    main()
