from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "Helo, [{}](tg://user?id={})\n\n I am PATRICIA📻 bot which plays music in [PATRICIA-RADIO📻](https://t.me/PATRICIA_RADIO)"
HELP = """**Common Commands**:

**/play**  Reply with an audio to play/queue it, or show playlist
**/player**  Show current playing time of current track
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat of current group
**/leave**  Leave current voice chat
**/vc**  Check which VC is joined
**/stop**  Stop playing
**/radio** Start Radio
**/stopradio** Stops Radio Stream
**/replay**  Play from the beginning
**/clean** Remove unused RAW PCM files
**/pause** Pause playing
**/resume** Resume playing
**/mute**  Mute the VC userbot
**/unmute**  Unmute the VC userbot
**/restart** Restarts the Bot
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('BOT UPDATES💢', url='https://t.me/patricia_updates'),
        InlineKeyboardButton('RADIO GROUP📻', url='https://t.me/PATRICIA_RADIO'),
    ],
    [
        InlineKeyboardButton('OWNER🥀', url='https://t.me/PiroXpower'),
        InlineKeyboardButton('SOURCE-CODE💫', url='https://github.com/TEAM-PATRICIA/PATRICIA-RADIO'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
