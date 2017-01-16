from core.base.CoreBaseClass import CoreBaseClass
from core.logger.CoreLogger import CoreLogger
from core.logger.CoreLoggerDebug import CoreLoggerDebug
from core.notification.CoreListener import CoreListener
from core.notification.CoreNotification import CoreNotification
from core.notification.CoreNotificationContainer import CoreNotificationContainer


class Main(CoreBaseClass):
    def __init__(self):
        super(Main, self).__init__()
        CoreLogger.getInstance(CoreLoggerDebug())
        CoreNotificationContainer.getInstance()
        CoreListener.register("koko",self.koko)

        self.sc.registerService("asd",self.asd)
        self.sc.getService("asd").addParam("kaki",10).execute()
        CoreNotification.createNotification("koko").send()

    def asd(self,params):
        # print params['kaki']
        pass

    def koko(self,params):
        print "koko"



main = Main()
