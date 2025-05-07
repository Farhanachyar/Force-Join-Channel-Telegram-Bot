# Telegram Force Join Bot

A Telegram bot that requires users to join a specific channel before they can use the bot's features. The bot also provides information about forwarded messages and user details.

## Features

- **Force Join**: Users must join a specific channel before using the bot
- **Message Information**: Get details about forwarded messages from channels or users
- **User Information**: Display user information with the `/info` command
- **Simple Interface**: Easy-to-use commands with interactive buttons

## Commands

- `/start` - Start the bot and receive a welcome message
- `/help` - Display available commands and information
- `/info` - Show information about the user

## Prerequisites

Before setting up this bot, you'll need:

- Python 3.7 or higher
- A Telegram account
- A Telegram bot token (obtained from [@BotFather](https://t.me/BotFather))
- Telegram API credentials (API ID and API HASH)

## How to Get API ID and API HASH

1. Visit [my.telegram.org](https://my.telegram.org/auth) and log in with your Telegram account
2. Click on "API Development Tools"
3. Fill in the required fields (you can use "Telegram Bot" as the app title and short name)
4. Click "Create Application"
5. Your API ID (a number) and API HASH (a string) will be displayed on the page
6. Save these credentials securely - you'll need them to set up the bot

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/telegram-force-join-bot.git
   cd force-join-channel-telegram-bot-main
   ```

2. Install the required dependencies:
   ```bash
   python -m venv venv
   venv\scripts\activate
   pip install -r requirements.txt
   ```
3. Running The Bot And Forward anything message from Targetting Channel ( Force Channel ) And you will get Channel ID / Group ID
   
4. Create a configuration file or edit the script directly with your credentials:
   - Replace `API_ID` with your Telegram API ID
   - Replace `API_HASH` with your Telegram API HASH
   - Replace `BOT_TOKEN` with your bot token from BotFather
   - Set `CHANNEL_ID` to your channel's ID (must start with -100)
   - Set `CHANNEL_URL` to your channel's url

## Usage

1. Start the bot:
   ```bash
   python bot.py
   ```

2. Open your bot in Telegram and send the `/start` command

3. If you haven't joined the required channel, the bot will prompt you to join

4. After joining the channel, you can use all the bot's features

## How to Get Channel ID

## Customization

You can customize the bot by:
- Changing the welcome messages
- Adding more commands
- Modifying the keyboard buttons
- Adding additional features as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Created by [@farhanachyar](https://github.com/farhanachyar)
- Built with [Pyrogram](https://github.com/pyrogram/pyrogram)

## Support

If you have any questions or issues, please open an issue on GitHub or contact me through Telegram.

---

⭐ Don't forget to star this repository if you find it useful!
