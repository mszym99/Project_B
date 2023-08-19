import nextcord
import valo_api
import requests
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *

mainEndpoint = 'https://valorant-api.com/v1/'

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

async def getAgentUuid(ctx, agent_name):
    endpoint = mainEndpoint + 'agents'
    response =  requests.get(endpoint).json()
    for agent in response['data']:
        if agent['displayName'] == agent_name:
            agent_uuid = agent['uuid']
            return agent_uuid
            
    await ctx.send(f"Agent '{agent_name}' not found")
     



@bot.command()
async def Agent(ctx, agent_name):
   agent_uuid = await getAgentUuid(ctx, agent_name)
   #print(agent_uuid)
   if agent_uuid == None:
       return
   else:
    endpoint = f'https://valorant-api.com/v1/agents/{agent_uuid}'
    response = requests.get(endpoint).json()
    
    abilities = response['data']['abilities']
    description = response['data']['description']

    abilities_info = "\n".join([f"{ability['displayName']}: {ability['description']}" for ability in abilities])

    await ctx.send(f"**{agent_name}**\n{description}\n\n**Abilities**\n{abilities_info}\n\n")








bot.run(secrets.token_bot())