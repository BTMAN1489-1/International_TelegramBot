class BotAppData:
    from environs import Env

    env = Env()
    env.read_env()

    API_TOKEN = env.str("API_TOKEN")
    ADMINS = env.list("ADMINS", [])


class I18NData:
    from pathlib import Path, PurePath
    BASE_DIR = Path(__file__).parents[1]
    LOCALES_DIR = BASE_DIR.joinpath(PurePath('locales'))
    if not LOCALES_DIR.exists():
        LOCALES_DIR.mkdir()
    I18N_DOMAIN = 'internatbot'
