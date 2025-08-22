A customizable Discord bot template with basic commands for streamers/content creators.

🚀 Features
Basic social media commands (Twitch, YouTube, Instagram)

Server information

Customizable streaming status

Easy to configure and personalize

📦 Required Dependencies
bash
pip install discord.py flask
⚙️ Setup Instructions
Clone or download this project

Install the dependencies:

bash
pip install -r requirements.txt
Configure the variables in the code:

python
# Customize these values
STREAMER_NAME = "YourName"
TWITCH_URL = "https://www.twitch.tv/yourchannel"
YOUTUBE_URL = "https://www.youtube.com/yourchannel"
INSTAGRAM_URL = "https://www.instagram.com/yourprofile"
MINECRAFT_NAME = "YourMinecraftName"
SERVER_OWNER = "ServerOwner"
Set up your Discord bot token as an environment variable:

Replit: Go to "Secrets" and add DISCORD_BOT_SECRET with your token

Local: Create a .env file with:

text
DISCORD_BOT_SECRET=your_discord_bot_token_here
🎯 Available Commands
Command	Description
>help	Shows all available commands
>stats	Displays server information
>twitch	Link to Twitch channel
>youtube or >yt	Link to YouTube channel
>instagram or >ing	Link to Instagram profile
>nick	Shows Minecraft username
🔧 Creating a Discord Bot
Go to the Discord Developer Portal

Click "New Application" and give it a name

Go to the "Bot" section and click "Add Bot"

Copy the bot token (never share this publicly!)

Enable these Privileged Gateway Intents:

PRESENCE INTENT

SERVER MEMBERS INTENT

MESSAGE CONTENT INTENT

🔗 Inviting the Bot to Your Server
In the Developer Portal, go to the "OAuth2" → "URL Generator" section

Select these scopes:

bot

applications.commands

Select these bot permissions:

Send Messages

Read Message History

Embed Links

Use the generated URL to invite the bot to your server

📁 Project Structure
text
discord-bot/
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (optional)
└── README.md           # This file
🚀 Deployment
On Replit:
Create a new Python Repl

Upload the bot files

Add your token in the "Secrets" tab

Run the bot

On Your Own Server:
Install Python 3.8+

Install dependencies: pip install -r requirements.txt

Set environment variable: export DISCORD_BOT_SECRET=your_token

Run: python main.py

❓ Troubleshooting
Bot not responding: Check if the bot has the correct permissions

Module errors: Make sure all dependencies are installed

Connection issues: Verify your bot token is correct

📝 License
This project is open source and available under the MIT License.

🤝 Support
If you need help with this bot template, feel free to:

Check the Discord.py Documentation

Join the Discord API Server for community support

Note: Always keep your bot token private and never commit it to version control!
