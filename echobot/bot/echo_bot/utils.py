from viberbot.api.bot_configuration import BotConfiguration

from django.conf import settings

from viberbot import Api

bot_conf = BotConfiguration(
    name = 'Vasya',
    avatar = 'https://images.opencollective.com/nicolascarlo/f0fbfa7/avatar.png',
    auth_token = settings.VIBER_AUTH_TOKEN,
)

viber = Api(bot_conf)