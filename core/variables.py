from RPA.Robocorp.WorkItems import WorkItems

from core.logger.Logger import Logger


class Variables:

    def __init__(self):
        self.search_phrase = "Ukraine"
        self.section = "any"
        self.number_of_month = 2
        self.logger = Logger().get_logger()

    def Execute(self):
        try:
            library = WorkItems()
            library.get_input_work_item()
            variables = library.get_work_item_variables()
            self.search_phrase = variables['search_phrase']
            self.section = variables['section']
            self.number_of_month = variables['number_of_month']
        except KeyError:
            self.logger.error("Key error: default values has been set")
        finally:
            return self
