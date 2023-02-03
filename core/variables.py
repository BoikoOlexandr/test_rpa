from RPA.Robocorp.WorkItems import WorkItems

from core.logger.Logger import log


class Variables:

    def __init__(self):
        try:
            library = WorkItems()
            library.get_input_work_item()
            variables = library.get_work_item_variables()
            self.search_phrase = variables['search_phrase']
            self.section = variables['section']
            self.number_of_month = variables['number_of_month']
            log.info("Variables has been set from work items")
        except KeyError:
            log.warn("Local run: default variables has been set")
            self.search_phrase = "Ukraine"
            self.section = "any"
            self.number_of_month = 2
