from core.logger.Logger import log
from core.nytimes import Nytimes


def main():
    # try:
        bot = Nytimes()
        bot.execute()
    # except Exception as e:
    #     log.error(e.with_traceback())


if __name__ == "__main__":
    main()
