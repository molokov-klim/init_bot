"""
hash_bot entrypoint
"""
import logging
import bot_base


def enable_debug():
    """
    Включение логгирования
    """
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


manager = bot_base.BotManager()
manager.start()
