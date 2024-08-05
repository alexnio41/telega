# API_URL = 'https://api.telegram.org/bot'
# BOT_TOKEN = '7330218093:AAF3A7CPSRhy2y0RqOi6Yj2DpXjYrXy8V5I'

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7330218093:AAF3A7CPSRhy2y0RqOi6Yj2DpXjYrXy8V5I'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )
# Этот хэндлер будет срабатывать на команду "/zadachi"
async def process_zadachi_command(message: Message):
    await message.answer('Тут будут задачи')

async  def process_sticker(message: Message):
    await message.answer('Спасибо за стикер!')

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.answer('Чудесная фотка')

@dp.message(F.voice)
async def process_sent_voice(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришло голосовое
    await message.answer(text='Вы прислали голосовое сообщение!')

# Навешиваем декоратор без фильтров, чтобы ловить большинство типов апдейтов
@dp.message()
async def process_any_update(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришел апдейт
    await message.answer(text='Вы что-то прислали')

dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_zadachi_command, Command(commands='zadachi'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(process_sticker, F.sticker)  # Пример использования фильтра для стикеров
# dp.message.register(send_echo)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )



if __name__ == '__main__':
    dp.run_polling(bot)