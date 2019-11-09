#!/usr/bin/env python

import datetime
import gspread
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import telebot
import datetime
import conf
import requests
import os
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

sh = gspread.authorize(credentials)
wks = sh.open("denisov").sheet1

bot = telebot.TeleBot(conf.TOKEN)



keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
bt0 = telebot.types.KeyboardButton('SNPRO')
bt1 = telebot.types.KeyboardButton('Обучение')
bt2 = telebot.types.KeyboardButton('Магазин')
bt3 = telebot.types.KeyboardButton('Консультация',request_contact=True)
bt4 = telebot.types.KeyboardButton('Посетить семинар')
bt5 = telebot.types.KeyboardButton('Полезный материал')
keyboard1.add(bt0, bt1, bt2, bt3, bt4, bt5)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Любитель', 'Выступающий спортсмен', 'Тренер')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Назад', 'Подробнее', 'Вперед')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Полностью (любитель)', 'В рассрочку (любитель)', 'О курсе')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('Полностью (спортсмен)', 'В рассрочку (спортсмен)', 'О курсе')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('Полностью (тренер)', 'В рассрочку (тренер)', 'О курсе')
keyboardsnpro = telebot.types.ReplyKeyboardMarkup(True, row_width=1)
btcont = telebot.types.KeyboardButton('Оставить контакт', request_contact=True)
"""keyboard7 = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
bt_giri = telebot.types.KeyboardButton('Гири')
bt_aks = telebot.types.KeyboardButton('Аксессуары')
bt_diz = telebot.types.KeyboardButton('Дизайнерская одежда')
bt_inv = telebot.types.KeyboardButton('Инвентарь')
bt_so = telebot.types.KeyboardButton('Спортивная одежда')
bt_sp = telebot.types.KeyboardButton('Спортпит')
bt_bk = telebot.types.KeyboardButton('Назад')
keyboard7.add(bt_giri,bt_aks,bt_diz,bt_inv,bt_so,bt_sp, bt_bk)"""


@bot.message_handler(commands=['start'])
def start_message(message):
    nm = message.from_user.first_name
    ni = message.from_user.id

    bot.send_message(message.chat.id, 'Здравствуйте,' +str(nm)+ ' , вы попали в чат бот онлайн академии гиревого спорта Ивана Денисова. Выберите из меню интересующий Вас вопрос', reply_markup=keyboard1);

@bot.message_handler(content_types=['text'])
def send_text(message):
        # ОБУЧЕНИЕ
    if message.text.lower() == 'обучение':
        tm = message.message_id
        tu = message.chat
        print(tm)
        print(tu)
        bot.send_message(message.chat.id, 'Какой уровень Вас интересует?', reply_markup=keyboard2 )
    # SNPRO
    elif message.text.lower() == 'snpro':
        tu = message.from_user.first_name
        ti = message.from_user.id
        val = int();
        val = wks.cell(1, 1).value
        wks.update_cell(val, 2, tu)
        wks.update_cell(val, 3, ti)
        val1 = (int(val) + 1)
        wks.update_cell(1,1,val1)
        bot.send_message(message.chat.id, '<a href="https://vk.com/kettlebellschool?w=app5898182_-164184252">\n '+str(tu)+' ,рады видеть Вас на SNPRO, по ссылке Вас ждет бесплатный интенсив от Ивана Денисова!</a>', parse_mode="HTML", reply_markup=keyboard1)

        # любитель
    elif message.text.lower() == 'любитель':
        bot.send_message(message.chat.id, 'Вы хотите оплатить весь курс со скидкой 30% или оформить обучение в рассрочку?', reply_markup=keyboard4)
    elif message.text.lower() == 'полностью (любитель)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML");
    elif message.text.lower() == 'в рассрочку (любитель)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);
    elif message.text.lower() == 'о курсе':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);



    # спортсмен
    elif message.text.lower() == 'выступающий спортсмен':
            bot.send_message(message.chat.id, 'Вы хотите оплатить весь курс со скидкой 30% или оформить обучение в рассрочку?', reply_markup=keyboard5)
    elif message.text.lower() == 'полностью (спортсмен)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);
    elif message.text.lower() == 'в рассрочку (спортсмен)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);


    # тренер
    elif message.text.lower() == 'тренер':
            bot.send_message(message.chat.id, 'Вы хотите оплатить весь курс со скидкой 30% или оформить обучение в рассрочку?', reply_markup=keyboard6)
    elif message.text.lower() == 'полностью (тренер)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);
    elif message.text.lower() == 'в рассрочку (тренер)':
        bot.send_message(message.chat.id, '<a href="https://kettlebellschool.com/#rec99375761">Перейти на сайт курса</a>',
                         parse_mode="HTML",reply_markup=keyboard1);


    # СЕМИНАР
    elif message.text.lower() == 'посетить семинар':
        bot.send_message(message.chat.id, '<a href="https://idkbc.com/seminary/">Ознакомиться с календарём</a>',
                         parse_mode="HTML",reply_markup=keyboard1)

   # КОНСУЛЬТАЦИЯ
    elif message.text.lower == 'консультация':
        CONTACTS(message)

   # МАГАЗИН - либо слайды, либо тупо список
    elif message.text.lower() == 'магазин':
        bot.send.message(message.chat.id, '<a href="https://idkbc.com/shop/">Ознакомьтесь со всеми товарами на сайте!</a>', parse_mode="HTML", reply_markup=keyboard1)
        """bot.send_message(message.chat.id, 'Я пока хз че сюда добавить, но пока изучи ассортимент. Скорее всего сделаем такую сортировку с вот такими товарами всплывающими и с гиперссылкой', reply_markup=keyboard7)
        photo = open('1.jpg', "rb")
        bot.send_photo(message.chat.id, photo, caption= 'Бамперный диск 10кг, 3500р.', reply_markup=keyboard7);
    elif message.text.lower() == 'назад':
        photo1 = open('4.jpg', "rb")
        bot.send_photo(message.chat.id, photo1, caption = 'Ты чё, пиздюк, ниче не купил?', reply_markup=keyboard1)"""

# ОБРАБОТКА КОНТАКТА
@bot.message_handler(func=lambda message: True, content_types=['contact'])
def CONTACTS(message): # получаем данные клиента
    global tel_id
    global tel_ph
    global tel_name
    a = message.contact.user_id
    b = message.contact.phone_number
    c = message.contact.first_name
    print(b)
    print(c)
    print(a)

    bot.send_message(conf.bossid, ''+str(b)+' телефон, '+str(c)+' имя ' )



bot.polling(none_stop=True, interval=0)