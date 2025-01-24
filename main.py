
import discord
from bot_mantik import gen_pass

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("Şifreniz: " + gen_pass(10))


client.run(
    "TOKEN")
