import discord
from discord.ext import commands
import requests
import time

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Ready')
    while True:
        channel = bot.get_channel(953819623122415619)
        client_id = 'w44itmy3785pbc175e9z7wchlpl9y1'
        client_secret = '26p62wuzp2fn785tciu1h0qtarotle'
        streamer_name = 'NikeTheHuman'

        body = {
            'client_id': client_id,
            'client_secret': client_secret,
            "grant_type": 'client_credentials'
        }
        r = requests.post('https://id.twitch.tv/oauth2/token', body)

        # data output
        keys = r.json();
        headers = {
            'Client-ID': client_id,
            'Authorization': 'Bearer ' + keys['access_token']
        }
        stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

        stream_data = stream.json();

        if len(stream_data['data']) == 1:
            await channel.send(f'{streamer_name} стримиет https://www.twitch.tv/nikethehuman')
            time.sleep(25200)
        else:
            time.sleep(300)


bot.run('OTUzODE5ODQ2Nzc5NDY5ODI0.YjKH9A.v2oag__DZQtPnVQUcl_QhOy30cE')
