from data import *
import requests
import nextcord
import random
import aiohttp
from io import BytesIO
from itertools import permutations
import json
from nextcord.ext import commands
import urllib.request
import re

CoinStorage=[]
UIDstorage=[]

Event = ["BlackHole", "PlanetBlast", "AmethystCloud", "CoinRainPlanet", "GirlsOnlyPlanet", "ShipBlasted", "KiledByBTS", "MemerBoi", "A RabitInSpace", "FlushedYourSelf", "MinecraftNoobInToilet", "Amongus"]

slots = [":coin:",":gem:",":fire:",":ice_cube:",":jack_o_lantern:",":roll_of_paper:",":poop:",":hourglass_flowing_sand:",":crossed_swords:"]

async def update_item(item, amount, user):
    users = await get_data()
    if item not in users[str(user.id)]["inv"]:
        users[str(user.id)]["inv"][item] = {"amount": 0}
        with open("database.json", "w") as f:
            json.dump(users, f)
    users[str(user.id)]["inv"][item]["amount"] += amount
    with open("database.json", "w") as f:
        json.dump(users, f)

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

async def get_items():
    with open("items.json", "r") as f:
        users = json.load(f)
    return users

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

amethyst = commands.Bot(command_prefix="a?")

spacepic=["https://images.squarespace-cdn.com/content/v1/551a19f8e4b0e8322a93850a/1544972636400-3X0P40MZM5CQ5Q3PXDC9/Title_Image.png", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05ae7fdf-1ed9-4261-ab43-8ae6a2e1d02a/ddfoxqx-09886676-4017-4cbf-af17-8060afcd0a64.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA1YWU3ZmRmLTFlZDktNDI2MS1hYjQzLThhZTZhMmUxZDAyYVwvZGRmb3hxeC0wOTg4NjY3Ni00MDE3LTRjYmYtYWYxNy04MDYwYWZjZDBhNjQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QN7t7WLkgwC9UDjEwX-FUtZaZUGZqoMjCBFV-Uqls6w", "https://pbs.twimg.com/media/FG1l17wWYAAqa6m?format=jpg&name=large", "https://pbs.twimg.com/media/DkP7527XcAAl7Pv.png", "https://pbs.twimg.com/media/EErIPZFWwAEYZBj.png", "https://pbs.twimg.com/media/FGmw_OXWQAkHHJV?format=jpg&name=large"]


@amethyst.command()
async def cat(ctx):
  url_cat = requests.get("https://api.thecatapi.com/v1/images/search").json()
  embed_cat = nextcord.Embed(title = f"**Meow!!**", description = f"**`#LoveCats`**", color = nextcord.Colour.purple())
  embed_cat.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar.url)
  cat = url_cat[0]['url']
  embed_cat.set_image(url = cat)
  await ctx.reply(embed = embed_cat)

@amethyst.command(name="adv", aliases=["Adv", "Adventure", "adventure"])
async def adv(ctx):
    win = True
    wait = True
    Em = nextcord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", color=nextcord.Colour.purple())
    Em.set_image(url=random.choice(spacepic))
    Em.set_footer(text=f"Are You Sure {ctx.author} (Y / N)")
    EMBED = await ctx.reply(embed=Em)
    try:
        msg = await amethyst.wait_for("message", timeout=30)
        msg = msg.content
    except TimeoutError:
        await ctx.reply(f"You Took Too Long To Reply !!")
    if not msg == None:
        if msg == "Y":
            eventchoice = "AmethystCloud"
            with open("adv.json", "r") as f:
                load = json.load(f)
            event = load["events"][eventchoice]
            event_msg = event["msg"]
            won_item = event["item"]
            event_msg2 = event["msg2"]
            event_footer = event["foot"]
            won = event["won"]
            event_options = event["op"]
            color = event["color"]
            color2 = event["color2"]
            amt1 = event["amt1"]
            amt2 = event["amt2"]
            if color == "r":
                color = nextcord.Colour.red()
                if color2 == "r":
                    color2 = nextcord.Colour.red()
                else:
                    color2 = nextcord.Colour.green()
            else:
                color = nextcord.Colour.green()
                if color2 == "r":
                    color2 = nextcord.Colour.red()
                else:
                    color2 = nextcord.Colour.green()
            if event_options == "None":
                wait = False
            if won == "None":
                win = False
            EMbed = nextcord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", description=f"{event_msg}\n\n{event_msg2}", color=color)
            EMbed.set_footer(text=event_footer)
            newEMbed = nextcord.Embed(title=f"**`{ctx.author.name}'s` Adventure Game**", description=f"{event_msg}\n\n{won}", color=color2)
            await EMBED.edit(embed = EMbed)
            await update_item(won_item, amt1, ctx.author)
            if win == True:
                if wait == True:
                    try:
                        msg2 = await amethyst.wait_for("message", timeout=30)
                        msg2 = msg2.content
                    except TimeoutError:
                        msg.reply("You Took Too Long To Reply")
                    if msg2 == event_options:
                        await EMBED.edit(embed=newEMbed)
                        await update_item(won_item, amt2, ctx.author)
                else:
                    await update_item(won_item, amt2, ctx.author)



