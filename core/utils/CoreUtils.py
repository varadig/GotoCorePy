import datetime

from core.base.CoreBaseClass import CoreBaseClass


class CoreUtils(CoreBaseClass):
    @staticmethod
    def get_timeStamp():
        timestamp = ""
        timestamp += datetime.date.year + "-";
        timestamp += datetime.date.month + "-";
        timestamp += datetime.date.day + " ";
        timestamp += datetime.time.hour + "_";
        timestamp += datetime.time.minute + "_";
        timestamp += datetime.time.second + "_";
        timestamp += datetime.time.microsecond;
        return timestamp;
