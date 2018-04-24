#-*- coding:utf-8 -*-
import logging

LOGGING_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"

class LYMLogging:
    def __init__(self,
                 level = logging.DEBUG,  # 日志级别
                 format = LOGGING_FORMAT, #日志格式
                 datefmt = "%a, %d %b %Y %H:%M:%S", # 日期格式
                 filename = "LYM.log",
                 filemode = "w"
                 ):
        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = filename
        self.filemode = filemode

        # 初始化日志同时输出到console和文件
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)

        # 定义StreamHandler，将INFO级别或更高级别的日志信息打印打印到标准错误
        # 并添加到当前日志的处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
        console.setFormatter(formatter)
        logging.getLogger('LYMLogger').addHandler(console)
        self.log = logging.getLogger("LYMLogger")

    # 日志输出
    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告
             self.log.warning(msg)
        elif level == logging.ERROR:
            self.log.error(msg)
        else:
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.set_level(level)

if __name__ == '__main__':
    print("python logging实例")
    log = LYMLogging()
    log.output("It's a debug mag", level=logging.DEBUG)
    log.output("It's a info mag", level=logging.INFO)
    log.output("It's a warning mag", level=logging.WARNING)
    log.output("It's a error mag", level=logging.ERROR)
    log.output("It's a unknown mag", level=logging.CRITICAL)