import os

from telebot import types

import telebot
# from dotenv import load_dotenv

from telegram_bot.client import TodoCleint

# load_dotenv()

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

host = os.getenv("BOT_BACKEND_HOST")
port = os.getenv("BOT_BACKEND_PORT")
clientDB = TodoCleint(host=host, port=int(port))

pred_message = ''


@bot.message_handler(commands=['start'])
def start(message):
    # user = UserPydanModel(
    #     us_id = message.from_user.id,
    #     user_name=message.from_user.first_name,
    #     username=message.from_user.username,
    #     last_name=message.from_user.last_name,
    # )
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    # body = {
    #     "user_id": user_id,
    #     "first_name": first_name,
    #     "username": username,
    #     "last_name": last_name
    # }
    result = clientDB.registration(us_id, us_name, us_sname, username)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.InlineKeyboardButton(text="Создать новую задачу", callback_data="create_task")
    btn2 = types.InlineKeyboardButton(text="Показать мои задачи", callback_data="get_tasks")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        text=f"Привет, {message.from_user.first_name}! Не запоминай все, записывай в меня и я тебе напомню!",
        reply_markup=markup)


# @bot.callback_query_handler(lambda c: c.data.startswith('create_task'))
# @bot.callback_query_handler(func=lambda call: call.data == "create_task")
# def create_task(call):
#     a = 1
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.InlineKeyboardButton("Напишите название задачи", callback_data="description_task")
#     markup.add(btn1)
#     bot.send_message(
#         call.message.chat.id,
#         text="Напишите название задачи")

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Создать новую задачу":
        bot.send_message(
            message.chat.id,
            text="Напишите свою задачу в формате:\n"
                 "название задачи: ???\n"
                 "описание задачи: ???")

    if message.text == "Показать мои задачи":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.InlineKeyboardButton(text="Изменить задачу", callback_data="update_task")
        btn2 = types.InlineKeyboardButton(text="Удалить задачу", callback_data="delete_tasks")
        markup.add(btn1, btn2)
        user_id = message.from_user.id
        result = clientDB.get_tasks(user_id)
        stroka = ''
        for i in result:
            stroka += f"{i['name']}: {i['description']}, {i['status']}, {i['id']}\n"
        bot.send_message(
            message.chat.id,
            text=stroka,
            reply_markup=markup)

    if message.text == "Удалить задачу":
        bot.send_message(
            message.chat.id,
            text="Напишите номер задачи которую необходимо удалить")
    # Удалить задачу написав в тг ее id
    if message.text in list(map(str,range(1000))):
        result = clientDB.delete_task(message.text)
        if len(result) == 1:
            stroka = result['detail']
            bot.send_message(
                message.chat.id,
                text=stroka)
            return
        stroka = f"Задача: №{result['id']}. name:{result['name']} успешно удалена"
        bot.send_message(
            message.chat.id,
            text=stroka)
    if message.text == "Изменить задачу":
        bot.send_message(
            message.chat.id,
            text="Напишите название задачи которую необходимо изменить:\n"
                 " задачу:№_\n"
                 "название:???\n"
                 "описание:???")
    # if message.text.split(':')[0] == "задачу":
    #     result = clientDB.update_task()
    #     bot.send_message(
    #         message.chat.id,
    #         text="Напишите название задачи которую необходимо изменить: задачу № _")
    else:
        # СОЗДАТЬ ЗАДАЧУ
        message_lines = message.text.split("\n")
        if len(message_lines) == 2:
            task_name = message_lines[0].split(":")[1]
            task_descripton = message_lines[1].split(":")[1]
            user_id = message.from_user.id
            status = False
            result = clientDB.create_task(task_name, task_descripton, status, user_id)


# @bot.callback_query_handler(func=lambda call: call.data == "delete_tasks")
# def button_pressed_handler(call):
#     bot.send_message(
#         call.message.chat.id,
#         text="Напишите номер задачи")


bot.polling(none_stop=True)
