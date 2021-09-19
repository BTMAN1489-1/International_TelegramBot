import unittest
from data import BotAppData
from loader import get_dispatcher
import aiohttp


class ValidTest(unittest.TestCase):
    def test_valid_token(self):
        self.assertIsNotNone(BotAppData.API_TOKEN, "Token must not be None")

    @unittest.skipUnless(BotAppData.WEBHOOK_HOST != '', "Webhook is invalid")
    def test_valid_domain(self):
        self.assertRegex(text=BotAppData.WEBHOOK_HOST, expected_regex="https://.*")


class BotTest(unittest.IsolatedAsyncioTestCase):
    async def test_bot_auth(self):

        async with aiohttp.ClientSession() as BotAppData._session:
            self.bot_info = await get_dispatcher().bot.get_me()
        self.assertEqual(self.bot_info["username"], "my_first_developed_bot")


if __name__ == '__main__':
    unittest.main(verbosity=2, defaultTest=('BotTest', 'ValidTest'))

