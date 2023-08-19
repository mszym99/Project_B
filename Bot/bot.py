import nextcord
import valo_api as valo
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *
import Agent.agent_info as agent_info
from Agent.agent_info import *
import Data.agent_data as agent_data
import Data.account_data as account_data
from Data.account_data import *
import Map.map_info as map_info
from Map.map_info import *
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")



@bot.event
async def on_ready():
    print("Bot is ready")
    welcome_message = (
        f"Here are a few highlighted commands to get you started:\n"
        "`!ping`: Check if the bot is responsive.\n"
        "`!Agent AgentName`: Get Agent description and abilities.\n"
        "`!Account PlayerName PlayerTag`: Get account details for a Valorant player.\n"
    )
    listview  = await map_info.Random_Mapbanner()
    general_channel = bot.get_channel(427153301889613825)
    if general_channel:
        await general_channel.send(listview)
        await general_channel.send(welcome_message)


@bot.command()
async def Agent(ctx, agent_name):
    await agent_info.Agent(ctx, agent_name)

@bot.command()
async def Account(ctx, account_name, account_tag):
    await account_data.Account(ctx, account_name, account_tag)

bot.run(secrets.token_bot())