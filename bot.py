import discord
import asyncio

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

async def send_message():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = client.get_channel("channel_id") #ganti channel_id dengan ID channel Discord yang ingin Anda gunakan
        await channel.send("owoh")
        await asyncio.sleep(60) #mengatur waktu interval pengiriman pesan (dalam detik)

@client.event
async def on_ready():
    print('Bot telah login sebagai {0.user}'.format(client))
    asyncio.create_task(send_message())

async def main():
    await client.start("token") #ganti token dengan token akun Discord Anda

asyncio.run(main())
