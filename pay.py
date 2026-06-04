import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# =========================================
# LOAD ENV
# =========================================
load_dotenv()

TOKEN = os.getenv("TOKEN")

WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))
CHAT_CHANNEL_ID = int(os.getenv("CHAT_CHANNEL_ID"))
BUY_CHANNEL_ID = int(os.getenv("BUY_CHANNEL_ID"))
RULES_CHANNEL_ID = int(os.getenv("RULES_CHANNEL_ID"))

# =========================================
# GIF / IMAGE
# =========================================
WELCOME_GIF = "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3djE3NWZyZXpnemdoNnhsbWJyb3V2NWRlcWl4MmE4YXc3YTJxZXlqayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/shy030IeNMQmc/giphy.gif"

# =========================================
# BOT SETUP
# =========================================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================================
# READY EVENT
# =========================================
@bot.event
async def on_ready():
    print(f"✅ Logged In As {bot.user}")

# =========================================
# MEMBER JOIN EVENT
# =========================================
@bot.event
async def on_member_join(member):

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if not channel:
        return

    embed = discord.Embed(
        title="👑 WELCOME TO AXB COMMUNITY 👑",
        description=(
            f"👋 HEY {member.mention}\n\n"
            "✨ WELCOME TO OUR PREMIUM SERVER ✨\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"💬 • CHAT ➜ <#{CHAT_CHANNEL_ID}>\n\n"
            f"🛒 • BUY ➜ <#{BUY_CHANNEL_ID}>\n\n"
            f"📜 • RULES ➜ <#{RULES_CHANNEL_ID}>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "💎 PREMIUM PRODUCTS\n"
            "💎 TRUSTED COMMUNITY\n"
            "💎 FAST SUPPORT\n\n"
            "🔥 ENJOY YOUR STAY 🔥"
        ),
        color=0x9B59B6
    )

    embed.set_image(url=WELCOME_GIF)

    if member.guild.icon:
        embed.set_thumbnail(url=member.guild.icon.url)

    embed.set_footer(text=f"Member #{member.guild.member_count}")

    await channel.send(embed=embed)

# =========================================
# PANEL COMMAND
# =========================================
@bot.command()
async def panel(ctx):

    if ctx.channel.id != WELCOME_CHANNEL_ID:
        await ctx.send("❌ Wrong Channel")
        return

    embed = discord.Embed(
        title="👑 WELCOME TO AXB COMMUNITY 👑",
        description=(
            f"👋 HEY {ctx.author.mention}\n\n"
            "✨ WELCOME TO OUR PREMIUM SERVER ✨\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"💬 • CHAT ➜ <#{CHAT_CHANNEL_ID}>\n\n"
            f"🛒 • BUY ➜ <#{BUY_CHANNEL_ID}>\n\n"
            f"📜 • RULES ➜ <#{RULES_CHANNEL_ID}>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "💎 PREMIUM PRODUCTS\n"
            "💎 TRUSTED COMMUNITY\n"
            "💎 FAST SUPPORT\n\n"
            "🔥 ENJOY YOUR STAY 🔥"
        ),
        color=0x9B59B6
    )

    embed.set_image(url=WELCOME_GIF)

    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)

    embed.set_footer(text="AXB COMMUNITY • PREMIUM SERVER")

    await ctx.send(embed=embed)

# =========================================
# RUN BOT
# =========================================
if not TOKEN:
    print("❌ TOKEN NOT FOUND")
else:
    bot.run(TOKEN)