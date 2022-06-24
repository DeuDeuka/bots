import asyncio, telebot, config, json
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, Chat, ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database_handler import *
from tools.getseconds import getseconds

bot = AsyncTeleBot(config.token)
data = get()
async def check(message: Message, **kwargs):
    data = get()
    for i in data:
        try:
            data[i][str(message.chat.id)].append(0)
            data[i][str(message.chat.id)].pop()
        except:
            data[i][str(message.chat.id)] = []
    try:
        data['messages_id'][str(message.chat.id)].append(message.id)
    except:
        data['messages_id'][str(message.chat.id)] = [message.id]
    set(data)
    perm = kwargs.get('is_special', False)
    is_reg(str(message.chat.id), message.from_user.username)
    if is_muted(str(message.chat.id), message.from_user.username):
        await bot.delete_message(message.chat.id, message.message_id)
        return True
    if perm:
        if message.from_user.username not in config.moderators_usernames:
            await bot.send_message(message.chat.id, 'Вы не можете пользоваться этой командой')
            return True

def is_reg(chat_id, user_id: str):
    data = get()
    if user_id not in data['users'][chat_id]:
        data['users'][chat_id].append(user_id)
    set(data)

def is_muted(chat_id, user_id: str):
    data = get()
    if user_id in data['muted'][chat_id]:
        return True
    return False

@bot.message_handler(commands=['help'])
async def help_command(message: Message):
    if await check(message):
        return
    await bot.send_message(
        message.chat.id,
        "hello!",
        reply_to_message_id = message.id    
    )

@bot.message_handler(commands=['markup'])
async def markup_command(message: Message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            'test',
            callback_data='test'
        ),
        InlineKeyboardButton(
            'test1',
            callback_data='test1'
        )
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text='test',
        reply_markup=markup,
        parse_mode='HTML'
    )

@bot.callback_query_handler(func=lambda call: True)
async def handle_query(call: CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=f'test expression: {call.data}'
    )

#Moderation
@bot.message_handler(commands=['clear'])
async def clear_command(message: Message):
    if await check(message):
        return
    content = message.text.split()
    content.pop(0)
    data = get()
    l = data['messages_id'][str(message.chat.id)][::-1]
    if content != []:
        try:
            count = int(content[0])
            if count > len(l):
                count = len(l)
            for i in range(count):
                await bot.delete_message(message.chat.id, l[i])
            for i in range(count):
                l.remove(l[i])
        except:
            await bot.send_message(
                chat_id=message.chat.id,
                text=f'{content} не число'
            )
            return
    else:
        for i in range(len(l)):
            await bot.delete_message(message.chat.id, l[i])
        l = []

    data['messages_id'][str(message.chat.id)] = l[::-1]
    set(data)

@bot.message_handler(commands=['mute'])
async def mute_command(message: Message):
    if await check(message, is_special=True):
        return
    content = message.text.split()[1:]
    if content:
        user = content.pop(0).split('@')[1]
        content = content[0]
        data = get()
        if user not in data['muted'][message.chat.id]:
            data['muted'][str(message.chat.id)].append(user)
            set(data)
            output = f'Пользователь @{user} был замучен'
            time = getseconds('111y')
            if content:
                time = getseconds(content)
                output += f' на **{time}** секунд'
            await bot.send_message(
                message.chat.id,
                output
            )
            await asyncio.sleep(time)
            data = get()
            data['muted'][str(message.chat.id)].remove(user)
            set(data)
            await bot.send_message(
                message.chat.id,
                f'Пользователь @{user} был размучен\!\nПриятного общения!', 
                parse_mode= 'MarkdownV2'
            )
        else:
            await bot.send_message(
                message.chat.id,
                f'Пользователь @{user} уже находится в муте', 
                parse_mode= 'MarkdownV2'
            )
    else:
        await bot.send_message(
                message.chat.id,
                f'Вы не дали соотвествующих параметров\.\nВыполните команду ||/help mute||', 
                parse_mode= 'MarkdownV2'
            )

@bot.message_handler(commands=['unmute'])
async def unmute_command(message: Message):
    if await check(message, is_special=True):
        return
    content = message.text.split()[1:]
    if content:
        user = content.pop(0).split('@')[1]
        data = get()
        if user not in data['muted'][str(message.chat.id)]:
            await bot.send_message(
                message.chat.id,
                f'Пользователь @{user} уже не находится в муте', 
                parse_mode= 'MarkdownV2'
            )
        else:
            data['muted'][str(message.chat.id)].remove(user)
            set(data)
            await bot.send_message(
                message.chat.id,
                f'Пользователь @{user} был размучен\!\nПриятного общения\!', 
                parse_mode= 'MarkdownV2'
            )
            
    else:
        await bot.send_message(
                message.chat.id,
                f'Вы не дали соотвествующих параметров\.\nВыполните команду ||/help mute||', 
                parse_mode= 'MarkdownV2'
            )

@bot.message_handler(func=lambda message: True)
async def handle_all_message(message: Message):
    await check(message)
    print(message.date)
        
asyncio.run(bot.polling())