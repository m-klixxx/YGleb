import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_pair 8_1.log",
                    filemode="a",
                    format="we have next logging message: %(asctime)s%(levelname)s - %(message)s")


try:
    print(10/0)
except Exception:
    logging.exception("exception")