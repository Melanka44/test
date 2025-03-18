import telebot
import random
import time

bot = telebot.TeleBot('7575316457:AAE98zWhJtw0a_DsiopRMDA7SCDErtLjwrg')

libraries = ["tkinter", "math", "time", "calendar", "string"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привіт! Це бот кабанчика')

@bot.message_handler(commands=['library'])
def send_library(message):
    day = time.strftime("%A")
    lib = random.choice(libraries)
    bot.reply_to(message, f"Сьогодні {day}, вивчи бібліотеку: {lib} ")

@bot.message_handler(commands=['random'])
def send_random(message):
    number = random.randint(1, 100)
    bot.reply_to(message, f"Твоє рандомне число: {number} ")

@bot.message_handler(commands=['info'])
def send_help(message):
    bot.reply_to(message, "Команди:\n"
                          " /start - Почати роботу з ботом\n"
                          " /library - Дізнатись яку бібліотеку сьогодні вивчити сьогодні\n"
                          " /random - Отримати рандомне число\n"
                          " /help - Показати список команд")

bot.polling()
