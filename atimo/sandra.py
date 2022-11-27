import os
import logging
from abc import ABCMeta, abstractmethod


class FSHandler(metaclass=ABCMeta):

    # метод для отсутствия возможности создать экземпляр класса
    @abstractmethod
    def __never_born(selfself):
        pass

    @classmethod
    def log(cls, *args):
        #Логирование
        log_path = os.path.join(os.path.dirname(__file__), 'debug.log')
        formatt = '[%(levelname)s] %(asctime).19s [%(filename)s_Line:%(lineno)d] %(message)s'

        logging.basicConfig(
            level=logging.DEBUG,
            format=formatt,
            filename=log_path,
            filemode='w'
        )

        logger = logging.getLogger()

        logger.debug(args)

class DBWorker(metaclass=ABCMeta):

    @abstractmethod
    def __never_born(self):
        pass