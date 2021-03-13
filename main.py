import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import telegram

# ****************************************************************
#              CREATING SETUP FILES (FIRST TIME ONLY)
# ****************************************************************

curr_dir = os.getcwd()
f_list = os.listdir(curr_dir)

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
#            SENDING IMAGE ONCE A SCREENSHOT IS CAPTURED
# ****************************************************************


class ExampleHandler(FileSystemEventHandler):
    count = 0

    def on_created(self, event):
        try:
            bot = telegram.Bot(token=bot_api_token)
            bot.send_photo(SEND_TO, photo=open(event.src_path, 'rb'))
            self.count += 1
            print("Screenshot send successfully! - ", self.count)
        except Exception as ev:
            print("SENDING UNSUCCESSFUL!")
            print(ev)


observer = Observer()
event_handler = ExampleHandler()
observer.schedule(event_handler, path='C:\\Users\\arkad\\Pictures\\Screenshots')
observer.start()


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
