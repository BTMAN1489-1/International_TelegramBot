def setup_loggers():

    import ujson
    import logging.config as config

    with open(r'utils/misc/bot_logging/config.json', 'rb') as conf:
        cn = ujson.load(conf)
    config.dictConfig(cn)
