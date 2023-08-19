import nextcord
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *
import Agent.agent_info as agent_info
from Agent.agent_info import *

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def Agent(ctx, agent_name):
    await agent_info.Agent(ctx, agent_name)

bot.run(secrets.token_bot())