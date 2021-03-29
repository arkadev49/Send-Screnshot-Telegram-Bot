import os
import time
import telegram
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

COUNTRY_CODE = '+91'
PATH = ''


# ****************************************************************
#              CREATING SETUP FILES (FIRST TIME ONLY)
# ****************************************************************

f_list = os.listdir(os.getcwd())


inputs = [
    'YOUR_BOT_API_TOKEN_HERE.txt',
    'RECEIVER_ID_HERE.txt',
    'SCREENSHOT_DIR_DEFAULT_PATH_HERE.txt'
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
    exit(0)

# ****************************************************************
#           GETTING INDIVIDUAL UNIQUE SECRET INFORMATION
# ****************************************************************

try:
    with open('YOUR_BOT_API_TOKEN_HERE.txt', 'r') as fp:
        bot_api_token = fp.read()
        if bot_api_token.strip() == '':
            raise ValueError('API TOKEN MISSING!')

    with open('RECEIVER_ID_HERE.txt', 'r') as fp:
        SEND_TO = fp.read()
        if SEND_TO.strip() == '':
            raise ValueError('RECEIVER ID MISSING!')

    with open('SCREENSHOT_DIR_DEFAULT_PATH_HERE.txt') as fp:
    	PATH = fp.read()
    	if PATH.strip() == '':
    		raise ValueError('SCREENSHOT DIR DEFAULT PATH IS MISSING')
except (ValueError, FileNotFoundError) as e:
    print(e)
    print()
    print("You Must Fill Up valid ['API TOKEN', 'API ID', 'API HASH', 'YOUR PHONE NO.', "
          "'RECEIVER ID'] in the respective files before running this script.")
    exit(0)


# ****************************************************************
#            SENDING IMAGE ONCE A SCREENSHOT IS CAPTURED
# ****************************************************************


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.count = 0
        self.first_screenshot_taken = False

    def on_created(self, event):
        if not self.first_screenshot_taken:
            print(f"Observer triggered : A new file detected : {event.src_path}")
            print("The Script will not send the file using the telegram bot.")
            print("Uploading started....")
        try:
            bot = telegram.Bot(token=bot_api_token)
            bot.send_photo(SEND_TO, photo=open(event.src_path, 'rb'))
            self.count += 1
            print(f"Screenshot {self.count} : [Sent - {str(datetime.now().strftime('%d %B, %Y at %I:%M %p'))}]")
        except Exception as ev:
            print("Error Occurred : SENDING UNSUCCESSFUL!")
            print(ev)

        self.first_screenshot_taken = True


# All the down four process is happening not in the main thread..
# Daemon Thread

observer = Observer() # Initiating the Observer Object
event_handler = EventHandler() # Initiating the Event Handler Object
observer.schedule(event_handler, path=PATH) # Implanting the observer at the given path
observer.start() # Listening to Observer events....
print(f"Observer Implanted for any creation changes at path {PATH}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('A KeyboardInterrupt was raised and the observer was stopped! Re-run the script to reinitialize the observer.')
    observer.stop()

observer.join()
print('Observer was stopped successfully!')
