import logging
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG) #logging level; time, s=turn into string
#blank is logging.basicConfig(level=logging.DEBUG)
#more advanced example from stackoverflow
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',level=logging.DEBUG) #logging level; time, s=turn into string
#-8s - indentantion for log level so that info____ and warning_
#logger = logging.getLogger(__name__) #so that each module has its own logger
logger = logging.getLogger('books') #naming logger based on functionality

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


#LOGGING to a file
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
                    ,level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H-%N-%S', #we can define daterormat in logs
                    filename='logs.txt') #that's how file is used

logger = logging.getLogger('books.database') #naming logger based on functionality
#^ this one is a child logger, inheriting from books logger