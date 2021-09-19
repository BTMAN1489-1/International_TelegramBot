from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import User


class InterNatMiddleware(I18nMiddleware):
    def __init__(self, domain, path, default='en'):
        super().__init__(domain, path, default)
        self._install()

    def _install(self):
        import builtins
        builtins.__dict__['_'] = self.gettext

    async def get_user_locale(self, action: str, args: tuple):
        current_user = User.get_current()
        user_locale = current_user.language_code
        return user_locale
