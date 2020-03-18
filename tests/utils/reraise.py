import re
import sys


def reraise(exception: Exception, *append_message: [str]):
    """ 例外にメッセージを付与する """
    exc_type = type(exception)
    # 元メッセージ
    message = re.sub('^Message:\\s?', str(exception), '')
    # 追記
    exc_value = exc_type(message + '\n'.join(append_message))
    exc_traceback = sys.exc_info()[2]
    if exc_traceback is not None and \
            exc_value.__traceback__ is not exc_traceback:
        raise exc_value.with_traceback(exc_traceback)
    raise exc_value
