import os

from core.base.corebaseclass import CoreBaseClass
from core.base.corecallback import CoreCallback
from core.filesystem.corefilesystem import CoreFileSystem
from core.logger.corelogger import CoreLogger
from core.logger.coreloggerdebug import CoreLoggerDebug
from core.logger.coreloggerfile import CoreLoggerFile
from core.notification.corelistener import CoreListener
from core.notification.corenotification import CoreNotification
from core.notification.corenotificationcontainer import CoreNotificationContainer


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
        # self.sc.getService(ControllerTest.SERVICE)\
        #     .addParam('foo', 'service.bar')\
        #     .execute()
        CoreCallback.addCallback(self, "test.callback", self.sc.getService(ControllerTest.SERVICE))

        CoreNotification.createNotification(NotificationTest.NOTIFICATION)\
            .addParam('foo', 'notification.bar')\
            .send()

        self.createCallBack("test.callback").addParam("foo", "bar kaka").send()


class ControllerTest(CoreBaseClass):

    SERVICE = 'controller.test.service'
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
