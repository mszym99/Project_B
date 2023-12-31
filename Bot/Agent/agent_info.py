import requests
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *

mainEndpoint = 'https://valorant-api.com/v1/'

async def getAgentUuid(ctx, agent_name):
    endpoint = mainEndpoint + 'agents'
    response =  requests.get(endpoint).json()
    for agent in response['data']:
        if agent['displayName'] == agent_name:
            agent_uuid = agent['uuid']
            return agent_uuid
            
    await ctx.send(f"Agent '{agent_name}' not found")

async def getAgentImage(ctx, agent_name):
    agent_uuid = await getAgentUuid(ctx, agent_name)
    if agent_uuid == None:
        return
    else:
        endpoint = f'https://valorant-api.com/v1/agents/{agent_uuid}'
        response = requests.get(endpoint).json()
        displayIcon = response['data']['displayIcon']
        await ctx.send(displayIcon)

async def Agent(ctx, agent_name):
   agent_uuid = await getAgentUuid(ctx, agent_name)
   
   await getAgentImage(ctx, agent_name)

   #print(agent_uuid)
   if agent_uuid == None:
       return
   else:
    endpoint = f'https://valorant-api.com/v1/agents/{agent_uuid}'
    response = requests.get(endpoint).json()
    
    abilities = response['data']['abilities']
    description = response['data']['description']
    #abilityIcons = await getAgentAbilityIcons(ctx, agent_name)
    #abilities_info = "\n".join([f"{ability['displayName']}\n{ability['description']}\n{abilityIcons[i]}" for i, ability in enumerate(abilities)])
    abilities_info = "\n".join([f"{ability['displayName']}\n{ability['description']}" for i, ability in enumerate(abilities)])
    await ctx.send(f"**{agent_name}**\n{description}\n\n**Abilities**\n{abilities_info}\n\n")

async def getAgentAbilityIcons(ctx, agent_name):
    agent_uuid = await getAgentUuid(ctx, agent_name)
    if agent_uuid == None:
        return
    else:
        endpoint = f'https://valorant-api.com/v1/agents/{agent_uuid}'
        response = requests.get(endpoint).json()
        abilities = response['data']['abilities']
        ability_icons = [ability['displayIcon'] for ability in abilities]
        return ability_icons
