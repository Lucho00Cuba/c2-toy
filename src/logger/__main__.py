import logging

class Logger():

    def __init__(self, log_level="INFO", name="default"):

        # Logging
        self.name = name
        self.log_level = log_level

        # check handler logger
        if logging.getLogger(f"{self.name}").hasHandlers() == False:
            self.build_logger()
            #print(f"BUILD LOGGER {name.upper()}")
            self.__log__()
        else:
            self.logger = logging.getLogger(f"{self.name}")
            self.log_level = logging.getLevelName(self.logger.level)
            #print(f"GET LOGGER {name.upper()}")

    def show_loggers(self):
        loggers = [('root', logging.getLogger())]
        for name in sorted(logging.Logger.manager.loggerDict.keys()):
            logger = logging.getLogger(name)
            loggers.append( (name, logger) )
        for name, logger in loggers:
            indent = ""
            if name != 'root':
                indent = "   "*(name.count('.')+1)
            if logger.propagate:
                prop = "+ "
            else:
                prop = "  "
            handlers = ""
            if len(logger.handlers) > 0:
                handlers = ": " + str(logger.handlers)
            level = logging.getLevelName(logger.level)
            eff_level = logging.getLevelName(logger.getEffectiveLevel())
            if level == eff_level:
                level_str = ' [%s]' % level
            else:
                level_str = ' [%s -> %s]' % (level, eff_level)
            print(indent + prop + name + level_str + handlers)

    def build_logger(self):

        self.logger = logging.getLogger(f"{self.name}")

        if self.log_level.upper() == "INFO":
            self.logger.setLevel(logging.INFO)
        elif self.log_level.upper() == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug(f"LOG_LEVEL {self.log_level} not found")

        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', "%Y-%m-%d %H:%M:%S")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def setLevel(self, level):
        self.log_level = level
        if self.log_level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif self.log_level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        self.printable("__logging__",f"Switched to Mode {self.log_level}")


    def __log__(self, function="__logging__", debug=False):
        if debug:
            self.printable(function, message="Load Class Logging", debug=True)
            self.printable(function, message=f"Log Level {self.log_level}", debug=True)
        else:
            self.printable(function, message="Load Class Logging")
            self.printable(function, message=f"Log Level {self.log_level}")

    def debug(self, function, message):
        self.logger.debug(f"[{function}] - {message}")

    def info(self, message):
        self.logger.info(message)

    def warning(self, function, message):
        self.logger.warning(f"[{function}] - {message}")

    def error(self, function, message):
        self.logger.error(f"[{function}] - {message}")

    def printable(self, function=None, message=None, debug=False):
        if debug == True or self.log_level == "DEBUG":
            self.debug(function ,message)
        else:
            self.info(message)