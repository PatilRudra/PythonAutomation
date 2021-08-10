import logging
import inspect
#import time

def log():
    fileName = "logs.log"
    logg = logging.getLogger(inspect.stack()[1][3])
    logg.setLevel(logging.DEBUG)
    std_format = "%(asctime)s %(levelname)s %(name)s %(message)s"
    dateFormat = "%d/%m/%y %I:%M:%S %p"
    filhandler = logging.FileHandler(fileName,mode='a')
    filhandler.setLevel(logging.DEBUG)
    formattr = logging.Formatter(std_format,datefmt=dateFormat)
    filhandler.setFormatter(formattr)
    logg.addHandler(filhandler)
    return logg
