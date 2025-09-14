import logging, os
LOGFILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'minidyno.log')
logging.basicConfig(filename=LOGFILE, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
def info(msg): logging.info(msg)
def warning(msg): logging.warning(msg)
def error(msg): logging.error(msg)
