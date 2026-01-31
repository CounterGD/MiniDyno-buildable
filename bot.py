import os, json, asyncio
import discord
from discord.ext import commands
from core.db import init_db
from core.scheduler import check_expired
init_db()
with open('config.json') as f:
    cfg = json.load(f)
TOKEN = os.environ.get('MINIDYNO_TOKEN', cfg.get('TOKEN'))
PREFIX = cfg.get('PREFIX','!')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
@bot.event
async def on_ready():
    print('MiniDyno bot ready', bot.user)
    bot.loop.create_task(check_expired(bot))
from core.automod import is_bad_message, record_message_and_check_spam
@bot.event
async def on_message(message):
    if message.author.bot: return
    if is_bad_message(message.content):
        try:
            await message.delete()
            await message.channel.send(f"{message.author.mention} 🚫 message removed (filter)")
        except: pass
    else:
        if record_message_and_check_spam(message.author.id):
            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention} 🤐 spam detected" )
                await message.author.timeout(None)
            except: pass
    await bot.process_commands(message)
@bot.tree.command(name='ping', description='Ping')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')
async def main():
    async with bot:
        await bot.start(TOKEN)
if __name__=='__main__':
    asyncio.run(main())
