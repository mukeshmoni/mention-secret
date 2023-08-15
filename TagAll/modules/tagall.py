import asyncio
import glob
import random

from pyrogram import Client, enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from TagAll import Abishnoi
from TagAll.modules.utils.english_all import ENGLISH
from TagAll.modules.utils.hindi_all import HINDI
from TagAll.modules.utils.hr import HARYAANAVI
from TagAll.modules.utils.pnb import PUNJABI
from TagAll.modules.utils.tag_assm import ASSAMESE

chatQueue = []

stopProcess = False


@Abishnoi.on_cmd(["admins", "atags"], group_only=True, self_admin=True)
@Abishnoi.adminsOnly(permissions="can_restrict_members", is_both=True)
async def admins(client: Client, message: Message):
    try:
        adminList = []
        ownerList = []
        async for admin in client.get_chat_members(
            message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        ):
            if admin.privileges.is_anonymous == False:
                if admin.user.is_bot == True:
                    pass
                elif admin.status == ChatMemberStatus.OWNER:
                    ownerList.append(admin.user)
                else:
                    adminList.append(admin.user)
            else:
                pass
        lenAdminList = len(ownerList) + len(adminList)
        text2 = f"**ɢʀᴏᴜᴘ sᴛᴀғғ - {message.chat.title}**\n\n"
        try:
            owner = ownerList[0]
            if owner.username == None:
                text2 += f"👑 ᴏᴡɴᴇʀ\n└ {owner.mention}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
            else:
                text2 += f"👑 ᴏᴡɴᴇʀ\n└ @{owner.username}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
        except:
            text2 += f"👑 ᴏᴡɴᴇʀ\n└ <i>Hidden</i>\n\n👮🏻 ᴀᴅᴍɪɴs\n"
        if len(adminList) == 0:
            text2 += "└ <i>ᴀᴅᴍɪɴs ᴀʀᴇ ʜɪᴅᴅᴇɴ</i>"
            await client.send_message(message.chat.id, text2)
        else:
            while len(adminList) > 1:
                admin = adminList.pop(0)
                if admin.username == None:
                    text2 += f"├ {admin.mention}\n"
                else:
                    text2 += f"├ @{admin.username}\n"
            else:
                admin = adminList.pop(0)
                if admin.username == None:
                    text2 += f"└ {admin.mention}\n\n"
                else:
                    text2 += f"└ @{admin.username}\n\n"
            text2 += f"✅ | **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ ᴀᴅᴍɪɴs**: {lenAdminList}."
            await client.send_message(message.chat.id, text2)
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd("all", group_only=True, self_admin=True)
async def everyone(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 5 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = message.command[1]
                    elif len(message.command) == 1:
                        inputText = ""
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{inputText}\n\n"
                        try:
                            while j < 8:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(7)
                            i += 8
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["hrtag", "tag_haryanvi"], group_only=True, self_admin=True)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 20:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 20 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(HARYAANAVI)
                    elif len(message.command) == 1:
                        inputText = random.choice(HARYAANAVI)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(HARYAANAVI)}\n\n"
                        try:
                            while j < 1:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(5)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(
    ["tagallhindi", "htag"],
    group_only=True,
    self_admin=True,
)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 5 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(HINDI)
                    elif len(message.command) == 1:
                        inputText = random.choice(HINDI)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(HINDI)}\n\n"
                        try:
                            while j < 2:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(5)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["tagallassam", "assamtag"], group_only=True, self_admin=True)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 5 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(ASSAMESE)
                    elif len(message.command) == 1:
                        inputText = random.choice(ASSAMESE)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(ASSAMESE)}\n\n"
                        try:
                            while j < 1:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(20)
                            i += 2
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["pnbtag", "tagpunjabi"], group_only=True, self_admin=True)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 20:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 20 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(PUNJABI)
                    elif len(message.command) == 1:
                        inputText = random.choice(PUNJABI)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(PUNJABI)}\n\n"
                        try:
                            while j < 1:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(5)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["hrtag", "tag_haryanvi"], group_only=True, self_admin=True)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 20:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 20 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(HARYAANAVI)
                    elif len(message.command) == 1:
                        inputText = random.choice(HARYAANAVI)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(HARYAANAVI)}\n\n"
                        try:
                            while j < 1:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(5)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["engtagl", "tagall_en"], group_only=True, self_admin=True)
