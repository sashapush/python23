import logging
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG) #logging level; time, s=turn into string
#blank is logging.basicConfig(level=logging.DEBUG)
#more advanced example from stackoverflow
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',level=logging.DEBUG) #logging level; time, s=turn into string
#-8s - indentantion for log level so that info____ and warning_
logger = logging.getLogger('test_logger')

logger.info("I'm info message")
logger.warning("Warning") #will be displayed by default, we overwrote it it in line 2
logger.debug("Debug message")
logger.critical("Critical error occured")
logger.error("Error appeared")


"""
DEBUG
INFO
WARNING (default level)
ERROR
CRITICAL
"""