@amethyst.command(name="AddEmoji")
async def AddEmojis(ctx, url, *, name):
    await AddEmoji(ctx=ctx, url=url, messages=True, name=name)

@amethyst.command(name="RemoveEmoji")
async def DeleteEmoji(ctx, emoji: nextcord.Emoji):
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted : {emoji}')
		await emoji.delete()

@amethyst.command(name="ChangePic")
async def ChangePic(ctx, emoji: nextcord.Emoji, *,url):
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        await ctx.reply(f'Successfully Changed Emoji Photo')
        name = emoji.name
        await AddEmoji(ctx=ctx, url=url, messages=False, name=name)
        await emoji.delete()

@amethyst.command(name="RenameEmoji")
async def RenameEmoji(ctx, emoji: nextcord.Emoji, *, Name):
    if ctx.author.guild_permissions.manage_emojis_and_stickers:
        await ctx.reply(f'Successfully renamed : {emoji.name} to {Name}')
        url = emoji.url
        await AddEmoji(ctx=ctx, url=url, messages=False, name=Name)
        await emoji.delete()

@amethyst.command(name="slots", aliases=["Slots", "slot", "Slot"])
async def Slots(ctx, bet=None):
    account = await accounter(ctx.author)
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    breaker = True
    try:
        bet = int(bet)
        if bet <= 49:
            if breaker == False:
                await ctx.reply(f"Im Sorry But The Bet Should Be Higher Than 50 gems")
            breaker = False
    except:
        pass
    if bet == None:
        if breaker == False:
            await ctx.reply(f"Im Sorry But You Gotta Bet Something")
        breaker = False
    if bet > wallet:
        if breaker == False:
            if bet > wallet+bank:
                await ctx.reply(f"Im Sorry But You Dont Have Enough Money In Your Bank Or Your Wallet")
            else:
                withdraw = bet-wallet
                await ctx.reply(f"Pls Withdraw More ⏣ {withdraw}")
        breaker = False
    else:
        randoEmoji1 = await rando1()
        randoEmoji2 = await rando2()
        randoEmoji3 = await rando3()
        print(randoEmoji1,randoEmoji2,randoEmoji3)
        if randoEmoji1 == randoEmoji2:
            if randoEmoji1 == randoEmoji3:
                money = bet*3
                l_or_w = "Won"
            else:
                money = bet*2
                l_or_w = "Won"
        elif randoEmoji2 == randoEmoji3:
            money = bet
            l_or_w = "Won"
        elif randoEmoji1 == randoEmoji3:
            money = bet/2
            l_or_w = random.randrange(0,1)
        elif not randoEmoji1 == randoEmoji2:
            if not randoEmoji1 == randoEmoji3:
                money = bet
                l_or_w = "Lost"
        if l_or_w == 1:
            l_or_w = "Won"
        if l_or_w == 0:
            l_or_w = "Lost"
        if l_or_w == "Won":
            await update_wallet(money, ctx.author)
            balance = users[str(ctx.author.id)]["wallet"] + money
        elif l_or_w == "Lost":
            await update_wallet(f"-{money}", ctx.author)
            balance = users[str(ctx.author.id)]["wallet"] - money
        if breaker == True:
            embed = nextcord.Embed(title=f"{ctx.author.name}'s slot machine results\n>>  {randoEmoji1}  {randoEmoji2}  {randoEmoji3}  <<", description=f"\n\nYou {l_or_w}  ⏣ {money}\nYour Current Balance Is {balance}\n\n")
            await ctx.reply(embed=embed)

