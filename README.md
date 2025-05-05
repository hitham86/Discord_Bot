Python Discord Bot 🤖
A Python-based Discord bot using discord.py that listens for messages, responds to simple commands, and handles reactions. Great starting point for building more complex bots.

📋 Features
Responds to simple messages like hi, bye, and cool

Supports command prefix (!) and includes a sample !hello command

Logs events to console and errors to error.log

Token is securely loaded from .env file

🔧 Requirements
Python Version	Supported
3.8+	✅

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/hitham86/Discord_Bot.git
cd Discord_Bot
Set up your .env file:

Create a .env file in the root directory with the following content:

env
Copy
Edit
TOKEN=your_discord_bot_token_here
⚠️ Never share your token publicly.

Run the bot:

bash
Copy
Edit
python Discord_chat.py
💬 Message Responses
Message	Bot Response
hi	"hey how are you?"
bye	"see you later"
cool	Reacts with 😎

🔧 Slash & Prefix Commands
Command	Description
!hello	Responds with "Hello there!"

You can add more commands using the @bot.command() decorator.

🛠️ Development Notes
Virtual Environment
bash
Copy
Edit
python -m venv .venv
# Activate:
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
Then install:

bash
Copy
Edit
pip install -r requirements.txt
Logging
Info-level logs print to console

Errors are saved to error.log

🔒 Security
Make sure .env and other sensitive files are excluded from Git by using .gitignore:

bash
Copy
Edit
.env
__pycache__/
*.pyc
.idea/
🙌 Contributing
Pull requests, bug reports, and suggestions are welcome!
