import discord
from discord.ext import commands
from discord.ui import View, Button
import random
import urllib.parse
import os

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("ERROR: TOKEN not found. Set it in environment variables.")
    exit()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

RED = discord.Color.from_rgb(255,0,0)

# =========================
# NICHE PRODUCT DATABASE
# =========================

NICHES = {

"👶 Baby Essentials":[
"Portable Baby Bottle Warmer",
"Baby Sleep Soother Machine",
"Baby Head Protection Pillow",
"Foldable Baby Changing Pad",
"Baby Stroller Fan"
],

"💄 Beauty & Skincare":[
"LED Face Therapy Mask",
"Electric Blackhead Remover",
"Face Ice Roller",
"Facial Cleansing Brush",
"Skin Tightening Device"
],

"🐶 Pet Accessories":[
"Pet Hair Remover Roller",
"Automatic Pet Feeder",
"Pet Water Fountain",
"Pet Nail Grinder",
"Pet Grooming Brush"
],

"📱 Tech Gadgets":[
"Magnetic Wireless Power Bank",
"Mini Bluetooth Printer",
"Phone Cooling Fan",
"Wireless Charging Stand",
"LED Smart Lights"
],

"🏠 Home & Kitchen":[
"Electric Cleaning Spin Scrubber",
"Under Sink Organizer",
"Automatic Soap Dispenser",
"Vacuum Storage Bags",
"Magnetic Screen Door"
],

"👕 Fashion & Apparel":[
"Oversized Streetwear Hoodie",
"Compression Gym Shirt",
"Cargo Streetwear Pants",
"Zip Tech Jacket"
],

"🌱 Eco Products":[
"Reusable Storage Bags",
"Bamboo Toothbrush Kit",
"Eco Cleaning Brush",
"Reusable Cleaning Sponge"
],

"💪 Fitness & Health":[
"Resistance Band Set",
"Ab Roller Trainer",
"Massage Gun Device",
"Posture Corrector"
],

"🚗 Car Accessories":[
"Car Phone Mount Holder",
"Car Interior LED Lights",
"Car Cleaning Gel",
"Wireless Car Charger"
],

"🎮 Gaming Accessories":[
"RGB Gaming Mouse Pad",
"Controller Cooling Fan",
"Gaming Headset Stand",
"Mechanical Keyboard Kit"
]

}

# =========================
# PREMIUM BRAND NAMES
# =========================

BRANDS = [
"Velmora",
"Oravelle",
"Voltique",
"Nexora",
"Aurelia",
"Novyra",
"Zentrix",
"Veltrix",
"Axiora",
"Cryonix"
]

used_products=set()

# =========================
# PRODUCT GENERATOR
# =========================

def generate_product(niche):

    available=[p for p in NICHES[niche] if p not in used_products]

    if not available:
        used_products.clear()
        available=NICHES[niche]

    product=random.choice(available)
    used_products.add(product)

    cost=round(random.uniform(5,18),2)
    sell=round(cost*random.uniform(2.5,4),2)
    profit=round(sell-cost,2)

    daily=random.randint(5,18)
    monthly=int(daily*profit*30)

    saturation=random.randint(25,60)

    encoded=urllib.parse.quote(product)

    ali=f"https://www.aliexpress.com/wholesale?SearchText={encoded}"
    alibaba=f"https://www.alibaba.com/trade/search?SearchText={encoded}"
    cj=f"https://app.cjdropshipping.com/search?keywords={encoded}"

    return {
        "product":product,
        "cost":cost,
        "sell":sell,
        "profit":profit,
        "daily":daily,
        "monthly":monthly,
        "saturation":saturation,
        "ali":ali,
        "alibaba":alibaba,
        "cj":cj
    }

# =========================
# EMBED BUILDER
# =========================

def create_embed(niche,data):

    hook_examples=[
    f"POV: This fixed my biggest problem instantly",
    f"POV: I wish I found this sooner",
    f"POV: This made everything easier",
    f"POV: This changed my daily routine"
    ]

    embed=discord.Embed(
    title="🔥 WINNING PRODUCT REPORT",
    color=RED)

    embed.add_field(
    name="Product",
    value=f"**{data['product']}**",
    inline=False)

    embed.add_field(
    name="Niche",
    value=niche,
    inline=False)

    embed.add_field(
    name="Market Analysis",
    value=f"Competition: Medium\nSaturation Score: {data['saturation']}/100\nMarket Status: Profitable Entry Window",
    inline=False)

    embed.add_field(
    name="Profit Analysis",
    value=f"Cost: ${data['cost']}\nSell Price: ${data['sell']}\nProfit Per Unit: ${data['profit']}\nEstimated Daily Sales: {data['daily']}\nEstimated Monthly Profit: ${data['monthly']}",
    inline=False)

    embed.add_field(
    name="Supplier Links",
    value=f"[AliExpress]({data['ali']})\n[Alibaba]({data['alibaba']})\n[CJ Dropshipping]({data['cj']})",
    inline=False)

    embed.add_field(
    name="Supplier Contact Script",
    value=f"Hello,\n\nI'm interested in ordering **{data['product']}**.\n\nPlease provide:\n• Bulk pricing\n• Private labeling options\n• Shipping times\n• Branding options\n\nI am looking for a long-term supplier partnership.",
    inline=False)

    embed.add_field(
    name="TikTok Ad Blueprint",
    value=f"Hook:\n\"{random.choice(hook_examples)}\"\n\nCTA:\n\"Get yours before it sells out\"\n\nExecution:\nShow problem → show product → transformation\n\nPosting:\n3–5 videos daily",
    inline=False)

    embed.add_field(
    name="Store Launch Plan",
    value=f"Recommended Price: ${data['sell']}\nTarget Audience: Buyers actively searching for solutions in this niche\nPositioning: Premium problem-solving product",
    inline=False)

    embed.add_field(
    name="Premium Brand Name Ideas",
    value="\n".join(random.sample(BRANDS,5)),
    inline=False)

    return embed

# =========================
# NEXT PRODUCT VIEW
# =========================

class ProductView(View):

    def __init__(self,niche):
        super().__init__(timeout=None)
        self.niche=niche

        button=Button(label="Next Product ➜",style=discord.ButtonStyle.danger)
        button.callback=self.next_product
        self.add_item(button)

    async def next_product(self,interaction):

        data=generate_product(self.niche)
        embed=create_embed(self.niche,data)

        await interaction.response.edit_message(embed=embed,view=self)

# =========================
# NICHE SELECT VIEW
# =========================

class NicheView(View):

    def __init__(self):
        super().__init__(timeout=None)

        for niche in NICHES:

            button=Button(label=niche,style=discord.ButtonStyle.secondary)

            async def callback(interaction,n=niche):

                data=generate_product(n)
                embed=create_embed(n,data)

                await interaction.response.send_message(
                embed=embed,
                view=ProductView(n))

            button.callback=callback
            self.add_item(button)

# =========================
# COMMAND
# =========================

@bot.command()
async def create(ctx):

    embed=discord.Embed(
    title="🔥 Choose Your Niche",
    description="Select a niche below to unlock a winning product, supplier links, and launch plan.",
    color=RED)

    await ctx.send(embed=embed,view=NicheView())

# =========================
# READY EVENT
# =========================

@bot.event
async def on_ready():
    print(f"Bot Online: {bot.user}")

bot.run(TOKEN)

