from core.base.CoreBaseClass import CoreBaseClass
from core.utils.CoreUtils import CoreUtils


class CoreBaseLogger(CoreBaseClass):
    def __init__(self):
        self.br = "\n"

    def addLog(self, *messages):
        for message in messages:
            self.addLogEntry(str(message));

        def addLogEntry(self, message):
            print (message)

    def createEntryFrom(self, message):
        return (CoreUtils.timeStamp() + " ----> " + message + self.br);
