from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
import wikipedia
wikipedia.set_lang("uz")
#https://t.me/MATHtestchannel
channel = "@MATHtestchannel"
admin_id = "7151642135"
son1 = 0
son2 = 0
amal = ""
ildiz = 0
ism = ""
t = ""


#7288450518:AAG1cZQmkj3Zk2LmsG93QWyolbTCXM-zLVk
bot = TeleBot('7402806309:AAFV5sMbwlWFx1sdV080wsqiVg3QGXFjrA8')
#7402806309:AAFV5sMbwlWFx1sdV080wsqiVg3QGXFjrA8
def test10():
    test10_1 = InlineKeyboardMarkup(row_width=3)
    test10_1.add(InlineKeyboardButton("A)", callback_data="A10"), InlineKeyboardButton("B)", callback_data="B10"), InlineKeyboardButton("C)", callback_data="C10"))
    return test10_1

def test9():
    test9_1 = InlineKeyboardMarkup(row_width=3)
    test9_1.add(InlineKeyboardButton("A)", callback_data="A9"), InlineKeyboardButton("B)", callback_data="B9"), InlineKeyboardButton("C)", callback_data="C9"))
    return test9_1

def test8():
    test8_1 = InlineKeyboardMarkup(row_width=3)
    test8_1.add(InlineKeyboardButton("A)", callback_data="A8"), InlineKeyboardButton("B)", callback_data="B8"), InlineKeyboardButton("C)", callback_data="C8"))
    return test8_1

def test7():
    test7_1 = InlineKeyboardMarkup(row_width=3)
    test7_1.add(InlineKeyboardButton("A)", callback_data="A7"), InlineKeyboardButton("B)", callback_data="B7"), InlineKeyboardButton("C)", callback_data="C7"))
    return test7_1

def test6():
    test6_1 = InlineKeyboardMarkup(row_width=3)
    test6_1.add(InlineKeyboardButton("A)", callback_data="A6"), InlineKeyboardButton("B)", callback_data="B6"), InlineKeyboardButton("C)", callback_data="C6"))
    return test6_1

def test5():
    test5_1 = InlineKeyboardMarkup(row_width=3)
    test5_1.add(InlineKeyboardButton("A)", callback_data="A5"), InlineKeyboardButton("B)", callback_data="B5"), InlineKeyboardButton("C)", callback_data="C5"))
    return test5_1

def test4():
    test4_1 = InlineKeyboardMarkup(row_width=3)
    test4_1.add(InlineKeyboardButton("A)", callback_data="A4"), InlineKeyboardButton("B)", callback_data="B4"), InlineKeyboardButton("C)", callback_data="C4"))
    return test4_1

def test3():
    test14 = InlineKeyboardMarkup(row_width=3)
    test14.add(InlineKeyboardButton("A)", callback_data="A3"), InlineKeyboardButton("B)", callback_data="B3"), InlineKeyboardButton("C)", callback_data="C3"))
    return test14

def test2():
    test11 = InlineKeyboardMarkup(row_width=3)
    test11.add(InlineKeyboardButton("A)", callback_data="A2"), InlineKeyboardButton("B)", callback_data="B2"), InlineKeyboardButton("C)", callback_data="C2"))
    return test11

def test1():
    test13 = InlineKeyboardMarkup(row_width=3)
    test13.add(InlineKeyboardButton("A)", callback_data="A1"), InlineKeyboardButton("B)", callback_data="B1"), InlineKeyboardButton("C)", callback_data="C1"))
    return test13

def test12():
    btnm = InlineKeyboardMarkup()
    btnm.add(InlineKeyboardButton("Testni boshlash", callback_data="text"))
    return btnm

def true():
    ta = ReplyKeyboardMarkup()
    ta.add(KeyboardButton("Ma'umotlar toʻgʻri 100%"), KeyboardButton("Testda qatnashish"))
    return ta
def error():
    e = InlineKeyboardMarkup()
    e.add(InlineKeyboardButton("-Orqaga" , callback_data="back"))
    return e
def obuna():
    m = InlineKeyboardMarkup(row_width=1)
    n1 = InlineKeyboardButton("Obuna boʻlish ✅", url="https://t.me/MATHtestchannel")
    n2 = InlineKeyboardButton("Obuna boʻldim ✅", callback_data='obuna')
    m.add(n1, n2)
    return m

