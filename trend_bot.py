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

    divider = "\n━━━━━━━━━━━━━━━━━━━━━━\n"

    hook_examples = [
        "POV: This fixed my biggest problem instantly",
        "POV: I wish I found this sooner",
        "POV: This made everything easier",
        "POV: This changed everything"
    ]

    embed = discord.Embed(
        title="🔥 WINNING PRODUCT REPORT",
        description=f"{divider}",
        color=RED
    )

    embed.add_field(
        name="📦 Product",
        value=f"{data['product']}{divider}",
        inline=False
    )

    embed.add_field(
        name="🏷️ Niche",
        value=f"{niche}{divider}",
        inline=False
    )

    embed.add_field(
        name="📊 Market Analysis",
        value=
        f"Competition: Medium\n"
        f"Saturation Score: {data['saturation']}/100\n"
        f"Market Status: Profitable Entry Window"
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="💰 Profit Analysis",
        value=
        f"Cost: ${data['cost']}\n"
        f"Sell Price: ${data['sell']}\n"
        f"Profit Per Unit: ${data['profit']}\n"
        f"Estimated Daily Sales: {data['daily']}\n"
        f"Estimated Monthly Profit: ${data['monthly']}"
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="🚚 Supplier Links",
        value=
        f"[AliExpress]({data['ali']})\n"
        f"[Alibaba]({data['alibaba']})\n"
        f"[CJ Dropshipping]({data['cj']})"
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="📨 Supplier Contact Script",
        value=
        f"Hello,\n\n"
        f"I'm interested in ordering **{data['product']}**.\n\n"
        f"Please provide:\n"
        f"• Bulk pricing\n"
        f"• Private labeling options\n"
        f"• Shipping times\n"
        f"• Branding options\n\n"
        f"I am looking for a long-term supplier partnership."
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="📈 TikTok Ad Blueprint",
        value=
        f"Hook:\n\"{random.choice(hook_examples)}\"\n\n"
        f"CTA:\n\"Get yours before it sells out\"\n\n"
        f"Execution:\nShow problem → show product → transformation\n\n"
        f"Posting:\n3–5 videos daily"
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="🏪 Store Launch Plan",
        value=
        f"Recommended Price: ${data['sell']}\n\n"
        f"Target Audience:\nBuyers actively searching for solutions in this niche\n\n"
        f"Positioning:\nPremium problem-solving product"
        f"{divider}",
        inline=False
    )

    embed.add_field(
        name="🧠 Premium Brand Name Ideas",
        value="\n".join(random.sample(BRANDS,5)),
        inline=False
    )

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

