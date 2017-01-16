from core.base.CoreBaseParameterHolder import CoreBaseParameterHolder


class CoreBaseSender(CoreBaseParameterHolder):
    def __init__(self):
        super(CoreBaseSender, self).__init__()
        self.name = None
        self.collection = []
