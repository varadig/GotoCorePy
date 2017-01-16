import os

from core.base.CoreBaseClass import CoreBaseClass
from core.filesystem.CoreFileSystem import CoreFileSystem
from core.logger.CoreLogger import CoreLogger
from core.logger.CoreLoggerDebug import CoreLoggerDebug
from core.logger.CoreLoggerFile import CoreLoggerFile
from core.notification.CoreListener import CoreListener
from core.notification.CoreNotification import CoreNotification
from core.notification.CoreNotificationContainer import CoreNotificationContainer


class Main(CoreBaseClass):
    def __init__(self):
        super(Main, self).__init__()
        self.initCoreModules()
        self.initModules()
        self.startApplication()

    def initCoreModules(self):
        CoreFileSystem.getInstance()
        CoreLogger.getInstance([CoreLoggerDebug(), CoreLoggerFile('gotocorepy.log')])
        CoreNotificationContainer.getInstance()

    def initModules(self):
        ControllerTest.getInstance()
        NotificationTest.getInstance()

    def startApplication(self):
        self.sc.getService(ControllerTest.SERVICE)\
            .addParam('foo', 'service.bar')\
            .execute()

        CoreNotification.createNotification(NotificationTest.NOTIFICATION)\
            .addParam('foo', 'notification.bar')\
            .send()


class ControllerTest(CoreBaseClass):

    SERVICE='controller.test.service'
    instance=None

    @staticmethod
    def getInstance():
        if ControllerTest.instance == None:
            ControllerTest.instance = ControllerTest()
        return ControllerTest.instance

    def __init__(self):
        super(ControllerTest, self).__init__()
        self.sc.registerService(ControllerTest.SERVICE,self.testService)

    def testService(self, params):
        self.log(params.get('foo'))


class NotificationTest(CoreBaseClass):

    NOTIFICATION = 'notification.test.noti'
    instance = None

    @staticmethod
    def getInstance():
        if NotificationTest.instance == None:
            NotificationTest.instance = NotificationTest()
        return NotificationTest.instance

    def __init__(self):
        super(NotificationTest, self).__init__()
        CoreListener.register(NotificationTest.NOTIFICATION, self.notificationHandler)

    def notificationHandler(self, params):
        self.log(params.get('foo'))

main = Main()
