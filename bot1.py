import discord
import asyncio

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_message():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = await client.fetch_user('usder_id') #ganti user_id dengan ID pengguna Discord 
        await channel.send("owoh")
        await asyncio.sleep(60) #mengatur waktu interval pengiriman pesan (dalam detik)

@client.event
async def on_ready():
    print('Bot telah login sebagai {0.user}'.format(client))
    asyncio.create_task(send_message())

client.run('token') #ganti token dengan token anda
