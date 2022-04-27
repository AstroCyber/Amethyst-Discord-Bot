import nextcord
import random
import aiohttp
from io import BytesIO
from itertools import permutations
import json
from main import *
from nextcord.ext import commands

CoinStorage=[]
UIDstorage=[]

slots = [":coin:",":gem:",":fire:",":ice_cube:",":jack_o_lantern:",":roll_of_paper:",":poop:",":hourglass_flowing_sand:",":crossed_swords:"]

async def rando1():
    randoEmoji1 = random.choice(slots)
    return randoEmoji1
async def rando2():
    randoEmoji2 = random.choice(slots)
    return randoEmoji2
async def rando3():
    randoEmoji3 = random.choice(slots)
    return randoEmoji3

def full():
    money = random.randrange(100,1000)
    return money
def half():
    money = random.randrange(50,200)
    return money

async def AddEmoji(ctx, url, messages, *, name):
    guild = ctx.guild
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:

                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        if messages == True:
                            await ctx.reply(f'Successfully Created Emoji {emoji}')
                        await ses.close()
                    else:
                        if messages == True:
                            await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()

                except nextcord.HTTPException:
                    if messages == True:
                        await ctx.send('File size is too big!')

async def get_data():
    with open("database.json", "r") as f:
        users = json.load(f)
    return users

async def accounter(user):
    users = await get_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 100
        users[str(user.id)]["bank"] = 100
        users[str(user.id)]["bank space"] = 1000
        users[str(user.id)]["inv"] = {"StarterPack": {"img": "", "amount": 1}, "BankSpace": {"img": "", "amount": 1}}
    with open("database.json", "w") as f2:
        json.dump(users, f2)

async def update_bank(money, user):
    users = await get_data()
    bank = users[str(user.id)]["bank"]
    bank_space = users[str(user.id)]["bank space"]
    if money+bank > bank_space:
        ft = False
    else:
        users[str(user.id)]["bank"] += money
        with open("database.json", "w") as f3:
            json.dump(users, f3)
        ft = True
    return ft

async def update_wallet(money, user):
    users = await get_data()
    users[str(user.id)]["wallet"] += int(money)
    with open("database.json", "w") as f3:
        json.dump(users, f3)

async def random_names():
    with open("names.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split(",")))
        return random.choice(words)

def all_cmds(message):
    alls = [''.join(x) for x in permutations(list(message)+list(message.upper()), 3) if ''.join(x).lower() == message]
    for all in alls:
        if all == message:
            alls.remove(all)
    print(alls)
    return alls
