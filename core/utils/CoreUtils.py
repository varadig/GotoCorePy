import time

import datetime

from core.base.CoreBaseClass import CoreBaseClass


class CoreUtils(CoreBaseClass):
    @staticmethod
    def timeStamp():
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

