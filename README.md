<h1 align="center">
    <samp>Telegram Chanal Copy</samp>
</h1>

<p align="center">
    A script to copy all content from a Telegram channel.  <br />
    It retrieves and saves all messages, including text, images, and links, from a specified Telegram channel for easy backup and access.
</p>

<p align="center">
    <img alt="GitHub License" src="https://img.shields.io/github/license/Warnigo/telegram-chanal-copy?style=flat&label=license&labelColor=%23ffffff&color=%23454545">
</p>

---

## ✨ Features

- 📋 Clone any **Telegram channel or group** (supports both public & private).
- 🔄 You **must be a member** of the source channel or group to copy its content.
- 🛠 Automatically handles text, images, PDFs, and videos for efficient backup.

---

### 📂 Clone this Repository

```sh
git clone https://github.com/Warnigo/telegram-chanal-copy.git

cd telegram-chanal-copy
```

## 🛠 Configuration

### 1. Edit [config.py](./config.py) file before use

- `API_ID` and `API_HASH` - Get those from [my.telegram.org](http://my.telegram.org/)
- `PHONE_NUMBER` - Give phone number with country code (ex. +998901234567)
- `NAME` - Give any name what you want
- `SOURCE_CHAT_ID` and `DESTINATION_CHAT_ID` - Get those from [@username_idbot](https://telegram.dog/username_idbot)

#### Example `config.py`:

```python
class Config:
    API_ID = "12345678"            # Your API ID
    API_HASH = "your_api_hash"     # Your API Hash
    PHONE_NUMBER = "+998901234567" # Your phone number (with country code)
    NAME = "telegram-channel"      # Any name you choose
    SOURCE_CHAT_ID = -1001234567890 # Source channel/group ID
    DESTINATION_CHAT_ID = -1009876543210 # Destination channel/group ID
```

>[!NOTE]
> Make sure to replace the placeholders with your actual credentials.

### 2. Create the config.py file

If it doesn't exist, create the configuration file:

```bash
touch config.py
```

## 🐍 Virtual Environment Setup

It's highly recommended to use a virtual environment to avoid dependency conflicts.

### 1. Create a Virtual Environment
- #### Windows

```sh
python -m venv myenv
```

- #### macOS and Linux

```sh
python3 -m venv myenv
```

### Activate Virtual Environment

- #### Windows

```powershell
.\myenv\Scripts\activate
```

- #### macOS and Linux

```bash
source myenv/bin/activate
```

> [!NOTE]
> To deactivate the virtual environment at any time, simply run:

```bash
deactivate
```

## 📦 Install Dependencies

The script relies on the Telethon library to interact with Telegram.

### Install [telethon](https://pypi.org/project/Telethon/)

- #### Windows

```powershell
pip install telethon
```

- #### macOS and Linux
 
```bash
pip3 install telethon
```

## 🚀 Running the Script

### To start copying content:

- #### Windows

```powershell
python bot.py
```

- #### macOS and Linux

```bash
python3 bot.py
```

## 📋 Usage Instructions
Upon running the script, you'll be prompted to choose whether to load new messages or resend all messages from the source channel.

- Enter `y` to only copy new messages from the source channel to the destination.
- Enter `n` to copy all messages again from the source to the destination.

>[!NOTE]
> If you interrupt the script and restart it, you can choose to continue from where you left off or start over.

## 🛠 Troubleshooting
- Make sure you have joined both the source and destination channels/groups before running the script.
- Double-check your API credentials if you encounter authentication errors.
If the script stops unexpectedly, you can rerun it. Use the y/n prompt to control what content is copied.

## ❤️ Support
If you find this project useful, please ⭐️ star the repository to show your support!

<p align="center"> <samp>Made with ❤️ by Warnigo</samp> </p> 