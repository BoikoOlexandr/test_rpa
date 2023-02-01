from RPA.Browser.Selenium import Selenium
from RPA.Robocorp.WorkItems import WorkItems
browser_lib = Selenium()


# def open_the_website(url):
#     browser_lib.open_available_browser(url)
#
#
# def search_for(term):
#     input_field = "css:input"
#     browser_lib.input_text(input_field, term)
#     browser_lib.press_keys(input_field, "ENTER")
#
#
# def store_screenshot(filename):
#     browser_lib.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        library = WorkItems()
        library.get_input_work_item()
        variables = library.get_work_item_variables()
        print(variables)
        # open_the_website("https://robocorp.com/docs/")
        # search_for("java")
        # store_screenshot("output/screenshot.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()