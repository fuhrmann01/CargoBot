from django.core.management.base import BaseCommand
from telegram import Bot, ReplyKeyboardMarkup
from telegram.utils.request import Request
from telegram.ext import Updater, CommandHandler
from django.conf import settings


def do_start(update, context):
    reply_keyboard = [["Узнать стоимость доставки"]]
    update.message.reply_text(
        text="Этот бот разошлет Ваш запрос транспортным компаниям-партнерам сервиса. Вы сможете выбрать наиболее подходящие "
             "Вам тарифы и связаться с компниями.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
class Command(BaseCommand):
    help = 'telegram bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
            con_pool_size=8,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )

        start_handler = CommandHandler("start", do_start)

        updater.start_polling()
        updater.idle()
