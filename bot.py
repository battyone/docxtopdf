#!/usr/bin/env python3
import telebot 
from telebot.types import Message
import pypandoc
import pdfkit
import requests
import urllib
from urllib import request
import convertapi
import PyPDF2
import os

#Bot's Token and Bot object
MyToken = "803015368:AAGWYDoyWqs0bxFlvjtQYt3ybflAKdjFwYI"
convertapi.api_secret = '9bgjl6kGBTSNh8Hk'
bot = telebot.TeleBot(MyToken)


@bot.message_handler(content_types=["document"])
def convertDocToPDF(message: Message):
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    fileID = message.document.file_id
    fileInfo = bot.get_file(fileID)
    fileURL = bot.get_file_url(fileID)
    urllib.request.urlretrieve(fileURL, "newFile.docx")
    convertapi.convert('pdf', {'File': '/Users/dankotov/Documents/Projects/TelegramConverterBot/newFile.docx'}, from_format = 'docx').save_files('/Users/dankotov/Documents/Projects/TelegramConverterBot/convertedFile.pdf')
    fileToSend = open("convertedFile.pdf", "rb")
    bot.send_document(message.chat.id, fileToSend)
    os.remove("/Users/dankotov/Documents/Projects/TelegramConverterBot/newFile.docx")
    os.remove("/Users/dankotov/Documents/Projects/TelegramConverterBot/convertedFile.pdf")
    

    



bot.polling()

