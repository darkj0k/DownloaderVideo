import logging


class Base:
    logging.getLogger(__name__)
    logging.basicConfig(filename="Log.log", level=logging.DEBUG, filemode='a', encoding='utf-8',
                        format="%(asctime)s : %(name)s - %(module)s.%(funcName)s : %(levelname)s ---- %(message)s")

    def __init__(self):
        logging.basicConfig(filename="Log.log", level=logging.DEBUG, filemode='a', encoding='utf-8',
                            format="%(asctime)s : %(name)s - %(module)s.%(funcName)s : %(levelname)s ---- %(message)s")
