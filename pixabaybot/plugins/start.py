import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pixabaybot import pixabaybot
from pixabaybot.plugins.helpers import dynamic_data_filter
from pixabaybot.plugins.texts import helptext, helptext1, helptext2, tiptext1


@pixabaybot.on_message(filters.command("start"))
async def alive(_, message):
    buttons = [[InlineKeyboardButton('How it works', callback_data='help_1')]]
    await message.reply(helptext, reply_markup=InlineKeyboardMarkup(buttons))


@pixabaybot.on_callback_query(dynamic_data_filter("help_1"))
async def help_button(_, query):
    buttons = [[InlineKeyboardButton('Next', callback_data='help_2')]]
    await query.message.edit(helptext1, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))


@pixabaybot.on_callback_query(dynamic_data_filter("help_2"))
async def tip_button1(_, query):
    buttons = [
        [InlineKeyboardButton('Previous', callback_data='help_1'),
        InlineKeyboardButton('Search', switch_inline_query_current_chat = 'backgrounds sunset'),
        InlineKeyboardButton('Next', callback_data='tip_1')]]
    await query.message.edit(helptext2, reply_markup=InlineKeyboardMarkup(buttons))


@pixabaybot.on_callback_query(dynamic_data_filter("tip_1"))
async def tip_button2(_, query):
    buttons = [[InlineKeyboardButton('Previous', callback_data='help_2')]]
    await query.message.edit(tiptext1, reply_markup=InlineKeyboardMarkup(buttons))