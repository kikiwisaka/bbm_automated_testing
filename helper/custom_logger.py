import os
import logzero
import datetime
import logging
from pythonjsonlogger import jsonlogger


class LoggerHelper():
    def __init__(self):
        pass

    @staticmethod
    def json_logger():
        json_format = LoggerHelper.json_formatter()
        logger1 = logzero.setup_logger(name="test_log", logfile="test_log.log", formatter=LoggerHelper.json_formatter())
        return logger1

    @staticmethod
    def json_formatter():
        jsonFormat = CustomJsonFormatter('(level) (message) (timestamp)')
        return jsonFormat

    @staticmethod
    def simple_formatter():
        simpleFormat = SimpleFormatter.formatter()
        return simpleFormat


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


class SimpleFormatter:
    @staticmethod
    def formatter():
        formatter = '%(color)s[%(levelname)1.1s]%(end_color)s ' \
                    '%(color)s[%(message)s]%(end_color)s ' \
                    '%(color)s[%(asctime)s]%(end_color)s'
        log_zero_formatter = logzero.LogFormatter(fmt=formatter)
        return log_zero_formatter
