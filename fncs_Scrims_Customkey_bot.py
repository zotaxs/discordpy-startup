import discord
import asyncio
from discord.ext import commands
from asyncio.tasks import sleep
import time
import threading
import sched
import discord
import random
from discord import channel
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command
import datetime
import time
from datetime import datetime, timedelta

from discord.ext.commands.errors import MissingRequiredArgument
from discord.ext.commands.help import MinimalHelpCommand
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


client = discord.Client()

@client.event
async def on_ready():
    print("起動完了")



@client.event 
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '.help':
        Embed = discord.Embed(title="FORTNITE Custom Key Distribution-BOT",description="How to use bot\n全自動キー配布ボットの使い方")
        Embed.add_field(name="Command",value="Processing",inline=False)
        Embed.add_field(name=".key",value="Processing",inline=False)

#二試合トリオパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.trio 2':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")



#三試合トリオパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.trio 3':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")

#4試合トリオパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.trio 4':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#四試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Trio`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")






#ソローーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー







#二試合ソロパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.solo 2':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")



#三試合ソロパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.solo 3':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")

#4試合ソロパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.solo 4':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Trio Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#四試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Solo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Solo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")




#デュオーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


#二試合デュオパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.duo 2':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")



#三試合ソロパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.duo 3':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")

#4試合ソロパターン
@client.event 
async def on_message(message):
    channel_log = client.get_channel(886073601000865825) #ログチャンネル
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '.duo 4':

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(885000642211491891) #Trio-freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒
#二試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#三試合目ーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")
        await sleep(60)

        next_time = datetime.today()


        next_key = next_time + timedelta(minutes=40) # => 40分後key配布します(minutes=40)

        next_start = next_key + timedelta(minutes=1) #スタートの時間 (minutes=1)


        await channel_free.send("Next key "+ next_key.strftime("%H:%M") + "\n\n→ start " + next_start.strftime("%H:%M") + "\n@everyone")

        await sleep(2400)#2400秒

#四試合目ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
        num_random = random.randrange(1111,9999)
        random_key = str(num_random)

        Embed = discord.Embed(title="__↓Custorm Key__",description="__`" + random_key + "`__",color=0x2ecc71)
        Embed.set_author(name="Fncs Scrims", icon_url="https://cdn.discordapp.com/attachments/876350779651399691/897061483815522345/9_20210813085751.png")
        Embed.add_field(name="Mode",value="`Arena Duo`",inline=False)
        Embed.add_field(name="参加ルール",value="・キーの横流し\n・wkey禁止(有利がなく対面を仕掛けること)\n・<#886073601139306524>を読んで参加してください",inline=False)
        
        channel_free = client.get_channel(896210739063304222) #freeチャンネル 
        channel_Unei = client.get_channel(897429463820800030) #運営チャンネル
        channel_tokubetu = client.get_channel(871564616713523200) #特別優先
        channel_1st = client.get_channel(838371556337516564) #1st
        channel_2nd = client.get_channel(838371484682551307) #2nd
        channel_3rd = client.get_channel(838371243295375401) #3rd
        channel_4th = client.get_channel(838367561140797470) #4th

        #----------------------------------------------------------------
        await channel_Unei.send('@here\n',embed=Embed)
        await sleep(120)
        await channel_1st.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_tokubetu.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_2nd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_3rd.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_4th.send('@here\n',embed=Embed)
        await sleep(60)
        await channel_free.send('@here\n',embed=Embed)



        await sleep(60) #スタートの合図
        await channel_free.send("**Duo Scrim Started.**")

#最後ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        await sleep(600)
        await channel_free.send("﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣﹣\nToday end")

client.run('ODk3MDU2OTk4MjUwNjcyMTY4.YWQHbg.XYxk7o-H7GL_Z0z7IfHiKrkMF5g')

