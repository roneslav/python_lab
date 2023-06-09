"""
Module: decorators
Create a parametrized decorator
"""
import logging


class LoggedDecorator:  # pylint: disable=too-few-public-methods
    """
    Class: LoggedDecorator

    """
    def __init__(self, exception, mode):
        self.exception = exception
        self.mode = mode


def logged(exception, mode):
    """
    Method: logged
    :param exception: Class_Exception
    :param mode: file/console
    :return: text of an error
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            Wrapper
            :param args:
            :param kwargs:
            :return:
            """
            try:
                return func(*args, **kwargs)
            except exception as ex:
                if mode == 'console':
                    logging.error('Exception occurred: %s', ex)
                elif mode == 'file':
                    logging.basicConfig(filename='app.log', level=logging.ERROR)
                    logger = logging.getLogger(__name__)
                    logger.error('Exception occurred: %s', ex)
                else:
                    raise ValueError('Invalid mode specified.') from ex
        return wrapper
    return decorator
