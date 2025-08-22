#By OrellanaJheremiasT
from webserver import keep_alive
import os
import datetime
import discord
from discord.ext import commands
from discord.utils import get
import random

bot = commands.Bot(command_prefix='>')
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")

# Customizable variables - EDIT THESE VALUES
STREAMER_NAME = "STREAMER_NAME"  # Change to streamer's name
TWITCH_URL = "https://www.twitch.tv/your_channel"  # Change to your Twitch URL
YOUTUBE_URL = "https://www.youtube.com/your_channel"  # Change to your YouTube URL
INSTAGRAM_URL = "https://www.instagram.com/your_profile"  # Change to your Instagram URL
MINECRAFT_NAME = "YourMinecraftName"  # Change to Minecraft username
SERVER_OWNER = "ServerOwner"  # Change to server owner's name

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(
        name=STREAMER_NAME, url=TWITCH_URL))
    print("Bot is ready")


@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="**Server Stats**",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.dark_purple())
    embed.add_field(name="Server Owner", value=f"{SERVER_OWNER}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    await ctx.send(embed=embed)

@bot.command()
async def twitch(ctx):
    await ctx.send(f"**{STREAMER_NAME}'s Twitch is:** {TWITCH_URL}")

@bot.command()
async def youtube(ctx):
    await ctx.send(f"**{STREAMER_NAME}'s YouTube is:** {YOUTUBE_URL}")

@bot.command()
async def yt(ctx):
    await ctx.send(f"**{STREAMER_NAME}'s YouTube is:** {YOUTUBE_URL}")

@bot.command()
async def instagram(ctx):
    await ctx.send(f"**{STREAMER_NAME}'s Instagram is:** {INSTAGRAM_URL}")

@bot.command()
async def ig(ctx):  # Kept for backward compatibility
    await ctx.send(f"**{STREAMER_NAME}'s Instagram is:** {INSTAGRAM_URL}")

@bot.command()
async def nick(ctx):
    await ctx.send(f"{STREAMER_NAME}'s Minecraft name is **{MINECRAFT_NAME}**")

@bot.command()
async def help(ctx):
    await ctx.send(
        f"```Help - Commands\n\n"
        f"Twitch: Link to {STREAMER_NAME}'s Twitch\n\n"
        f"Stats: Server information\n\n"
        f"YouTube/YT: Link to {STREAMER_NAME}'s YouTube\n\n"
        f"Nick: {STREAMER_NAME}'s Minecraft name\n\n"
        f"Instagram/ING: {STREAMER_NAME}'s Instagram```"
    )

bot.run(TOKEN)