import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://beingtek.com/ref/GreyMatter658')
    START_TXT = """<b>๐ง๐พ๐๐๐ {},
๐'m ๐  ๐ณ๐พ๐๐พ๐๐๐บ๐ ๐ฒ๐๐๐๐๐พ ๐ฏ๐๐พ ๐ฅ๐๐ผ๐๐๐๐๐พ๐ฝ ๐ ๐๐๐๐ฅ๐๐๐๐พ๐ ๐ก๐๐.๐จ๐๐ ๐ค๐บ๐๐ ๐ณ๐ ๐ด๐๐พ ๐ฌ๐พ ):\n๐ฉ๐๐๐ ๐ ๐ฝ๐ฝ ๐ฌ๐พ ๐ณ๐ ๐ธ๐๐๐ ๐ฆ๐๐๐๐ ๐ ๐ Admin,๐ง๐๐ ๐ณ๐๐พ help ๐ฅ๐๐ ๐ฌ๐๐๐พ ๐จ๐๐ฟ๐</b>"""
    HELP_TXT = """๐ง๐พ๐ {}
๐ง๐พ๐๐พ ๐จ๐ ๐ฌ๐ ๐ง๐พ๐๐ ๐ข๐๐๐๐บ๐๐ฝ๐."""
    ABOUT_TXT = """
<b>โฅ  ๐ฌ๐ ๐ญ๐บ๐๐พ</b> : <b><i><a href="https://t.me/MC_MovieBot">Mแดแด ษชแด Bแดแด ๐</a></i></b>
<b>โฅ  ๐ฎ๐๐๐พ๐</b> : <b><i><a href="https://t.me/TomHiiddleston">Tแดแด Hษชแดแดสแดsแดแดษด</a></i></b>
<b>โฅ ๐ข๐๐พ๐ฝ๐๐๐</b> : <code>Everyone in this journey</code>
<b>โฅ ๐ฃ๐บ๐๐บ๐ป๐บ๐๐พ</b> : <b><a href="https://www.mongodb.com/">MongoDB</a></b>
<b>โฅ ๐ซ๐บ๐๐๐๐บ๐๐พ</b> : <code>Python3</code>
<b>โฅ ๐ซ๐๐ป๐๐บ๐๐</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>
<b>โฅ ๐ฒ๐พ๐๐๐พ๐</b> : <code>AWS</code>
<b>โฅ ๐ก๐๐๐๐ฝ ๐ฒ๐๐บ๐๐</b> : <code>V8.0 [BETA]</code>

ยฉ๏ธ MแดษชษดแดแดษชษดแดD Bส  <a href=https://t.me/MovieClubOfficiall>Mแดแด ษชแด Cสแดส</a>"""
    SOURCE_TXT = """
<code>All the files in this bot are freely available on the internet or posted by somebody else.This bot is indexing files which are already uploaded on Telegram for easy of searching, We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact us so that it can be removed asap.</code>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/GreyMatter_Owner)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>แโบ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>แโบ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>แโบ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ  
    
<b>แโบ ๐๐ - <code>{}</code></b>
<b>แโบ ๐๐๐ฆ๐ - {}</b>
"""
