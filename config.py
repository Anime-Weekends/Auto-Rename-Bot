import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "28744454")
    API_HASH  = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7629093637:AAELMuIlnb0eJSikh28KRLhBmmsEy2gfviI") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Renamex")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://jeffymoses123:jeffymoses123@cluster0.ybmj0.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002402968652"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """
<b>ʜᴇʏ {} ! ✨

🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!
ᴡʜɪᴄʜ ᴄᴀɴ ᴍᴀɴᴜᴀʟʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ ᴄᴀɴ sᴇᴛ ᴘʀᴇғɪx ᴀɴᴅ sᴜғғɪx ᴏɴ ʏᴏᴜʀ ғɪʟᴇs.⚡️

✨ ᴛʜɪs ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ <a href=https://t.me/JeffySama>J૯ԲԲyઽαʍα</a>
─────────────────────────</b>
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Alya Sometimes Hides Her Feelings In Russian - [CHepisode] @Manga_Weekends </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = """
╭───────────────⍟
├<b>My Name</b> : {}
├<b>Developer</b> : <a href=https://t.me/JeffySama>Dᴇᴠᴇʟᴏᴘᴇʀ</a> 
├<b>Main Channel</b> : <a href=https://t.me/Anime_Stardust>Aɴɪᴍᴇ Sᴛᴀʀᴅᴜsᴛ</a>
├<b>Main Channel</b> : <a href=https://t.me/Anime_Weekends>Aɴɪᴍᴇ Wᴇᴇᴋᴇɴᴅs</a>
├<b>Support Channel</b> : <a href=https://t.me/Weebs_Weekends>Sᴜᴘᴘᴏʀᴛ</a>
├<b>Bot Updates</b> : <a href=https://t.me/EmitingStars_Botz>Mᴏʀᴇ Bᴏᴛᴢ</a>
├<b>Network</b> : <a href=https://t.me/Eminence_Society>Nᴇᴛᴡᴏʀᴋ</a>
├<b>Pookie</b> : <a href=https://t.me/Alisa_Zoe>Assɪsᴛᴀɴᴛ</a></b>     
╰───────────────⍟
"""
    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>clementrajadurai@okhdfcbank</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

