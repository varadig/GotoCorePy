import cocos
from core.base.corebaseclassfactory import CoreBaseClassFactory
from core.utils.log import Log


class CoreLayer(cocos.layer.Layer):
    is_event_handler = True
    _nameIndex = 0
    _namePrefix = "core.cocos.layer"

    PRESS = "layer.press"

    RELEASE = "layer.release"

    MOTION = "layer.motion"

    DATA = "layer.data"

    def __init__(self):
        super(CoreLayer, self).__init__()
        self.sc = None
        self.context = None
        self.callbacks = {}
        self.name = self.generateName()
        CoreBaseClassFactory.construct(self)

    def get_name(self):
        return self.name

    def serviceAddCallback(self, params):
        CoreBaseClassFactory.serviceAddCallback(self, params)

    def serviceAddCallbacks(self, params):
        CoreBaseClassFactory.serviceAddCallbacks(self, params)

    def serviceRemoveCallback(self, params):
        CoreBaseClassFactory.serviceRemoveCallback(self, params)

    def serviceRemoveCallbacks(self, params):
        CoreBaseClassFactory.serviceRemoveCallbacks(self, params)

    def createCallBack(self, group):
        return CoreBaseClassFactory.createCallBack(self, group)

    def log(self, message):
        Log.add(message)

    def generateName(self):
        CoreLayer._nameIndex += 1
        return CoreLayer._namePrefix + str(CoreLayer._nameIndex)

    def on_mouse_press(self, x , y, button, modifiers):
        self.createCallBack(CoreLayer.PRESS)\
            .addParam(CoreLayer.DATA, {"x": x, "y": y, "button": button, "modifiers": modifiers})\
            .send()

    def on_mouse_release(self, x, y, button, modifiers):
        self.createCallBack(CoreLayer.RELEASE)\
            .addParam(CoreLayer.DATA, {"x": x, "y": y, "button": button, "modifiers": modifiers})\
            .send()

    def on_mouse_motion(self, x, y, dx, dy):
        self.createCallBack(CoreLayer.MOTION).addParam(CoreLayer.DATA, {"x": x, "y": y, "dx": dx, "dy": dy}).send()
        pass