def ishora():
    i = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("Qoʻshish")
    b2 = KeyboardButton("Ayrish")
    b3 = KeyboardButton("Koʻpaytirish")
    b4 = KeyboardButton("Boʻlish")
    i.add(b1, b2)
    i.add(b3, b4)

return i
    
def k1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Kalkulyator'), KeyboardButton("Ildiz"))
    markup.add(KeyboardButton("Kvadrat²"), KeyboardButton("Kub³"))
    markup.add(KeyboardButton("Tasodifiy raqam"))
    markup.add(KeyboardButton("Testda qatnashish"))
    return markup

@bot.message_handler(commands=['search', 'wiki'])
def search(m):
    bot.send_message(m.chat.id, "Qidirmoqchi boʻlgan soʻzni yuboring!")
    bot.register_next_step_handler(m, get_search)
    
@bot.message_handler(commands=['start'])
def start(m):
    b = bot.get_chat_member(channel, m.from_user.id).status
    if b != "left":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "Assalomu Alaykum men kalkulyator botman", reply_markup=k1())
        bot.send_message(admin_id, f"Botga {m.from_user.first_name} /start buyrugʻini yubordi.\n\nIsmi:  {m.from_user.first_name}\n\nUsername:  {m.from_user.username}\n\nID:  {m.from_user.id}")
    else:
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

@bot.message_handler(content_types=['text'])
def get_text(m):
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if channeltest != "left":
        if m.text == 'Kalkulyator':
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_son1)
        elif m.text == "Ma'umotlar toʻgʻri 100%":
            bot.send_message(m.chat.id, "Tayyor boʻlsngiz qiyidagi tugmani bosing! 👇", reply_markup=test12())
            bot.delete_message(m.chat.id, m.message_id)
            bot.delete_message(m.chat.id, m.message_id - 1)
        elif m.text == "Testda qatnashish":
            bot.send_message(m.chat.id, "👋")
            bot.send_message(m.chat.id, "👋\nKeling testni boshlashdan oldin siz bilan tanishib olamiz! ✅")
            bot.send_message(m.chat.id, "Iltimos ismingizni kiriting!")
            bot.register_next_step_handler(m, get_name)
        elif m.text == 'Tasodifiy raqam':
            bot.send_message(m.chat.id, "Tasodifiy raqam tanlandi : " + str(random.randint(1, 100)) + " ✅")
        elif m.text == 'Ildiz':
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_Ildiz)
        elif m.text == 'Kvadrat²':
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_kv)
        elif m.text == 'Kub³':
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_kub)
    else:
        bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())



def get_son1(m):
    global son1
    son1 = m.text
    bot.send_message(m.chat.id, "Ishorani tanlang", reply_markup=ishora())
    bot.register_next_step_handler(m, get_amal)

def get_amal(m):
    global amal
    amal = m.text
    bot.send_message(m.chat.id, "Ikkinchi sonni kiriting")
    bot.register_next_step_handler(m, get_son2)

def get_son2(m):
    global son2
    son2 = m.text
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if channeltest != "left":
        if amal == "Qoʻshish":
            bot.send_message(m.chat.id, f"Javob: {int(son1) + int(son2)}", reply_markup=k1())
        elif amal == "Ayrish":
            bot.send_message(m.chat.id, f"Javob: {int(son1) - int(son2)}", reply_markup=k1())
        elif amal == "Koʻpaytirish":
            bot.send_message(m.chat.id, f"Javob: {int(son1) * int(son2)}")
        elif amal == "Boʻlish":
            if son2 > "0" or son2 < "0":
                bot.send_message(m.chat.id, f"Javob: {int(son1) / int(son2)}", reply_markup=k1())
            elif son2 == "0":
                bot.send_message(m.chat.id, "Boʻlish imkonsiz", reply_markup=k1())
        else:
            bot.send_message(m.chat.id, "Amal notoʻgʻri", reply_markup=k1())
    else:
        bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

def get_search(m):
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if channeltest != "left":
        try:
            wikipedia.summary(m.text)
            bot.send_message(m.chat.id, wikipedia.summary(m.text))
        except:
            bot.send_message(m.chat.id, "Men sizni umuman tushunmadim!")
    else:
        bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

