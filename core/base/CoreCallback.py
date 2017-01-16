from core.base.CoreBaseSender import CoreBaseSender
from core.service import CoreServiceContainer


class CoreCallback(CoreBaseSender):
    GROUP = 'group'
    CALLBACK = 'callback'
    CALLBACKS = 'callbacks'

    ADD_CALLBACK = ".add.callback"
    ADD_CALLBACKS = ".add.callbacks"

    REMOVE_CALLBACKS = ".remove.callbacks"
    REMOVE_CALLBACK = ".remove.callback"

    def __init__(self, name, collection):
        super(name, collection)

    def send(self):
        for service in self.collection:
            service.setParams(self.params).execute()

    @staticmethod
    def addCallback(self,target, group, callback):
        CoreServiceContainer.getInstance().getService(target.name + CoreCallback.ADD_CALLBACK).addParam(
            CoreCallback.GROUP, group).addParam(CoreCallback.CALLBACK, callback).execute()

    @staticmethod
    def addCallbacks(self,target, group, callbacks):
        CoreServiceContainer.getInstance().getService(target.name + CoreCallback.ADD_CALLBACKS).addParam(
            CoreCallback.GROUP, group).addParam(CoreCallback.CALLBACKS, callbacks).execute()

    @staticmethod
    def removeCallbacks(self,target, group, callbacks):
        CoreServiceContainer.getInstance().getService(target.name + CoreCallback.REMOVE_CALLBACKS).addParam(
            CoreCallback.GROUP, group).addParam(CoreCallback.CALLBACKS, callbacks).execute()
