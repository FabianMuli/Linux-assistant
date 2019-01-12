# -*- coding: utf-8 -*-
import telebot
import sys
import time
import aiml
import os

bot = telebot.TeleBot("638949450:AAEo_Xs4XYN46yvGKLFs_Sv8ziuV-qgGXsY")
kernel = aiml.Kernel()
if os.path.isfile("ai_brain.brn"):
    kernel.bootstrap(brainFile="ai_brain.brn")
else:
    kernel.bootstrap(learnFiles="std.xml", commands="load aiml b")
    kernel.saveBrain("ai_brain.brn")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def reply(message):

    text = message.text
    ai_speech = kernel.respond(text)

    print("Me: ", text)
    print("AI: " + ai_speech)
    bot.reply_to(message, ai_speech)


def main_loop():
    bot.polling()
    while True:
        time.sleep(1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print(sys.stderr, '\nExiting by user request')
        sys.exit(0)