def get_Ildiz(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 0.5}", reply_markup=k1())

def get_kv(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 2}", reply_markup=k1())
def get_kub(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 3}", reply_markup=k1())
    
@bot.callback_query_handler(func=lambda call: True)
def call(call):
    test = bot.get_chat_member(channel, call.from_user.id).status
    if test != "left":
        if call.data == "obuna":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "Assalomu Alaykum men kalkulyator botman", reply_markup=k1())
        elif call.data == "text":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, f"1). Hisoblang:  -78+1745 = ?\nA) 1567\nB) 1667\nC) 1777", reply_markup=test1())
        elif call.data == "A1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        elif call.data == "B1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "C1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"2). Hisoblang:\n( 55 + 344 ) -- ( 122 + 44 ) = ? \nA) 203\nB) 213\nC) 233", reply_markup=test2())
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        elif call.data == "A2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        elif call.data == "B2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        elif call.data == "C2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"3). Hisoblang:  0,25*250= ?\nA) 62,5\nB) 63,5\nC) 64,5", reply_markup=test3())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "A3":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "B3":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)

bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
        elif call.data == "C3":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"4). Hisoblang :   ( 33 * 6 ) : 4 = ?\nA) 48,5\nB) 49,5\nC) 50,5", reply_markup=test4())
        elif call.data == "A4":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
        elif call.data == "B4":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "C4":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"5). Hisoblang:  1430 : 26 : 5 = ?\nA) 9\nB) 11\nC) 12", reply_markup=test5())
        elif call.data == "A5":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
        elif call.data == "B5":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "C5":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"6). Hisoblang:  - 2340 + 2677 = ?\nA) 337\nB) 347\nC) 357", reply_markup=test6())
        elif call.data == "A6":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "B6":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
        elif call.data == "C6":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"7). Hisoblang:  ( - 977 - 178 ) : 5 = ?\nA) -211\nB) -221\nC) -231", reply_markup=test7())
        elif call.data == "A7":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())
        elif call.data == "B7":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())

        elif call.data == "C7":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"8). Hisoblang:  ( 975 : 5 ) * 2 = ?\nA) 390\nB) 400\nC) 420", reply_markup=test8())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "A8":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "B8":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
        elif call.data == "C8":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"9). Hisoblang:  (6754-1456): 3= ?\nA) 1766\nB) 1966 \nC) 2266", reply_markup=test9())
        elif call.data == "A9":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "B9":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
        elif call.data == "C9":
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"10). Hisoblang:  ( 456 + 566 ) : 2= ?\nA) 502\nB) 511\nC) 521", reply_markup=test10())
        elif call.data == "A10":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        elif call.data == "B10":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="✅", show_alert=True)
        elif call.data == "C10":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="🚫", show_alert=True)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
            bot.answer_callback_query(callback_query_id=call.id, text="Barcha kanallarga obuna boʻlishingiz shart! ✅", show_alert=True)
        
def get_name(m):
    global ism
    ism = m.text
    bot.send_message(m.chat.id, "Yaxshi endi familiyangizni kiriting!")
    bot.register_next_step_handler(m, get_yosh)
def get_yosh(m):
    global t
    t = m.text
    bot.send_message(m.chat.id, "Yoshingiz nechada?")
    bot.register_next_step_handler(m, tasdiqlash)
def tasdiqlash(m):
    global ildiz
    ildiz = m.text
    bot.send_message(admin_id, "Yangi fiydalanuvchi\nIsmi: " + ism + "\n" + "<b>Familiyasi: </b>" + t + "\n" + "Yoshi: " + ildiz + "\n" + "Username: " + "@" + m.from_user.username + "\n" + "ID: " + str(m.from_user.id), parse_mode='html')

bot.send_message(m.chat.id, "Ma'lumotlaringiz toʻgʻri ekanligini tekshiring!\n\n\n" + "Ismingiz: " + ism + "\n" + "Familiyangiz: " + t +  "\n" + "Yoshingiz: " + ildiz + "\n\n\n" + "\n\nAks holda <b>«Testda qatnashish»</b> tugmasini bosib qayta roʻyxatdan oʻting!", parse_mode='html', reply_markup=true())



bot.polling()
