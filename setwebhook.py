from telegram import Bot
import config

Token = config.get_token()
url = config.get_url()

bot = Bot(token=Token)

bot.set_webhook(url)

# bot.delete_webhook()

print(bot.get_webhook_info())
