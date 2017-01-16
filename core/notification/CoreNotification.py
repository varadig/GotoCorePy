﻿from core.base.CoreBaseSender import CoreBaseSender
from core.service.CoreServiceContainer import CoreServiceContainer


class CoreNotification(CoreBaseSender):
    CREATE_NOTIFICATION = "create.notification"
    NAME = "name"
    BASE_NAME = "base.name"

    def __init__(self, name, collection):
        super(CoreNotification, self).__init__()
        self.name = name
        self.collection = collection

    def send(self):
        for listener in self.collection:
            print listener
            listener.setParams(self.params).addParam(CoreNotification.BASE_NAME, self.name).notify()
        print "CoreNotification send"

    @staticmethod
    def createNotification(name):
        return CoreServiceContainer.getInstance().getService(CoreNotification.CREATE_NOTIFICATION).addParam(CoreNotification.NAME, name).execute()

    @staticmethod
    def createNotificationFromClass(c):
        return CoreServiceContainer.getInstance().getService(CoreNotification.CREATE_NOTIFICATION).addParam(CoreNotification.NAME, c.__name__).execute()