@amethyst.command(name="with", aliases=["With", "Withdraw", "WithDraw", "AddToWallet"])
async def withdraw(ctx, coins : int):
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    if coins > bank:
        await ctx.reply(f"You Can Withdraw Only Equal (or) Less Than : ⏣ {bank}")
    else:
        await update_bank(-coins,ctx.author)
        await update_wallet(coins,ctx.author)
        await ctx.reply(f"Successfully Withdrawed ⏣ {coins} From Your Bank\n\n**Bank** : {bank-coins}   **Wallet** : {wallet+coins}")

@amethyst.command(name="dep", aliases=["Dep", "Deposit", "AddToBank", "deposit"])
async def deposit(ctx, coins : int):
    users = await get_data()
    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    bank_space = users[str(ctx.author.id)]["bank space"]
    if coins > wallet:
        await ctx.reply(f"You Can Deposit Only Equal (or) Less Than : ⏣ {wallet}")
    else:
        ft = await update_bank(coins,ctx.author)
        if ft == False:
            await ctx.reply(f"Sorry But Your Bank Space Isn't Enough Pls Buy BankSpace Tokens To Upgrade Your Space\n\n```Command: a!buy B-Space (or) BankSpace```  ```CurrentSpace: {bank_space}```")
        elif ft == True:
            await update_wallet(-coins,ctx.author)
            await ctx.reply(f"Successfully Added ⏣ {coins} To Your Bank\n\n**Wallet** : {wallet-coins}   **Bank** : {bank+coins}")

@amethyst.command(name="youtube", aliases=["yt", "find video", "get link", "link", "url", "Youtube", "YT"])
async def get_url_yt(ctx, *, search):
    if " " in search:
        search = search.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    await ctx.reply("https://www.youtube.com/watch?v=" + video_ids[0])

@amethyst.command(name="Shop", aliases=["shop", "shoping", "open shop"])
async def Shop(ctx, item, number=1):
    data = await get_items()
    find = data["items"][item]
    if item == None:
        print(1)
    else:
        catagory = find["cat"]
        if "Buyable" in catagory:
            cost = find["cost"] * number
            users = await get_data()
            wallet = users[str(ctx.author.id)]["wallet"]
            if cost > wallet:
                await ctx.reply(f"Im Sorry But You Dont Have Enough Money to Buy `{number}x {item}`")
            else:
                await update_item(item, number, ctx.author)
                await update_wallet(-cost,ctx.author)
                em = nextcord.Embed(title=f"Successful {item} Purchase", description=f"{ctx.author.mention} Bought {number}x {item} And Paid `⏣ {cost}`", color=nextcord.Colour.purple())
                em.set_thumbnail(url=find["img"])
                em.set_footer(text=f"Thank You Do Visit Again :)", icon_url=ctx.author.avatar.url)
                await ctx.reply(embed=em)

@amethyst.command(name="bal", aliases=["balance", "Bal", "Balance", "BAL", "BALANCE"])
async def bal(ctx, user: nextcord.Member=None):
    if user == None:
        user = ctx.author
    account = await accounter(user)
    users = await get_data()
    wallet = users[str(user.id)]["wallet"]
    bank = users[str(user.id)]["bank"]
    em = nextcord.Embed(title=f"{user.name}'s balance")
    em.add_field(name="Wallet", value=f"⏣ {wallet}", inline=False)
    em.add_field(name="Bank", value=f"⏣ {bank}", inline=False)
    await ctx.reply(embed=em)

@amethyst.command(name="beg", aliases=["Beg", "BEG"])
async def beg(ctx):
    account = await accounter(user=ctx.author)
    luck = random.randint(a=0,b=1)
    print(luck)
    if luck == 1:
        earning = random.randrange(10,100)
    else:
        earning = 0
    if not earning == 0:
        message = f"Here Beggar Take ⏣ {earning}"
        name = await random_names()
        em = nextcord.Embed(title=f"**{name}**", description=f"'' {message} ''", colour=nextcord.Colour.green())
        em.set_footer(text=f"Begged By {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=em)
    await update_wallet(earning,ctx.author)


amethyst.run('OTM5MTQ3NTM1OTU0NjIwNDY3.Yf0nTQ.4S0oT2NvCIkLUPFvU1oGKXjmV10')