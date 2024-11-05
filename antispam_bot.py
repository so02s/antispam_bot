from codecs import utf_32_be_decode
# -*- coding: utf_32_be_decode -*-

import telebot

token = ''
bot = telebot.TeleBot(token)

#что считать за спам?
spamList = ['π', 'ᧉ', 'ꚍ', 't.me', '@']
admin = ''
whiteList = []

#удаление сообщения
def delThisShit(message, someting):
    for spam in spamList:
        if spam in someting:
            bot.delete_message(message.chat.id, message.id)
            print(message)
            break


@bot.message_handler(chat_types='private', commands=['help'])
def help_handler(message):
    if message.from_user.username == admin:
        bot.send_message(message.chat.id, 'Надо бы придумать что-то веселое')
    elif message.from_user.username in whiteList:
        bot.send_message(message.chat.id, 'Функций у бота кроме удаления спама пока нет')

@bot.message_handler(content_types=['caption', 'photo', 'text', 'html_text', 'html_caption'])
def deleteSpam(message):
    #если сообщение не от пользователя из белого списка / админа
    if message.from_user.username not in whiteList and not(message.sender_chat and message.sender_chat.username in whiteList):
        #тут проверка на спам
        if message.text != None:
            delThisShit(message, message.text)
        if message.caption != None:
            delThisShit(message, message.caption)
        if message.html_text != None:
            delThisShit(message, message.html_text)
        if message.html_caption != None:
            delThisShit(message, message.html_caption)

bot.infinity_polling()