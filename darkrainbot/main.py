from webserver import keep_alive
import os
import datetime
import discord
from discord.ext import commands
from discord.utils import get
import random

# Activar intents para que el bot pueda leer más eventos
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)

# Mantener vivo si usas Replit u hosting similar
keep_alive()

# Token desde variable de entorno (no ponerlo directo en el código)
TOKEN = os.environ.get("DISCORD_BOT_SECRET")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="D4rkrain", url=""))
    print("✅ Bot is ready")

@bot.command()
async def stats(ctx):
    server_owner = "DarkRain"
    embed = discord.Embed(
        title=f"{ctx.guild.name}",
        description="**Stats del Servidor**",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.dark_purple()
    )
    embed.add_field(name="Server Owner", value=server_owner)
    embed.add_field(name="Server ID", value=ctx.guild.id)
    embed.add_field(name="Server created at", value=ctx.guild.created_at)
    await ctx.send(embed=embed)

@bot.command()
async def ruletarusa(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🔫 Salió el número: **{numero}**")

@bot.command()
async def twitch(ctx):
    await ctx.send("**Twitch de Darkrain es:** ")

@bot.command()
async def youtube(ctx):
    await ctx.send("**YouTube de Darkrain es:** ")

@bot.command()
async def yt(ctx):
    await ctx.send("**YouTube de D4rkrain es:** ")

@bot.command()
async def ing(ctx):
    await ctx.send("**El Instagram de Darkrain es**: ")

@bot.command()
async def nick(ctx):
    await ctx.send("Darkrain se llama **d4rkr4in** en Minecraft")

@bot.command()
async def ayuda(ctx):
    await ctx.send(
        "```Ayuda - Comandos\n\n"
        "Twitch: Link al Twitch de Darkrain\n"
        "Stats: Información del servidor\n"
        "Youtube/YT: Link al YouTube de Darkrain\n"
        "Nick: Nombre de Darkrain en Minecraft\n"
        "Twitter: Twitter de Darkrain\n"
        "ING: Instagram de Darkrain```"
    )

@bot.command(pass_context=True)
async def conectar(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ No estás conectado a un canal de voz")
        return
    canal = ctx.author.voice.channel
    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        await canal.connect()

@bot.command(pass_context=True)
async def desconectar(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.disconnect()
    else:
        await ctx.send("❌ El bot no está en un canal de voz")

