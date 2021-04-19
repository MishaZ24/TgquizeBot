import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help'])
def help_send_message(message):
	bot.reply_to(message, " Что я могу делать? \nПока что Ничего \nНо \n<b>Oбещаю, скоро научусь!</b>", parse_mode='html')

@bot.message_handler(commands=['start'])
def start_send_message(message):
    bot.send_message(message.chat.id," Привет! <b>{0.first_name}</b>, My name is <strong>{1.first_name}</strong>! \n Рад нашему знакомству!".format(message.from_user,bot.get_me()),
                     parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)
