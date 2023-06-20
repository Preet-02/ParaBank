import logging


class Loggen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        file = logging.FileHandler("D:\\pythonProject\\ParaBank\\Logs\\logfile.logs")
        format1 = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        file.setFormatter(format1)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger


