<h1 align="center">
    <samp>Telegram Forwarder Enhanced</samp>
</h1>


![telegram-forwarder-enhanced](/images/feature.png)


<p align="center">
    <img alt="GitHub License" src="https://img.shields.io/github/license/Warnigo/telegram-chanal-copy?style=flat&label=license&labelColor=%23ffffff&color=%23454545">
</p>

## About
[![About](http://www.randomnoun.com/wpf/shell32-avi/tshell32_160.gif)](#)

Telegram Forwarder Enhanced is a simple and effective tool developed in Python with Telethon to copy and forward messages between Telegram channels and groups quickly, safely, and automatically.

The project supports text, images, videos, and documents, and includes features such as automatic resume after interruptions, duplicate message detection, and protection against Telegram [FloodWait](https://core.telegram.org/api/errors#420-flood).

>> [Versão em Português](README_ptbr.md)
## ⚠️ Legal Disclaimer and Usage Risks

This script uses the **Telegram MTProto API via Telethon with user account credentials** (not a bot account). This means it operates as if you were logged into Telegram directly, which allows access to private channels and content forwarding.

Telegram may consider automated usage of this type a violation of its [Terms of Service](https://telegram.org/tos), particularly at scale or for mass channel copying. This may result in **temporary or permanent suspension of your account and/or `api_id`**.

**Additional behavior to consider:**
- Forwarding via `forward_messages` relies on how Telegram resolves media references server-side. This behavior may change in future Telegram API or Telethon library updates without prior notice, potentially causing silent failures or broken functionality.

**Use at your own risk. The author takes no responsibility for bans, data loss, or any consequences resulting from the use of this tool.**

> **📤 About forwarding:** The script uses Telegram's `forward_messages` API method, forwarding messages directly between channels server-side — without downloading media locally. This minimizes network usage and local storage, but messages will appear with a "Forwarded from" tag at the destination. This behavior is intentional.


## ✨ Features

- 📋 Clones a **Telegram channel or group** (compatible public or private channels/groups).
- 🔄 You **must be a member** of the channel or group to copy its content.
- 🛠 Supports text, images, PDFs, and videos.
- ⏱ Safe execution flow with random pauses to avoid flooding.
- 🆔 Message ID listing to prevent duplicate sending.

## 🚀 Improvements in This Version

- Fixed media sending failures
- Automatic resume after interruptions
- Better FloodWait handling
- Anti-duplication system
- Improved Telethon stability
- Compatibility with recent versions

## 🤝 Credits

This project is a fork of the original [telegram-chanal-copy](https://github.com/warnigo/telegram-chanal-copy) repository created by Warnigo. We thank the original author for their contribution. All original copyrights are retained under the MIT license.

## Installation

### 📂 Clone the Repository

```bash
git clone https://github.com/WaggBR/telegram-forwarder-enhanced.git

cd telegram-forwarder-enhanced
```

## 🛠 Settings

### 1. Edit the [config.py](./config.py) file before running.

- `API_ID` and `API_HASH` - Get these values from [my.telegram.org](http://my.telegram.org/)
- `PHONE_NUMBER` - Your phone number with country code (e.g.: +55199999999)
- `NAME` - A name of your choice
- `SOURCE_CHAT_ID` and `DESTINATION_CHAT_ID` - IDs obtained from Telegram channels/groups.

### How to Get the `chat_id` of a Channel or Group

There are several ways to get the `chat_id` of a channel or group. Here are two simple methods:

#### Using the Telegram Client [Kotatogram](https://kotatogram.github.io/download/):

- Open the channel or group
- Go to the channel/group description screen
- Copy the `chat_id` displayed below the channel/group name

#### Using the Telegram Bot [@username_to_id_bot](https://t.me/username_to_id_bot)

- Open the bot and start it
- Forward any message from the channel/group to the bot
- The bot will reply with the sender ID
- Copy the `chat_id` exactly as displayed (including the minus sign)

> [!NOTE]
> Telegram channels and supergroups usually start with `-100`.

#### `config.py` Example:

```python
class Config:
    API_ID = "12345678"                  # Your API ID
    API_HASH = "your_api_hash"           # Your API Hash
    PHONE_NUMBER = "+5511999999999"      # Your number with country code
    NAME = "telegram-forwarder"          # Chosen name
    SOURCE_CHAT_ID = -1001234567890      # Source channel/group ID
    DESTINATION_CHAT_ID = -1009876543210 # Destination channel/group ID
```


>[!NOTE]
>Make sure to replace the placeholders with your real credentials.


## 🐍 Virtual Environment Setup

Using a virtual environment is highly recommended to avoid dependency conflicts.

- #### Windows

```sh
python -m venv myenv
```

- #### macOS and Linux

```sh
python3 -m venv myenv
```

### Activate the Virtual Environment

- #### Windows

```powershell
.\myenv\Scripts\activate
```
> [!NOTE]
> **It should return:** `(myenv) C:\Users\`


- #### macOS and Linux

```bash
source myenv/bin/activate
```

> [!NOTE]
> To deactivate the virtual environment at any time, simply run the following command:

```bash
deactivate
```

## 📦 Dependency Installation

The script uses the Telethon library to interact with Telegram.

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

```powershell or CMD
python bot.py
```

- #### macOS and Linux

```bash
python3 bot.py
```

## 📋 Usage Instructions
When running the script, you will be asked whether you want to load new messages or resend all messages from the source channel.

- Type `y` to copy only new messages from the source channel to the destination.
- Type `n` to copy all messages again from the source to the destination.

>[!NOTE]
> If you interrupt the script and restart it, you can choose to continue from where you left off or start from scratch.

## 🛠 Troubleshooting
- Make sure you have joined the source and destination channels/groups before running the script.
- Double-check your API credentials if you encounter authentication errors.
  If the script stops unexpectedly, you can run it again.
  Use the y/n prompt to control which content will be copied.

## 🤝 Community Contributions

Pull Requests are welcome!

If you have ideas for improvements, fixes, or new features, open an *Issue* for discussion or submit a *Pull Request* directly.

## ❤️ Support
If you find this project useful, please give the repository a star ⭐️ to show your support!

<p align="center"> <samp>Based on the original project by Warnigo</samp> </p> 
<p align="center">
  <samp>
    Enhanced and actively maintained by
    <a href="https://github.com/WaggBR">WaggBR</a>
  </samp>
</p>
<p align="center">
  <a href="https://t.me/Wagg13">
    <img src="https://img.shields.io/badge/Telegram-Contact-2CA5E0?logo=telegram&logoColor=white"/>
  </a>
</p>
