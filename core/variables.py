from RPA.Robocorp.WorkItems import WorkItems

from core.logger.Logger import log


class Variables:

    def __init__(self):
        try:
            library = WorkItems()
            library.get_input_work_item()
            variables = library.get_work_item_variables()
            self.search_phrase: str = variables['search_phrase']
            self.sections: [str] = [section.strip().lower() for section in variables['search_phrase'].split(',')]
            self.number_of_month: int = self.validate_number_of_month(variables['number_of_month'])
            log.info("Variables has been set from work items")
        except (KeyError, TypeError, AttributeError):
            log.warn("Local run: default variables has been set")
            self.search_phrase = "Ukraine"
            self.sections = ["arts", "sports"]
            self.number_of_month = 1

    def validate_number_of_month(self, number_of_month):
        number_of_month = int(number_of_month)
        if number_of_month < 0:
            raise TypeError
        elif number_of_month == 0:
            number_of_month = 1
        return number_of_month
