from RPA.Browser.Selenium import Selenium

from core.variables import Variables

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)



def search_for(term):
    search_button = '/html/body/div[1]/div[2]/div[2]/header/section[1]/div[1]/div[2]/button/svg/path'
    browser_lib.click_element(search_button)
    input_field = '/html/body/div[1]/div[2]/div[2]/header/section[1]/div[1]/div[2]/div/form/div/input'
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        values = Variables().Execute()
        open_the_website("https://www.nytimes.com/")
        search_for(values)
        store_screenshot("output/screenshot.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()