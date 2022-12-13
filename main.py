import discord
from discord import commands
import os # default module
from dotenv import load_dotenv


load_dotenv() # load all the variables from the env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "rickroll", description = "Rickroll Someone")
async def hello(ctx):
    await ctx.respond("We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you!")

@bot.slash_command(name = 'parthiv-special', description = "find out")
async def rickrollspecial(ctx):
  await ctx.respond("Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,Thicc = Parthiv,")

bot.run(os.getenv('TOKEN')) # run the bot with the token



   


 

 


  












     