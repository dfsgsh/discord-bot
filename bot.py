import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
VERIFY_ROLE_ID = 1490754062998831164

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)   # ทำให้ปุ่มไม่หมดเวลา

    @discord.ui.button(
        label="VERIFY",
        style=discord.ButtonStyle.green,
        emoji="✅",
        custom_id="verify_button"
    )
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):

        role = interaction.guild.get_role(VERIFY_ROLE_ID)

        if role in interaction.user.roles:
            await interaction.response.send_message("คุณยืนยันตัวตนแล้ว", ephemeral=True)
            return

        await interaction.user.add_roles(role)
        await interaction.response.send_message("ยืนยันตัวตนสำเร็จ 🎉", ephemeral=True)


@bot.command()
async def verify(ctx):
    embed = discord.Embed(
        title="🔐 Verification",
        description="กดปุ่มด้านล่างเพื่อยืนยันตัวตน",
        color=0x2b2d31
    )

    await ctx.send(embed=embed, view=VerifyView())


@bot.event
async def on_ready():
    bot.add_view(VerifyView())  # ลงทะเบียนปุ่มทุกครั้งที่บอทเปิด
    print(f"Logged in as {bot.user}")


bot.run(TOKEN)
