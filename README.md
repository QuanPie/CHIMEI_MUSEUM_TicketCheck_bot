# CHIMEI_MUSEUM_TicketCheck_bot
Check is there any ticket soldable, if true, send a message to user by telegram bot.
## Install
1. Clone repo: `git clone https://github.com/QuanPie/CHIMEI_MUSEUM_TicketCheck_bot.git`.
2. Install Python 3.9.6 .
3. Run `pip install -r requirements.txt` to install package.
## Motivation
- I'm very upset that I didn't buy the early bird ticket, so I want to bet that someone will give up or refund the ticket.
- Refreshing and judging is too tiring, so I wrote a bot to help me.
## Setup
1. Build a file named 'config.py' in root of the repo.
2. Open 'config.py' and paste the content below.
    ```
    # config.py
    # store chat_IDs, bot_token

    class Config():
        def __init__(self):
            # bot_token, type is string
            self.bot_token = "<API_token>"
            # bot_chatIDs, type is array
            self.bot_chatIDs = ["<chatID1>", "<chatID2>"]

        @property
        def bot_token(self):
            return self._bot_token

        @bot_token.setter
        def bot_token(self, value):
            self._bot_token = value

        @property
        def bot_chatIDs(self):
            return self._bot_chatIDs

        @bot_chatIDs.setter
        def bot_chatIDs(self, value):
            self._bot_chatIDs = value
    ```
3. Get \<API_token> and \<chatID>, then replace it in `config.py`.
    -  **API_token**
        1. Go to [BotFather]('https://t.me/BotFather') .
        2. Send '/newbot' to creat a new bot.
        3. Copy HTTP API, this is your \<API_token>.

    -  **chatID**
        1. You can get chatID from these two bot.
            - https://t.me/raw_data_bot
            - https://t.me/RawDataBot
        2. Copy chat_id or user_id, this is your \<chatID>.

4. Now you can execute `tgbot.py` to check the ticket.

## Usage
- This will check the website if there is any ticket soldable.
- If any ticket is soldable, bot will send a message to me (or other user).
- If ticket is soldable, the frequency of checking will become more fast.

## LICENSE
- MIT License
