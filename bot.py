import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
VERIFY_ROLE_ID = 1490754062998831164

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def verify(ctx):

    embed = discord.Embed(
        title="🔐 Verify",
        description="กดอิโมจิ ✅ เพื่อรับยศ",
        color=0x2b2d31
    )

    embed.set_image(url="https://i.pinimg.com/1200x/77/f7/38/77f738bf86188c93746c3a91c80ee32b.jpg")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")


@bot.event
async def on_raw_reaction_add(payload):

    if payload.emoji.name != "✅":
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member.bot:
        return

    role = guild.get_role(VERIFY_ROLE_ID)
    await member.add_roles(role)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)