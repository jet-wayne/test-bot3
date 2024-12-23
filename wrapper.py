import functools
from google.protobuf.json_format import MessageToDict
import coloredlogs
import logging
# A decorator function that takes in any number of argument

coloredlogs.install()
coloredlogs.set_level(logging.ERROR)
logger = logging.getLogger("TKsel Search Application")

logger.setLevel(logging.ERROR)

logger.info("Starting TKsel Search Application")


# def log_data(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             response = func(*args, **kwargs)
#             logger.info("Showing environment variables")
#             logger.info(response)
#             return response
#         except Exception as e:
#             logging.exception(e)
#             raise e
#     return wrapper


def proto_to_dict(func):
    @ functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        result = MessageToDict(response._pb)
        logger.info(result)
        return result
    return wrapper
