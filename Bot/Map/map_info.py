import random
import requests
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *

mainEndpoint = 'https://valorant-api.com/v1/'

async def getMapUuid(ctx, map_name):
    endpoint = mainEndpoint + 'maps'
    response =  requests.get(endpoint).json()
    for map in response['data']:
        if map['displayName'] == map_name:
            map_uuid = map['uuid']
            print(map_uuid)
            return map_uuid
            
    await ctx.send(f"Map '{map_name}' not found")

async def Mapbanner(ctx, map_name):
    map_uuid = await getMapUuid(ctx, map_name)
    if map_uuid == None:
        return
    else:
        endpoint = f'https://valorant-api.com/v1/maps/{map_uuid}'
        response = requests.get(endpoint).json()
        listview = response['data']['listViewIcon']
        
        await ctx.send(listview)
        
async def Random_Mapbanner():
    maplist = await getlistmapuuids()
    random_uuid = random.choice(maplist)
    endpoint = f'https://valorant-api.com/v1/maps/{random_uuid}'
    response = requests.get(endpoint).json()
    listview = response['data']['listViewIcon']
    print(listview)
    return listview

async def getlistmapuuids():
    endpoint = mainEndpoint + 'maps'
    response =  requests.get(endpoint).json()
    maplist = []  # Initialize maplist outside the loop
    for map in response['data']:
        maplist.append(map['uuid'])  # Add UUID to the list
    return maplist
