import json

import discord
from discord.ext import commands


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="w?", intents=intents)
bot.remove_command("help")


with open("config.json",'r') as configjson:
    config = json.load(configjson)

@bot.command()
async def cops(ctx):
    channel = bot.get_channel(config["whentocopchannel"])
    with open("paires.json",'r') as pairejson:
        paire = json.load(pairejson)

    for paires in paire:
        with open("id.json",'r') as idjson:
            ids = json.load(idjson)

        if paire[paires]["id"] in ids["id"]:
            continue
        else:
            try:
                embed = discord.Embed(title=f"👟 **__{paires}__**",color=0x01ffb1,url=paire[paires]['url'])
                embed.add_field(name="``Modele``",value=paire[paires]['paire'],inline=True)
                embed.add_field(name="``Type de resell``",value=paire[paires]['resell-type'],inline=True)
                embed.add_field(name="``Prix de retail``",value=paire[paires]['retails-prix'],inline=True)
                embed.add_field(name="``Prix de resell``",value=paire[paires]['resell-prix'],inline=True)
                embed.add_field(name="``Date``",value=paire[paires]['date'],inline=True)
                lesliensachats = ""
                for i in range(len(paire[paires]['sites'])):
                    lesliensachats += f"[{paire[paires]['sites'][i]}]({paire[paires]['liens-achat'][i]})"
                    if i == len(paire[paires]['sites']):
                        pass
                    else:
                        lesliensachats += " ``|``"
                embed.add_field(name="``Où acheter ?``",value="``|`` " + lesliensachats)
                embed.set_thumbnail(url=f'https://www.whentocop.fr{paire[paires]["image"]}')
                embed.set_footer(text=f"Merci 2$py <3 | Id du modéle : {paire[paires]['id']}",icon_url=bot.user.avatar_url)
                await channel.send(embed=embed)
                with open("id.json", 'w+') as idjson:
                    ids["id"].append(paire[paires]["id"])
                    json.dump(ids,idjson,indent=4)
            except:
                pass


bot.run(config["token"])
