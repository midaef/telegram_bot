
import telebot #импорт библиотеки telebot
import random #импорт библиотеки random

token = '#your token'
stdian = 410850479
bot = telebot.TeleBot(token)
#bot.config['api_key'] = token
bot.send_message(stdian, "bot started")

print(bot.get_me())


def log(message, answer):
    print("\n--------------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))

    print("Answer: " + answer)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Привет, ЭТО НАВАЛЬНЫЙ!Что я умею?Сейчас расскажу!')
    bot.send_message(message.chat.id, '1) /contacts\n2) /vk\n3) /instagram\n4) /telegram\n 5) /donate')

@bot.message_handler(content_types=['text'])
def skill(message):
	answer = "Unknown command"
	if message.text == '/contacts':
		answer = 'Сайты:\n[navalny.com](https://navalny.com)'
		answer2 = '[navalny.live](https://navalny.live)'
		bot.send_message(message.chat.id, parse_mode="Markdown", text = answer + '\n' + answer2)
		log(message, answer + '\n' + answer2)
	if message.text == '/vk':
		answer = '[Ссылки ВК:\nvk.com/navalny](https://vk.com/navalny)'
		answer2 = '[vk.com/teamnavalny](https://vk.com/teamnavalny)'
		bot.send_message(message.chat.id, parse_mode="Markdown", text = answer + '\n' + answer2)
		log(message, answer + '\n' + answer2)
	if message.text == '/instagram':
		answer = '[Instagram:\ninstagram.com/teamnavalny](https://instagram.com/teamnavalny)'
		bot.send_message(message.chat.id, parse_mode="Markdown", text = answer + '\n')
		log(message, answer + '\n')
	if message.text == '/telegram':
		answer = '[Telegram:\n@navalny](https://t.me/navalny)'
		bot.send_message(message.chat.id, parse_mode="Markdown", text = answer + '\n')
		log(message, answer + '\n')
	if message.text == '/donate':
		answer = '[vk.com/teamnavalny](https://2018.navalny.com/#donate)'
		bot.send_message(message.chat.id, parse_mode="Markdown", text = answer + '\n')
		log(message, answer + '\n')
bot.polling(none_stop=True, interval=0)