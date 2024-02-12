from pyrogram import filters, Client
from pyrogram.types import Message

from Addy import OWNER, AddyBot
from Addy.database.chats import get_served_chats
from Addy.database.users import get_served_users


@AddyBot.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""Total Stats Of {(await cli.get_me()).mention} :

➻ **CHATS :** {chats}
➻ **USERS :** {users}"""
    )
