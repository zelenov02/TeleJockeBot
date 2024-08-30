import telebot
from telebot import types
import random
from jokes import bad_jokes, history_jokes, best_jokes


bot = telebot.TeleBot("5408840216:AAHuYV1E-caqkQlpZGWbZWmIFmRhz95RAmE")

amoral_mem = list(range(1, 21))
game_mem = list(range(21, 41))
legend_mem = list(range(41, 61))
english_memes = list(range(61, 81))
memes = amoral_mem + game_mem + legend_mem + english_memes
video_memes = list(range(1, 51))
jokes = bad_jokes + best_jokes + history_jokes


@bot.message_handler(commands=['start'])
def send_welcome(message):
	mess = f"Привет бедолага, <b>{message.from_user.first_name}</b>\nЯ заставлю тебя смеяться до смерти\n<b>У меня есть отборные анекдоты и мемы</b>"
	bot.send_message(message.chat.id, mess, parse_mode='html')
	photo = open('memes/start.jpg', 'rb')
	bot.send_photo(message.chat.id, photo)
	get_help(message)


@bot.message_handler(commands=['help'])
def get_help(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	jokes_button = types.KeyboardButton('Анекдот')
	memes_button = types.KeyboardButton('Мем')
	video_memes_button = types.KeyboardButton('Видео мем')
	random_jokes_button = types.KeyboardButton('Рандомный анекдот')
	random_memes_button = types.KeyboardButton('Рандомный мем')
	mem_day_button = types.KeyboardButton('Мем дня')
	jokes_day_button = types.KeyboardButton('Анекдот дня')
	markup.add(jokes_button, memes_button, random_memes_button, random_jokes_button, mem_day_button, jokes_day_button, video_memes_button)
	mess = f'Нажми <b>анекдот</b>, если хочешь увидеть отборные анекдоты по категориям\nНажми <b>мем</b>, если тебе нужны мемы по категориям\nНажми <b>Видео мем</b> если хочешь орных видосиков\nНажми <b>рандомный анекдот</b> или <b>рандомный мем</b> если тебе хочется посмеяться\nТак же можешь нажать <b>мем дня</b> или <b>анекдот дня</b>'
	bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['anekdot'])
def get_class_anekdot(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	bad_jokes_button = types.KeyboardButton('Чёрный юмор')
	history_jokes_button = types.KeyboardButton('Анекдоты 2007')
	best_jokes_button = types.KeyboardButton('Лучшая подбокра')
	back_button = types.KeyboardButton('Назад')
	markup.add(bad_jokes_button, history_jokes_button, best_jokes_button, back_button)
	bot.send_message(message.chat.id, f'У меня есть три темы анекдотов:\n<b>1. Чёрный юмор\n2. Анекдоты 2007\n3. Лучшая подбокра</b>\nВыбери тему', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['mem'])
def get_class_mem(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	amoral_mem_button = types.KeyboardButton('Аморальные мемы')
	game_mem_button = types.KeyboardButton('Игровые мемы')
	legend_mem_button = types.KeyboardButton('Легендарные мемы')
	english_memes_button = types.KeyboardButton('English memes')
	back_button = types.KeyboardButton('Назад')
	markup.add(amoral_mem_button, game_mem_button, legend_mem_button, english_memes_button, back_button)
	mess = f'Для тебя у меня есть три категории мемчиков:\n<b>1. Аморальные мемчки\n2. Игровые мемасы\n3. Легендарные мемосы\n4. English memes</b>\nВыбери категорию'
	bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['random_mem'])
def send_random_mem(message):
	mess = random.choice(memes)
	photo = open('memes/' + str(mess) + '.jpg', 'rb')
	bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['random_anekdot'])
def send_random_anekdot(message):
	mess = random.choice(jokes)
	bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['mem_day'])
def send_mem_day(message):
	photo = open('memes/mem_day.jpg', 'rb')
	bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['anekdot_day'])
def send_anekdot_day(message):
	mess = 'Почему доктор не стал лечить больного раком?\n<b>Неудобно</b>'
	bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['videomem'])
def send_videomem(message):
	mess = random.choice(video_memes)
	video = open('videomemes/' + str(mess) + '.mp4', 'rb')
	bot.send_video(message.chat.id, video)


@bot.message_handler(content_types=['text'])
def get_text_or_button_info(message):
	if message.text.lower() == 'анекдот':
		get_class_anekdot(message)
	elif message.text.lower() == 'черный юмор' or message.text.lower() == 'чёрный юмор':
		mess = random.choice(bad_jokes)
		bot.send_message(message.chat.id, mess, parse_mode='html')
	elif message.text.lower() == 'анекдоты 2007':
		mess = random.choice(history_jokes)
		bot.send_message(message.chat.id, mess, parse_mode='html')
	elif message.text.lower() == 'лучшая подбокра':
		mess = random.choice(best_jokes)
		bot.send_message(message.chat.id, mess, parse_mode='html')
	elif message.text.lower() == 'мем':
		get_class_mem(message)
	elif message.text.lower() == 'аморальные мемы':
		mess = random.choice(amoral_mem)
		photo = open('memes/' + str(mess) + '.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif message.text.lower() == 'игровые мемы':
		mess = random.choice(game_mem)
		photo = open('memes/' + str(mess) + '.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif message.text.lower() == 'легендарные мемы':
		mess = random.choice(legend_mem)
		photo = open('memes/' + str(mess) + '.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif message.text.lower() == 'english memes':
		mess = random.choice(english_memes)
		photo = open('memes/' + str(mess) + '.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif message.text.lower() == 'Рандомный анекдот'.lower():
		send_random_anekdot(message)
	elif message.text.lower() == 'Рандомный мем'.lower():
		send_random_mem(message)
	elif message.text.lower() == 'анекдот дня':
		send_anekdot_day(message)
	elif message.text.lower() == 'мем дня':
		send_mem_day(message)
	elif message.text.lower() == 'видео мем':
		send_videomem(message)
	elif message.text.lower() == 'назад':
		get_help(message)
	else:
		bot.send_message(message.chat.id, 'Я тебя не понимаю :(')
		get_help(message)


# Расставить переносы строк, добавить мемов и видео, деплоить


bot.polling(none_stop=True)