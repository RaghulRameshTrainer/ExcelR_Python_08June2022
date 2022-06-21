import logging

''' LEVELS:
DEBUG   10
INFO    20
WARNING 30
ERROR   40
CRITICAL 50
'''
logging.basicConfig(filename='output.log',
                    level=logging.DEBUG,
                    format="%(levelname)s %(asctime)s - %(message)s")
logger=logging.getLogger()
logger.debug("Debug message")
logger.info("Info messages")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical Messages")