from core.logger.base.corebaselogger import CoreBaseLogger


class CoreLoggerFile(CoreBaseLogger):

    def __init__(self,file):
        super(CoreLoggerFile, self).__init__()
        self.file = open(file, 'a')

    def addLogEntry(self, message):
        self.file.write(self.createEntryFrom(message))
