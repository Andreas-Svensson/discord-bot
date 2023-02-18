import discord
from discord.ext import commands
from config import key

def init():
    # setting up intents and client
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix = "!", intents = intents)

    @client.event
    async def on_ready():

        # TODO: load extensions from config file
        cog_files = [
            # put extensions here
        ]

        # load extensions if any were added
        if cog_files:
            print("loading extensions...")
            for cog_file in cog_files:
                await client.load_extension(cog_file)
                print(f"{cog_file} has loaded successfully")
            print("loading finished")

        print(f"{client.user.name} is now running!")

    client.run(key)