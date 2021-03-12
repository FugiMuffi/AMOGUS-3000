import discord
from discord.ext import commands, tasks
import asyncio
import keyboard

# CONFIG
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CHANNEL_ID = 000000000000000000
KEYBIND = 'ctrl+alt+n'


intents = discord.Intents().default()
intents.members = True

client = discord.Client(intents=intents)

is_muted = False
is_muted_bak = is_muted

async def update_mute():
    global is_muted
    global is_muted_bak
    while True:
        if is_muted is not is_muted_bak:
            print(f'value for is_muted has changed: {is_muted}')
            
            # mute everyone in the channel
            vc = client.get_channel(CHANNEL_ID)
            for member in vc.members:
                await member.edit(mute=is_muted)

            is_muted_bak = is_muted

        await asyncio.sleep(0.1)

def callback():
    global is_muted
    is_muted = not is_muted

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    activity = discord.Activity(type=discord.ActivityType.playing, name="Among Us")
    await client.change_presence(status=discord.Status.online, activity=activity)

    keyboard.add_hotkey(KEYBIND, callback)
    client.loop.create_task(update_mute())

@client.event
async def on_voice_state_update(member, before, after):
    vc = client.get_channel(CHANNEL_ID)
    global is_muted

    # user joined channel
    if before.channel is not vc and after.channel is vc:
        print(f'user {member.name} joined channel')
        await member.edit(mute=is_muted)

    # user left channel
    if before.channel is vc and after.channel is not vc and after.channel is not None:
        print(f'user {member.name} left channel')
        await member.edit(mute=False)

client.run(TOKEN)