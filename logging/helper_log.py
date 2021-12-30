
#by default only warning error and upper are printed

import logging

#Pyton documentation, we can change some values of our config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


logging.debug("this is a debug message")#classification of errors at levels
logging.info("this is a info message")
logging.warning("this is a warning message")
logging.error("this is a error message")
logging.critical("this is a critical message")
