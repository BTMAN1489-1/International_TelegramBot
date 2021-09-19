def setup_middleware(dispatcher):
    from data import I18NData
    from .i18n import InterNatMiddleware
    from .throttling import ThrottlingMiddleware
    from aiogram.contrib.middlewares.logging import LoggingMiddleware

    dispatcher.setup_middleware(LoggingMiddleware())
    dispatcher.setup_middleware(InterNatMiddleware(domain=I18NData.I18N_DOMAIN, path=I18NData.LOCALES_DIR))
    dispatcher.setup_middleware(middleware=ThrottlingMiddleware())


