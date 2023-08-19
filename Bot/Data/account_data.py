import json
import nextcord
import valo_api as valo
from nextcord.ext import commands
from valo_api import *
import secrets_1 as secrets
from secrets import *
import Agent.agent_info as agent_info
from Agent.agent_info import *
import Data.agent_data as agent_data

async def Account(ctx, account_name, account_tag):
    account_data = valo.get_account_details_by_name('v1',account_name, account_tag, True)
    # Create a dictionary containing the object's attributes
    account_dict = {
        "puuid": account_data.puuid,
        "region": account_data.region,
        "account_level": account_data.account_level,
        "name": account_data.name,
        "tag": account_data.tag,
        "card": {
            "id": account_data.card.id,
            "small": account_data.card.small,
            "large": account_data.card.large,
            "wide": account_data.card.wide
        },
        "last_update": account_data.last_update,
        "last_update_raw": account_data.last_update_raw
    }
    name = account_dict['name']
    tag = account_dict['tag']
    account_level = account_dict['account_level']
    account_region = account_dict['region']
    account_last_update = account_dict['last_update']
    card_wide = account_dict['card']['wide']

    # Convert the dictionary to a JSON string
    account_json = json.dumps(account_dict, indent=4)
    await ctx.send(card_wide)
    #await ctx.send(f"Account details for {account_name}:\n```json\n{account_json}\n```")
    await ctx.send(f"**Name:** {name}\n**Tag:** {tag}\n**Level:** {account_level}\n**Region:** {account_region}\n**Last Update:** {account_last_update}\n\n\n")
    