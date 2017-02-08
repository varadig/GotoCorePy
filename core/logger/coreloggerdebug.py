from core.logger.base.CoreBaseLogger import CoreBaseLogger


class CoreLoggerDebug(CoreBaseLogger):
    def addLogEntry(self, message):
        print self.createEntryFrom(message)