async def everyone_hindi(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 5 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(ENGLISH)
                    elif len(message.command) == 1:
                        inputText = random.choice(ENGLISH)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{random.choice(ENGLISH)}\n\n"
                        try:
                            while j < 2:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(5)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(
    ["tagallvoive", "allvoice"],
    group_only=True,
    self_admin=True,
)
async def everyone_voice(client: Abishnoi, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if len(chatQueue) > 10:
                await message.reply(
                    "⛔️ | ɪ'ᴍ ᴀʟʀᴇᴀᴅʏ ᴡᴏʀᴋɪɴɢ ᴏɴ ᴍʏ ᴍᴀxɪᴍᴜᴍ ɴᴜᴍʙᴇʀ ᴏғ 5 ᴄʜᴀᴛs ᴀᴛ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ sʜᴏʀᴛʟʏ."
                )
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | ᴛʜᴇʀᴇ's ᴀʟʀᴇᴀᴅʏ ᴀɴ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ɪɴ ᴛʜɪs ᴄʜᴀᴛ. ᴘʟᴇᴀsᴇ /stop ᴛᴏ sᴛᴀʀᴛ ᴀ ɴᴇᴡ ᴏɴᴇ."
                    )
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = random.choice(HINDI)
                    elif len(message.command) == 1:
                        inputText = random.choice(HINDI)
                    membersList = []
                    async for member in client.get_chat_members(message.chat.id):
                        if member.user.is_bot == True:
                            pass
                        elif member.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(member.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess:
                        stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        # text1 = f"{random.choice(HINDI)}"
                        text1 = " "
                        randi = glob.glob("./TagAll/modules/utils/voice/*")
                        voice = random.choice(randi)
                        try:
                            while j < 2:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await client.send_voice(
                                    message.chat.id,
                                    voice,
                                    caption=text1,
                                )
                            except Exception as e:
                                await asyncio.sleep(7)
                            i += 1
                        except IndexError:
                            try:
                                await client.send_voice(
                                    message.chat.id,
                                    voice,
                                    caption=text1,
                                )
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **ᴛᴏᴛᴀʟ ɴᴜᴍʙᴇʀ ᴏғ {i} ᴍᴇᴍʙᴇʀs**.\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    else:
                        await message.reply(
                            f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴇɴᴛɪᴏɴᴇᴅ **{i} ᴍᴇᴍʙᴇʀs.**\n❌ | ʙᴏᴛs ᴀɴᴅ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ᴡᴇʀᴇ ʀᴇᴊᴇᴄᴛᴇᴅ."
                        )
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@Abishnoi.on_cmd(["stop", "stoptagall", "cancel"], group_only=True, self_admin=True)
async def stop(client: Client, message: Message):
    global stopProcess
    try:
        try:
            sender = await client.get_chat_member(message.chat.id, message.from_user.id)
            has_permissions = sender.privileges
        except:
            has_permissions = message.sender_chat
        if has_permissions:
            if not message.chat.id in chatQueue:
                await message.reply("🤷🏻‍♀️ | ᴛʜᴇʀᴇ ɪs ɴᴏ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ᴛᴏ sᴛᴏᴘ.")
            else:
                stopProcess = True
                await message.reply("🛑 | sᴛᴏᴘᴘᴇᴅ.")
        else:
            await message.reply("👮🏻 | sᴏʀʀʏ, **ᴏɴʟʏ ᴀᴅᴍɪɴs** ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
    except FloodWait as e:
        await asyncio.sleep(e.value)
