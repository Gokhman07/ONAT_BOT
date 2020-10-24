import requests
from bs4 import BeautifulSoup
from utility import get_keyboard
from  telegram import  KeyboardButton, ReplyKeyboardMarkup, ParseMode, Location, Venue, InlineKeyboardMarkup
from  telegram.ext import ConversationHandler
from glob import glob

from  random import  choice
from emoji import  emojize
#from sqlitedb import  search_place
#build_keyboard

from utility import get_url

import sqlite3


def sms(bot, update):
 
    bot.message.reply_text((f'Привет дорогой студент ОНАС {bot.message.chat.first_name} 👨‍💻 🏫!!!!\n Я твой помощник по расписанию 🎓! \n '
    ),reply_markup=get_keyboard())

def get_teach(bot, update):
     data=get_url(bot.message.text)
     for d in data :
         bot.message.reply_text(d)
     
'''
def main_keyboard(bot, update):
    
  
    bot.message.reply_text("Главное меню", reply_markup=get_keyboard())

# функция печатает и отвечает на полученные геоданные
def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('{}, мы получили ваше местоположение!'.format(bot.message.chat.first_name))

def make_keyboard(bot,update):
   result=[]
   result= build_keyboard(bot.message.text)

    
   reply_keyboard = []
   reply_keyboard.append("🔙")
   for el in result:
       reply_keyboard.append(el)
    
   
   

   # создаем клавиатуру
   bot.message.reply_text(
        f"{bot.message.text}",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard , resize_keyboard=True))

def sendPlace(bot, update):
   
    place = search_place( bot.message.text)
    print(place)
     
   
    bot.message.reply_text(place[8])
    if(place[7]):
       bot.message.reply_text(f"Сайт: {place[7]}")
    update.bot.send_venue(chat_id=bot.message.chat.id,latitude=place[3], longitude=place[4], title=place[1],address=place[2])

 
   
  
  

def parrot(bot, update):
    bot.message.reply_text(bot.message.text)



'''










