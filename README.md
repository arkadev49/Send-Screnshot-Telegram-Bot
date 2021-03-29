# Send Screenshots to Telegram Chat/Channel/Group using Bot

## Instructions :-



- **Step - 1 :** Create a virtual environment by running the following command using your terminal/cmd.

**In Windows :**

        `python -m venv venv`

**In Mac/Linux :**
        
        `python3 -m venv venv`



- **Step - 2 :** Activate the virtual environment by running the following command in your cmd/terminal after successfully setting up the virtual environment.

**In Windows :**

        `venv\Scripts\activate`

**In Mac/Linux :**

        `source venv/bin/activate`


- **Step - 3 :** Install the necessary requirements for running the script - `main.py` by executing the following command there after

**In Windows :**
        
        `pip install -r requirements.txt`

**In Mac/Linux :**

        `pip3 install -r requirements.txt`

- **Step - 4 :** Run the main script by executing the following command in your terminal/cmd

**In Windows :-**

        `py main.py`

**In Mac/Linux :-**

        `python3 main.py`


- **Step - 5 :** After running the script for the first time, three files will be created in the directory where the `main.py` script is placed. 

    The File names are : 
    - `YOUR_BOT_API_TOKEN_HERE.txt`,
    - `RECEIVER_ID_HERE.txt`,
    - `SCREENSHOT_DIR_DEFAULT_PATH_HERE.txt`

    As the name suggests, enter your created Bot API TOKEN, Receiver Chat ID from telegram and the path of the directory where your screenshots are generally saved into respective files. If you do not know how to create API token, receiver ID or Bot in telegram, kindly google it.


- **Step - 6 :** Congratulations! You have completed the setup and observer is implanted on your given path, screenshots will be automatically sent to the mentioned receiver whenever you take a screenshot. Stop the script when you're done and no screenshots will be uploaded thereafter. To start the observer again rerun the script :: `main.py`

