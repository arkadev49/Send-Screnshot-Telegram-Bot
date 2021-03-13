import os
import telegram
import pyautogui as gui
from datetime import datetime

COUNTRY_CODE = '+91'

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

inputs = [
    'YOUR_BOT_API_TOKEN_HERE.txt',
    'RECEIVER_ID_HERE.txt',
]

flag = 0

for it in f_list:
    for inp in inputs:
        if inp not in f_list:
            flag = 1
            with open(inp, 'w') as fp:
                pass

if flag == 1:
    print('Setup Successful! Fill in your details in the files created and re-run the script again.')
    print('To Set a Keybinding, Create a shortcut of the \'send.vbs\' file and set a keybinding there.')
    print('Thank you for using our Setup Services.')
    exit(0)

# ****************************************************************
#           GETTING INDIVIDUAL UNIQUE SECRET INFORMATION
# ****************************************************************

try:
    with open('YOUR_BOT_API_TOKEN_HERE.txt', 'r') as fp:
        bot_api_token = fp.read()
        if bot_api_token.strip() == '':
            raise ValueError('API TOKEN MISSING!')
    # '1602420689:AAEeetAWtUatit1ubW1f821VdvJDqkQumBE'

    with open('RECEIVER_ID_HERE.txt', 'r') as fp:
        SEND_TO = fp.read()
        if SEND_TO.strip() == '':
            raise ValueError('RECEIVER ID MISSING!')
    # arkadevans
except (ValueError, FileNotFoundError) as e:
    print(e)
    print()
    print("You Must Fill Up valid ['API TOKEN', 'API ID', 'API HASH', 'YOUR PHONE NO.', "
          "'RECEIVER ID'] in the respective files before running this script.")
    exit(0)

# ****************************************************************
#    TAKING SCREENSHOT AND SAVING INTO THE 'Screenshots' Folder
# ****************************************************************

ss = gui.screenshot()
PATH = curr_dir + '\\Screenshots\\'
f_name = str(datetime.now().timestamp()) + '_Screenshot.png'

f = PATH + f_name

ss.save(f)

# ****************************************************************
#                         SENDING IMAGE
# ****************************************************************

try:
    bot = telegram.Bot(token=bot_api_token)
    bot.send_photo(SEND_TO, photo=open(f, 'rb'))
    print("Screenshot send successfully!")
except:
    print("SENDING UNSUCCESSFUL!")
