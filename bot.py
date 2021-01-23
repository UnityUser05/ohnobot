import discord
from discord.enums import EnumMeta
from discord.ext import commands
from discord.ext.commands.converter import InviteConverter
from discord.utils import get
#from discord.ext import tasks
#import nest_asyncio
import random
import praw
import datetime
import asyncio
from aiohttp import request
from aiohttp import ClientSession
import DiscordUtils
#from dateutil import tz

reddit = praw.Reddit(client_id = reddit client id,
                     client_secret = reddit client secret,
                     username = reddit username,
                     password = reddit password,
                     user_agent = reddit agent)
#https://www.youtube.com/watch?v=Q5u6MDQAG7I, helpful link for praw                     

#nest_asyncio.apply()


from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

intents = discord.Intents.all()


client = commands.Bot(command_prefix = '=', intents = intents)
client.launch_time = datetime.datetime.utcnow()
client.remove_command('help')



@client.group(invoke_without_command=True)
#@client.command()
async def help(ctx):
    embed = discord.Embed(
            title = 'HELP',
            description = "we have sended help ",
            color = discord.Color.green()
            )

     
    embed.add_field(name = "`fun`", value = "=helpfun \n", inline=False)
    embed.add_field(name = "`gifs`", value = "=helpgifs \n", inline=False)
    embed.add_field(name = "`miscellanous`", value = "=helpmisc \n", inline=False)
    embed.add_field(name = "`moderation`", value = "=helpmod \n", inline=False)
    embed.add_field(name = "`info`", value = "=helpinfo \n", inline=False)
    embed.add_field(name = "`reddit`", value = "=helpreddit \n", inline=False)
    embed.add_field(name = "`image`", value = "=helpimage \n", inline=False)
    embed.add_field(name = "`emojis`", value = "=helpemoji \n", inline = False)
    embed.add_field(name = "`text`", value = "=helptext \n", inline = False)
    embed.add_field(name = "`perms`", value = "=helpperms \n", inline = False)
    embed.add_field(name = "`sociux`", value = "=helpsociux \n", inline = False)
    embed.add_field(name = "`nsfw`", value = "=helpnsfw \n", inline=False)
    embed.add_field(name = "`You can now use =help (command) for more info on that command!`", value = "Note: No aliases will work for the =help (command), use the root command. \n", inline = False)
    
    embed.set_footer(text='some help for you and for you and help for EEEVVERYYYYYONEEEE')
    await ctx.send(embed=embed)

@client.command()
async def helpnsfw(ctx):
    embed = discord.Embed(
        title = ":smirk:",
        color = discord.Color.blurple()
        )
    embed.add_field(name= "`nsfw` ", value="=help nsfw", inline = False)
    embed.add_field(name = "`porngif`", value = "=help porngif", inline = False)
    embed.add_field(name = "`cumslut`", value = "=help cumslut", inline = False)
    embed.add_field(name = "`hentai`", value = "=help hentai", inline = False)
    embed.add_field(name = "`bj`", value = "=help bj", inline = False)
    embed.add_field(name = "`pussy`", value = "=help pussy", inline = False)
    embed.add_field(name = "`boobs`", value = "=help boobs", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def helpsociux(ctx):
    embed = discord.Embed(
        title = "yuinoviio viio ko yuiviyuinere",
        color = discord.Color.blurple()
        )
    embed.add_field(name= "`sociux` ", value="Shows information about Sociux", inline = False)
    embed.add_field(name = "`sociuxget / sg`", value = "Format : =sg (what you want to translate) \n turns the english language into sociux", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def helpperms(ctx):
    embed = discord.Embed(
        title = "Info bout' those perm commands yo 😎",
        color = discord.Color.blurple()
        )
    embed.add_field(name= "`roleperms` ", value="Format : =roleperms (put the id of the role) \n Returns the permissions for the role in an embed. \n WARNING : IF YOU INPUT A ROLE ID THAT DOES  NOT EXIST IN THE SERVER YOU ARE TYPING THE COMMAND IN, **IT WILL NOT WORK!** IT WILL RETURN AN ERROR MESSAGE! DO NOT REPORT THIS!", inline = False)
    embed.add_field(name = "`perms`", value = "Format : =perms (user) \n  Returns the **permissions** for the user **in the current channel** of the message being sent", inline = False)
    embed.add_field(name = "`roleid`", value = "Format : =roleid (mention a role here) \n  Returns the id of the mentioned role which can be used in =roleperms", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def helptext(ctx):
    embed = discord.Embed(
        title = "text memes ",
        color = discord.Color.blurple()
        )
    embed.add_field(name= "`give` ", value="Gave (person) (item)\n", inline = False)
    embed.add_field(name = "`kill`", value = "rip \n", inline = False)
    embed.add_field(name = "`tp`", value = "teleported (thing) to (thing2) \n", inline = False)
    embed.add_field(name = "`repair`", value = "repair (thing) \n", inline = False)
    await ctx.send(embed = embed)


@client.command()
async def helpemoji(ctx):
    embed = discord.Embed(
        title = "fReE nItRo iN eMoJi FoRm",
        color = discord.Color.gold()
        )
    embed.add_field(name= "`think` ", value="***thinkitythinkthink***\n", inline = False)
    embed.add_field(name = "`simp`", value = "simp alert \n", inline = False)
    embed.add_field(name = "`thonk`", value = "its an original, its og \n", inline = False)
    embed.add_field(name='`ohno`      ',value=":0 \n", inline = False)
    await ctx.send(embed = embed)


@client.command()
async def helpfun(ctx):
    embed = discord.Embed(
        title = "Fun Commands List",
        color = discord.Color.gold()
        )
    embed.add_field(name= "`c` ", value="format : =c (message) \n Chat, basically, the bot responds to your message. The responses will get better over time. \n", inline = False)
    embed.add_field(name= "`ship` ", value="format : =ship @person1 @person2 \n very self-explanatory what this does... :wink: \n", inline = False)
    embed.add_field(name = "`breakup`", value = "Format : =braeakup @personyouwanttobreakupwith \n sends an embed saying that someone broke up \n", inline = False)
    embed.add_field(name = "`love`", value = "Format : =love @personyoulove \n sends an embed saying you love someone \n", inline = False)
    embed.add_field(name='`8ball`      ',value="Format : **=8ball (question)** \n", inline = False)
    embed.add_field(name='`nsfwq`      ',value="asks a nsfw question \n", inline = False)
    embed.add_field(name='`scr`      ',value="sends a screenshot of the top part of a URL, use *`=help scr`* for more info \n", inline = False)
    embed.add_field(name='`showerthought`      ',value="sends a random shower thought \n", inline = False)
    embed.add_field(name='`yn`      ',value="Format : **=yn (question)** \n answers with yes or no to a question", inline = False)
    embed.add_field(name='`(fox,dog,cat,bird,panda,koala)fact`      ',value="Format : **=foxfact** or **=dogfact** \n facts about animals owo", inline = False)
    embed.add_field(name='`statussearch`      ',value="searches for values in people's status's \n Make sure your search does not have any capital letters(even if anyones stats has capital letters, it will still find it)", inline = False)
    #embed.add_field(name='`astate`      ',value="Format: =astate (then a statement) \n Eg: =astate hello my name is stupid \n makes an anonymous confession or statement.\n", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def helpimage(ctx):
    embed = discord.Embed(
        title = "Image Commands List",
        description = "Most Image Commands have the format =(command) (person/mention)",
        color = discord.Color.blurple()
        )
    embed.add_field(name = "`waitwhat`", value = "say what now \n This one is an exception, there is no need to mention someone after the command \n", inline = False)
    embed.add_field(name = "`no`", value = "no -_- \n This one is an exception, there is no need to mention someone after the command \n", inline = False)
    embed.add_field(name = "`wanted`", value = "oMg I wAnT a MiLliOn dOlLaRs \n", inline = False)
    embed.add_field(name = "`imp`", value = "red lookin' kinda sus ngl.. :eyes: \n", inline = False)
    embed.add_field(name = "`headache`", value = "stres, migraine, hypertension and here we go praise the master of pain \n", inline = False)
    embed.add_field(name = "`google`", value = "just searching something on google \n", inline = False)
    embed.add_field(name = "`wasted`", value = "=wasted (user) \n", inline = False)
    embed.add_field(name = "`triggered`", value = "***WEEWOOWEEWOO*** \n", inline = False)
    embed.add_field(name = "`glass`", value = "=glass (user) \n", inline = False)
    embed.set_footer(text="Page 1 of 2 | Use =helpimage2")
    await ctx.send(embed = embed)

@client.command()
async def helpimage2(ctx):
    embed = discord.Embed(
        title = "Image Commands List Part 2",
        #description = "Most Image Commands have the format =(command) (person/mention)",
        color = discord.Color.blurple()
        )
    embed.add_field(name = "`pixelate`", value = "pixelates a users avatar \n", inline = False)
    embed.add_field(name = "`google11`", value = "=help google11 \n", inline = False)
    embed.add_field(name = "`invert`", value = "inverts the colors in a users avatar(howmanytimesdoihavetowritethis) \n", inline = False)
    embed.add_field(name = "`gradient`", value = "=help g \n", inline = False)
    #embed.add_field(name = "`invertpic`", value = "=help ip \n", inline = False)
    embed.set_footer(text="Page 2 of 2 | Use =helpimage")
    await ctx.send(embed = embed)

@client.command()
async def helpgifs(ctx):
    embed = discord.Embed(
        title = "ALL THE GIFSSSSS",
        color = discord.Color.blurple()
        )
    
    embed.add_field(name = '`kiss`', value = 'Format: =kiss @person \n kisses person \n', inline = False)
    embed.add_field(name = '`hug`', value = 'Format: =hug @person \n hugs person \n ', inline = False)
    embed.add_field(name = "`lolgif`", value = "lol \n", inline = False)
    embed.add_field(name = "`bruh`", value = "for bruh moments \n", inline = False)
    embed.add_field(name = "`nice`", value = "*click* **noice** \n", inline = False)
    embed.add_field(name = "`sweat`", value = ":eyes: \n", inline = False)
    
    await ctx.send(embed = embed)
    
@client.command()
async def helpmisc(ctx):
    embed = discord.Embed(
        title = "random miscellanous commands lol",
        color = discord.Color.blurple()
        )

    embed.add_field(name = '`serverinvite`', value = 'creates an invite for current sever \n', inline = False)
    embed.add_field(name = '`supportinvite`', value = 'sends an invite for the ohnobot support server \n', inline = False)
    embed.add_field(name = '`invite`', value = 'sends a link which can be used to invite ohnobot to other servers \n', inline = False)
    embed.add_field(name = "`membed`", value = "asks for title, description, field title and field description \n then makes an embed out of it \n", inline = False)
    embed.add_field(name = "`randomcolor`", value = "sends a random color -_-", inline = False)
    embed.add_field(name = "`textlang`", value = "sends a random text language shortcut", inline = False)
    embed.add_field(name = "`math`", value = "=help math", inline = False)
    embed.set_footer(text ="Page 1 of 2, do =helpmisc2")
    await ctx.send(embed = embed)
    
@client.command()
async def helpmisc2(ctx):
    embed = discord.Embed(
        title = "random miscellanous commands lol",
        color = discord.Color.blurple()
        )

    embed.add_field(name = "`timers`", value = "Format : =timers (eg:10) \n sets timer for amount of seconds mentioned", inline = False)
    embed.add_field(name = "`timerm`", value = "Format : =timers (eg:10) \n sets timer for amount of minutes mentioned", inline = False)
    embed.add_field(name = "`timerh`", value = "Format : =timers (eg:10) \n sets timer for amount of hours mentioned", inline = False)
    embed.add_field(name = "`servers`", value = "Returns how many servers the is currently in", inline = False)
    embed.add_field(name='`ping`      ',value="Returns the bot's latency \n", inline = False)
    embed.add_field(name = '`roleperms`', value = 'Format : =roleperms (role id) \n Sends all permissions that role has in an embed. \n', inline = False)
    embed.set_footer(text = "Page 2 of 2")
    await ctx.send(embed = embed)
    
@client.command()
async def helpmod(ctx):
    embed = discord.Embed(
        title = "Moderashun commanddz",
        color = discord.Color.blurple()
        )

    embed.add_field(name = '`clear`', value = 'clears value of messages [eg =clear 2] \n \n Requires `Manage Messages` \n', inline = False)
    embed.add_field(name = '`poll`', value = 'Starts a poll......pretty obvious` \n', inline = False)
    embed.add_field(name = '`mark_nsfw`', value = '=help mark_nsfw \n \n Requires `Manage Channels` \n', inline = False)
    embed.add_field(name = '`gstart`', value = 'Format : =gstart {time in mins for the giveaway to end} {prize( dont mention roles, also no spaces)} \n Starts a giveaway... \n Requires `Manage Server`', inline = False)
    await ctx.send(embed = embed)

@client.command()
async def helpinfo(ctx):
    embed = discord.Embed(
        title = "INFO COMMANDS",
        color = discord.Color.blurple()
        )
    embed.add_field(name = '`info`', value = 'gets info about the bot \n', inline = False)
    embed.add_field(name = '`minfo`', value = 'gets info about a member \n Format: =minfo @person \n', inline = False)
    embed.add_field(name = '`sinfo`', value = 'gets info about this server \n', inline = False)
    embed.add_field(name = '`msginfo`', value = '=help msginfo \n', inline = False)
    embed.add_field(name = '`av`', value = 'gets a users avatar \n', inline = False)
    await ctx.send(embed = embed)
    
@client.command()
async def helpreddit(ctx):
    embed = discord.Embed(
        title = "REDDIT COMMANDS",
        color = discord.Color.blurple()
        )

    embed.add_field(name = '`meme`', value = 'sends a meme \n', inline = False)
    embed.add_field(name = '`customreddit`', value = '=help customreddit \n', inline = False)
    ##
    await ctx.send(embed = embed)      





@client.event
async def on_guild_join(ctx):
    em = discord.Embed(
        title = "I was added to a new server!!!!!!!!!!! :partying_face:",
        description = "Server name: " + ctx.name,
        color = discord.Color.blue()
        )
    em.add_field(name = "I am now in", value = f"{len(client.guilds)} servers.", inline = False)
    
    chan = client.get_channel(790548341037072416)
    
    
    em.set_image(url=ctx.icon_url)

    await chan.send(embed=em)

@client.event
async def on_guild_remove(ctx):
    em = discord.Embed(
        title = "I was removed from a server.... :cry:",
        description = "Server name: " + ctx.name,
        color = discord.Color.blue()
        )
    em.add_field(name = "I am now in", value = f"{len(client.guilds)} servers.", inline = False)
    
    chan = client.get_channel(790548341037072416)
    
    
    em.set_image(url=ctx.icon_url)

    await chan.send(embed=em)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title = ":x: You can't do that! :x:",
            description = "You're missing the required permissions.",
            color = discord.Color.red()
            )
        await ctx.send (embed = embed)
        
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title = ":x: INVALID! :x:",
            description = "Please fill all required arguments. Turn to =help for more info on commands.",
            color = discord.Color.red()
            )
        await ctx.send (embed = embed)
        
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title = ":x: INVALID! :x:",
            color = discord.Color.red(),
            description = "Command not found."
            )
        await ctx.send (embed = embed)

    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            title = ":(",
            description = "There was an error in the code.",
            color = discord.Color.red()
            )
        await ctx.send (embed = embed)
        raise error
    else:
        raise error

@client.event
async def on_ready():
    print ('Bot is Ready. Beep Boop')
    await client.change_presence(status=discord.Status.online, activity = discord.Game(' =help || =info'))
  

@client.command(aliases = ["m"])
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    allsubs = []
    top = subreddit.top(limit = 100)
    
    for submission in top:
        allsubs.append(submission)
        
    randomsub = random.choice(allsubs)
    
    name = randomsub.title
    lol = randomsub.url
    
    em = discord.Embed(
        title = name,
        color = discord.Color.blurple()
        )
    em.set_image(url = lol)
    
    await ctx.send(embed = em)

@help.command()
async def meme(ctx):
    em = discord.Embed(
        title =  "Meme",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =meme", value = "Sends a random meme from r/memes", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =m")
    await ctx.send(embed=em)

@help.command()
async def m(ctx):
    em = discord.Embed(
        title =  "Meme",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =meme", value = "Sends a random meme from r/memes", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =m")
    await ctx.send(embed=em)

@client.command()
async def poll(ctx, *, topoll):
    em = discord.Embed(
        title = str(topoll),
        description = "Requested by " + ctx.author.name,
        color = ctx.author.color
    )
    #em.set_author(name=ctx.author.name, icon=None, icon_url=ctx.author.avatar_url)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    msg = await ctx.channel.send(embed=em)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

@help.command()
async def poll(ctx):
    em = discord.Embed(
        title =  "Poll",
        #description = "Category : Moderation, =helpmod",
        color = ctx.author.color
    )

    em.add_field(name="Format : =poll {What you want to poll}", value = "Creates a poll", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command(aliases = ["n"])
async def nsfw(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("nsfw")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        em.set_image(url = lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        await ctx.send(embed = em)
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@client.command(aliases = ["pg","pgif"])
async def porngif(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("porngifs")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def porngif(ctx):
    em = discord.Embed(
        title =  "porngif",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =porngif", value = "Sends a *trending* porn gif \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =pg, =pgif")
    await ctx.send(embed=em)     


@help.command()
async def pg(ctx):
    em = discord.Embed(
        title =  "porngif",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =porngif", value = "Sends a *trending* porn gif \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =pg, =pgif")
    await ctx.send(embed=em) 


@help.command()
async def pgif(ctx):
    em = discord.Embed(
        title =  "porngif",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =porngif", value = "Sends a *trending* porn gif \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =pg, =pgif")
    await ctx.send(embed=em) 

@client.command(aliases = ["cs","cum"])
async def cumslut(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("cumsluts")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def cumslut(ctx):
    em = discord.Embed(
        title =  "cumslut",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =cumsluts", value = "Sends a *trending* cumslut pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =cum, =cs")
    await ctx.send(embed=em)  

@help.command()
async def cum(ctx):
    em = discord.Embed(
        title =  "cumslut",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =cumsluts", value = "Sends a *trending* cumslut pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =cum, =cs")
    await ctx.send(embed=em) 

@help.command()
async def cs(ctx):
    em = discord.Embed(
        title =  "cumslut",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =cumsluts", value = "Sends a *trending* cumslut pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =cum, =cs")
    await ctx.send(embed=em)   

@client.command()
async def hentai(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("hentai")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def hentai(ctx):
    em = discord.Embed(
        title =  "hentai",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =hentai", value = "Sends a *trending* hentai pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def bj(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("blowjobs")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def bj(ctx):
    em = discord.Embed(
        title =  "bj",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =bj", value = "Sends a *trending* bj pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def pussy(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("pussy")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def pussy(ctx):
    em = discord.Embed(
        title =  "pussy",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =pussy", value = "Sends a *trending* pussy pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def boobs(ctx):
    
    
    await ctx.send ("lol")
    #await ctx.channel.purge(limit=2)
    
    if ctx.channel.is_nsfw():
        subreddit = reddit.subreddit("boobies")
        allsubs = []
        top = subreddit.hot(limit = 100)
        
        for submission in top:
            allsubs.append(submission)
            
        randomsub = random.choice(allsubs)
    
    
        name = randomsub.title
        lol = randomsub.url
        
        em = discord.Embed(
            title = name,
            color = discord.Color.blurple()
            )
        await ctx.send(embed = em)
        await ctx.send(lol)
        
        
        #em.set_footer(text = "Created at" + (str(timelol)) + " in Unix Time.")
        
        
        

    else:
        em = discord.Embed(
            title = " :x: This is not an NSFW channel :x:",
            description = "bruh moment",
            color = discord.Color.red())
        em.add_field(name = "You cant use this command in non-nsfw channels.", value = "-_-", inline = False)
        
        await ctx.send(embed = em)

@help.command()
async def boobs(ctx):
    em = discord.Embed(
        title =  "boobs",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =boobs", value = "Sends a *trending* boobs pic \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command(aliases = ["cr"])
async def customreddit(ctx, red : str):
    subreddit = reddit.subreddit(red)
    allsubs = []
    top = subreddit.hot(limit=100)

    for submission in top:
        allsubs.append(submission)

    randomsub = random.choice(allsubs)

    name = randomsub.title
    lol = randomsub.url

    em2 = discord.Embed(
        title = name,
        color = discord.Color.blurple()
    )
    em2.set_image(url=lol)

    if randomsub.over_18:
        if ctx.channel.is_nsfw() == False:
            em = discord.Embed(
                title = " :x: The submission found was marked NSFW :x:",
                description = "bruh moment",
                color = discord.Color.red())
            em.add_field(name = "You cant use this view this post in non-nsfw channels.", value = "-_-", inline = False)

            await ctx.send(embed=em)
        if ctx.channel.is_nsfw():

            await ctx.send(embed=em2)


    else:
        await ctx.send(embed=em2)

@help.command()
async def customreddit(ctx):
    em = discord.Embed(
        title =  "CustomReddit",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =customreddir {subreddit name}", value = "Sends a random *top* post from the mentioned subreddit \n **WARNING : THE SUBREDDIT MUST NOT INCLUDE R/ ONLY TYPE THE NAME OF THE SUBREDDIT!**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =cr")
    await ctx.send(embed=em)

@help.command()
async def cr(ctx):
    em = discord.Embed(
        title =  "CustomReddit",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =customreddir {subreddit name}", value = "Sends a random *top* post from the mentioned subreddit \n **WARNING : THE SUBREDDIT MUST NOT INCLUDE R/ ONLY TYPE THE NAME OF THE SUBREDDIT!**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =cr")
    await ctx.send(embed=em)

@help.command()
async def nsfw(ctx):
    em = discord.Embed(
        title =  "Nsfw",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =nsfw", value = "Sends a *trending* post from r/nsfw \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =n")
    await ctx.send(embed=em)       
        

@help.command()
async def n(ctx):
    em = discord.Embed(
        title =  "Nsfw",
        #description = "Category : Reddit, =helpreddit",
        color = ctx.author.color
    )

    em.add_field(name="Format : =nsfw", value = "Sends a *trending* post from r/nsfw \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =n")
    await ctx.send(embed=em)  

@client.command(aliases = ["purge", "p"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@help.command()
async def clear(ctx):
    em = discord.Embed(
        title =  "Clear",
        #description = "Category : Moderation, =helpmod",
        color = ctx.author.color
    )

    em.add_field(name="Format : =clear {amount of messages you want to clear}", value = "Clears an amount of specified messages. Requires `Manage Messages`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =p, =purge")
    await ctx.send(embed=em)   
    
@help.command()
async def p(ctx):
    em = discord.Embed(
        title =  "Clear",
        #description = "Category : Moderation, =helpmod",
        color = ctx.author.color
    )

    em.add_field(name="Format : =clear {amount of messages you want to clear}", value = "Clears an amount of specified messages. Requires `Manage Messages`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =p, =purge")
    await ctx.send(embed=em)   

@help.command()
async def purge(ctx):
    em = discord.Embed(
        title =  "Clear",
        #description = "Category : Moderation, =helpmod",
        color = ctx.author.color
    )

    em.add_field(name="Format : =clear {amount of messages you want to clear}", value = "Clears an amount of specified messages. Requires `Manage Messages`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =p, =purge")
    await ctx.send(embed=em)   

@client.command()
async def ship(ctx, member: discord.Member, member2: discord.Member):
    randomnumber = random.randint(0, 100)

    if randomnumber == 0:
        embed = discord.Embed(
            title = ':broken_heart: Welp! :broken_heart:',
            description = member.mention + " and " + member2.mention  + " are",
            color = discord.Color.red()
            )
        embed.add_field(name=("ENEMIES"), value="with only " + str(randomnumber) + "% love...", inline = False)
        embed.set_footer(text='*fightfightfightfightfight*')
        await ctx.send(embed=embed)
    
    
    if randomnumber < 50:
        if randomnumber > 0:
            embed2 = discord.Embed(
                title = ':broken_heart: Welp! :broken_heart:',
                description = member.mention + " and " + member2.mention  + " are",
                color = discord.Color.blue()
                )
            embed2.add_field(name=("Not compatible with each other :cry:"), value="with only " + str(randomnumber) + "% love...", inline = False)
            embed2.set_footer(text='*sad sadness sounds*')
            await ctx.send(embed=embed2)
    
    if randomnumber > 50:
        if randomnumber < 90:
            embed3 = discord.Embed(  
                title = ':point_right: Whoa! :point_left:',
                description = member.mention + " and " + member2.mention  + " are",
                color = discord.Color.dark_blue()
                )
            embed3.add_field(name=("'Friends' only for now"), value="with " + str(randomnumber) + "% love...", inline = False)
            embed3.set_footer(text='*progressive much?*')
            await ctx.send(embed=embed3)
    
    if randomnumber > 90:
        if randomnumber < 100:
            embed4 = discord.Embed(
                title = ':heart: LOVERS!!! :heart:',
                description = member.mention + " and " + member2.mention  + " are",
                color = discord.Color.green()
                )
            embed4.add_field(name=("'LOVERS! *what a match*"), value="with " + str(randomnumber) + "% love...", inline = False)
            embed4.set_footer(text='*bleep*')
            await ctx.send(embed=embed4)
    
    if randomnumber == 100:
        embed5 = discord.Embed(
                title = ':heart: :heartpulse: SOULMATES :heart: :heartpulse:',
                description = member.mention + " and " + member2.mention  + " are",
                color = discord.Color.red()
                )
        embed5.add_field(name=("SOULMATES! *so much love*"), value="with " + str(randomnumber) + "% love... ", inline = False)
        embed5.set_footer(text='i wonder what happened that night :wink:')
        await ctx.send(embed=embed5)

@help.command()
async def ship(ctx):
    em = discord.Embed(
        title =  "Ship",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =ship {mention person 1} {mention person 2}", value = "Ships two people based on a random value and sends their *love status*", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)


@client.command()
async def ping(ctx):
    #await ctx.send(f"Pong! :ping_pong: {round(client.latency * 1000)} ms")
    
    embed = discord.Embed(
        title = "PONG!",
        color = ctx.author.color
        )
    embed.add_field(value = f"{round(client.latency * 1000)} ms", name = ":ping_pong:")
    await ctx.send(embed=embed)


@help.command()
async def ping(ctx):
    em = discord.Embed(
        title =  "Ping",
        #description = "Category : None, None",
        color = ctx.author.color
    )

    em.add_field(name="Format : =ping", value = "Returns the latency of the bot in milliseconds", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command(aliases = ["st"])
async def showerthought(ctx):
    responses = ["If aliens came to earth and said hello we wouldn't be shocked. We would be too busy debating whether they're real, fake news or manufactured by the government..",
                "Awkward kids find adults easier to interact with because adults are more polite and tolerant as opposed to other kids..",
                "In school we are taught and trained to get a lesson first and a test later. But in life things happen the opposite way, where we are tested first and we learn the lesson afterwards..",
                "There must be a lot of accounts out there with dead owners.",
                "Antarctica problably has the highest average IQ in the world.",
                "Toasting one slice of bread uses just as much electricity as toasting two slices.",
                "What? is probably the most asked question, but also the least anwsered question.",
                "A **football field** is a unit of area measurement in the imperial system at this point.",
                "Life is a video game where your character’s life bar reduces when he or she is levelling up.",
                "The nicer the sidewalks in a neighborhood, the greater number of people you see running in the damn road.",
                "When we are upset we stay up late night even though sleep is the only escape.",
                "Gloves are boring puppets.",
                "Buzz Light Year behaves like a toy in front of humans before he realises hes an actual toy.",
                "The queen is older than Saudi Arabia.",
                "One of the most satisfying things in life is peeing after holding it for a while.",
                "The stem of an apple is its umbilical cord.",
                "Most of these thoughts didn't pop up in the shower.",
                "The larger the download button, the less safe it seems.",
                "Movie posters are portrait, but movies are landscape.",
                "One person’s nightmare might be a perfectly pleasant dream to someone else.",
                "There must be beautiful 4D patterns that we can’t see.",
                "If you put chlorine into your mouth will it kill the germs?",
                "There could be a universe in parallel universes in which there are no parallel universes.",
                "If Jeff Bezos lost 99% of his net worth, he'd still be a billionaire.",
                "Things are less scary the smaller they get, until they're so small they become scary again.",
                "Noone has ever been inside an empty room.",
                "Claustrophobic people are fine with their brain being trapped in their skull.",
                "You've never seen your own face, only in pictures and reflections.",
                "Every day that you randomly see an ambulance, is a day that someone else will never forget.",
                "Babysitters are teenagers who behave like adults so that adults can go out and  behave like teenagers.",
                "If we removed all laws, the crime rate would be 0%.",
                "Winter would be horrifying if snow was black.",
                "If two mind-readers read each other's mind, whose mind are they reading?",
                "If the camera lens is circular, how come the picture is rectangular?",
                "If a person is born deaf, what language do they use to think in their head?",
                "Why would Cinderella's slipper fall off if it fit her perfectly?",
                "Since Adam and Eve were never kids, they were probably horrified when their kid's teeth started falling out for no reason.",
                "Nothing is on fire. \n Fire is on things",
                "If you drop soap on the floor, is the floor clean or is the soap dirty?",
                "If we were eyeless, we would be unaware of color. \n What if we're missing some part of reality, \n because we don't have the organ to sense it?",
                "Crispy is just crunchy but thin.",
                "If drink gas you are car",
                "Why is there a thing called grapefruit if there's a fruit called grape?",
                "A circle is a shape, letter and a number."
                "If you rip a hole in a net, there are actually fewer holes in it than before."
                ]
    
    #await ctx.send(f'{random.choice(responses)}')    
    #st = random.choice(responses)
    
    embed = discord.Embed(
        title = "Shower Thoughts",
        description = "taken from r/showerthoughts",
        color = discord.Color.blurple()
        )
    embed.add_field(name = f'{random.choice(responses)}', value = " yes ", inline = False)
    
    await ctx.send(embed=embed)

@help.command()
async def showerthought(ctx):
    em = discord.Embed(
        title =  "Shower Thought",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =showerthought", value = "Sends a random shower thought from a list of a few of them.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =st")
    await ctx.send(embed=em)

@help.command()
async def st(ctx):
    em = discord.Embed(
        title =  "Shower Thought",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =showerthought", value = "Sends a random shower thought from a list of a few of them.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =st")
    await ctx.send(embed=em)

@client.command()
async def breakup(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author
    
    sender = ctx.author
    
    embed = discord.Embed(
        title = "OH NO!",
        description = user.mention + "We have bad news for you...",
        color = discord.Color.red()
        )
    embed.add_field(name = ":broken_heart:", value = (sender.mention + " broke up with " + user.mention), inline = False)
    embed.set_footer(text = '*sad sadness sounds*')
    await ctx.send(embed=embed)

@help.command()
async def breakup(ctx):
    em = discord.Embed(
        title =  "Breakup",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =breakup {user you want to break up with}", value = "Sends an embed saying you broke up with a person.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def love(ctx, user : discord.Member = None):
    
    sender = ctx.author
    
    
    if user == None:
        user = ctx.author
    
    embed = discord.Embed(
        title = "CELEBRATION!",
        description = user.mention + "We have AWESOME news for you...",
        color = discord.Color.red()
        )
    embed.add_field(name = ":heart:", value = (sender.mention + " NOW LIKES " + user.mention), inline = False)
    embed.set_footer(text = ":D")
    await ctx.send(embed=embed)

@help.command()
async def love(ctx):
    em = discord.Embed(
        title =  "",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =love {user you love}", value = "Sends an embed saying you like someone.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def nsfwq(ctx):
    if ctx.channel.is_nsfw():
        
        qs = ["If you got to have a threesome with 2 other people, who would you do it with?",
                  "Who do you most want to sleep with, out of everyone here?",
                  "What’s your favorite fantasy to pleasure yourself to?",
                  "Who was your best partner and why?",
                  "When was the first time you came?",
                  "What is your favorite 'special' toy?",
                  "Have you ever cheated?",
                  "Have you ever wanted to cheat?",
                  "What’s in your web history that would be embarrassing if someone saw?",
                  "Who in this server would you most like to see naked?",
                  "Have you ever been walked in on while watching porn?",
                  "What's the first thing you would do if you woke up one day as the opposite sex?",
                  "What is your guilty pleasure?",
                  "Have you ever masturbated?",
                  "Do you sing in the shower?",
                  "Do you think you'll marry your current girlfriend/boyfriend?",
                  "What is the most illegal thing you have ever done?",
                  ]
            
        embed2 = discord.Embed(
                title = "Your question is......",
                color = discord.Color.blurple()
                )
        
        embed2.add_field(name = f'{random.choice(qs)}', value = " ANSWER ")
            
        await ctx.send(embed = embed2)
        
    else:
        embed = discord.Embed(
                title = "This Channel Is Not NSFW. \n Go find an NSFW channel and retype the command.",
                color = discord.Color.blurple()
                )
        await ctx.send(embed = embed)

@help.command()
async def nsfwq(ctx):
    em = discord.Embed(
        title =  "nsfwq",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =nsfwq", value = "Asks a NSFW Question \n Must be used in an `NSFW Channel`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)    
    
@client.command(aliases=['8ball','eightball','8b'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good."]
    
    await ctx.send('Question = ' + question + f'\n Answer:{random.choice(responses)}')

@help.command()
async def _8ball(ctx):
    em = discord.Embed(
        title =  "8ball",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =8ball {Any question that can be answered with yes or no}", value = "Answers a question with regular 8ball answers", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =8b, =8ball, =eightball")
    await ctx.send(embed=em)         

 
   
@client.command()
async def serverinvite(ctx):
    """Create instant invite"""
    link = await ctx.channel.create_invite()
    await ctx.send("Here is an instant invite to your server: \n " + str(link))

@help.command()
async def serverinvite(ctx):
    em = discord.Embed(
        title =  "",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =serverinvite", value = "Sends an invite link for the current server", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command(aliases=["mi","memberinfo"])
async def minfo(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author

    createdat = user.joined_at.strftime("%b %d, %Y")
    nickname = user.nick
    namelol = user.name
    toprole = user.top_role
    pfp = user.avatar_url
    disc = user.discriminator
    stat = user.raw_status
    mob = user.is_on_mobile()
    botness = user.bot
    statuss = user.activity
    
    embed = discord.Embed(
        title = "Info About : ",
        description = user.mention,
        color = discord.Color.blue()
        )
    
    embed.set_image(url=pfp)
    
    embed.add_field(name = "Join Date:", value = str(createdat), inline = False)
    embed.add_field(name = "Discriminator/Tag:", value = str(disc), inline = False)
    embed.add_field(name = "Is on Mobile:", value = str(mob), inline = False)
    embed.add_field(name = "Nickname on this server:", value = str(nickname), inline = False)
    embed.add_field(name = "Original name:", value = str(namelol), inline = False)
    if stat == "online":
        embed.add_field(name = "Current Status:", value = "Online 🟢", inline = False)
    elif stat == "idle":
        embed.add_field(name = "Current Status:", value = "Idle 🟡", inline = False)
    elif stat == "dnd":
        embed.add_field(name = "Current Status:", value = "DND / Do Not Disturb 🔴", inline = False)
    else:
        embed.add_field(name = "Current Status:", value = "Offline ⚫", inline = False)
    embed.add_field(name = "Highest role user has on this server:", value = toprole.mention, inline = False)
    embed.add_field(name = "Roles:", value = f"{len(user.roles)}", inline = False)
    embed.add_field(name = "User ID:", value = str(user.id), inline = False)
    embed.add_field(name = "Is a bot?", value = str(botness), inline = False)
    embed.add_field(name = "Status:", value = str(statuss), inline = False)
    await ctx.send(embed = embed)




@help.command()
async def minfo(ctx):
    em = discord.Embed(
        title =  "minfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =minfo {user you want to get information about}", value = "Sends information about the mentioned user in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =mi, =memberinfo")
    await ctx.send(embed=em)  

@help.command()
async def mi(ctx):
    em = discord.Embed(
        title =  "minfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =minfo {user you want to get information about}", value = "Sends information about the mentioned user in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =mi, =memberinfo")
    await ctx.send(embed=em)  

@help.command()
async def memberinfo(ctx):
    em = discord.Embed(
        title =  "minfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =minfo {user you want to get information about}", value = "Sends information about the mentioned user in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =mi, =memberinfo")
    await ctx.send(embed=em)  

@client.command(aliases=["si","serverinfo"])
async def sinfo(ctx):

    region = ctx.guild.region
    pfp = ctx.guild.icon_url
    created_atlol = ctx.guild.created_at.strftime("%b %d, %Y")
    embed = discord.Embed(
        title = "Info About : ",
        description = f"{ctx.guild.name}",
        color = discord.Color.green()
        )
    
    embed.set_image(url=pfp)
    embed.add_field(name = "Region of server:", value = str(region), inline = False)
    embed.add_field(name = "Creation Date:", value = str(created_atlol), inline = False)
    embed.add_field(name = "Total Channels:", value = f"{len(ctx.guild.channels)}", inline = False)
    embed.add_field(name = "Channels:", value = f"{len(ctx.guild.text_channels)}", inline = False)
    embed.add_field(name = "Voice Channels:", value = f"{len(ctx.guild.voice_channels)}", inline = False)
    embed.add_field(name = "Roles:", value = f"{len(ctx.guild.roles)}", inline = False)
    embed.add_field(name = "Member Count:", value = f"{ctx.guild.member_count}", inline = False)
    embed.add_field(name = "ID:", value = f"{ctx.guild.id}", inline = False)
    await ctx.send(embed = embed)   

@help.command()
async def sinfo(ctx):
    em = discord.Embed(
        title =  "sinfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sinfo", value = "Gets information about the current server and sends it in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =si, =serverinfo")
    await ctx.send(embed=em)  

@help.command()
async def si(ctx):
    em = discord.Embed(
        title =  "sinfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sinfo", value = "Gets information about the current server and sends it in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =si, =serverinfo")
    await ctx.send(embed=em)  

@help.command()
async def serverinfo(ctx):
    em = discord.Embed(
        title =  "sinfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sinfo", value = "Gets information about the current server and sends it in an embed.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =si, =serverinfo")
    await ctx.send(embed=em)  

@client.command()
async def supportinvite(ctx):
    sender = ctx.author
    invite = "https://discord.com/invite/YYtB7ema8A"
    embed = discord.Embed(
        title = "Invite for support server",
        description = (sender.mention + " Here you go!"),
        color = discord.Color.green()
        )
    
    
    embed.add_field(name = "Link:", value = invite  , inline = False)
    

    await ctx.send(embed = embed)

@help.command()
async def supportinvite(ctx):
    em = discord.Embed(
        title =  "supportinvite",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =supportinvite", value = "Sends an invite to the ohnobot support server.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=787679386227703820&permissions=8&scope=bot")

@help.command()
async def invite(ctx):
    em = discord.Embed(
        title =  "invite",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =invite", value = "Sends a link which can be used to invite ohnobot to other servers.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)      
 
@client.command()
async def kiss(ctx, user : discord.Member = None):
    
    
    sender = ctx.author
    
    if user == None:
        user = ctx.author
    
    embed = discord.Embed(
        description = (sender.mention + " kisses " + user.mention ),
        color = discord.Color.red()
        )
    
    gifs = ["https://i.imgur.com/i1PIph3.gif",
            "https://i.imgur.com/WVSwvm6.gif",
            "https://i.imgur.com/sZhtvBR.gif",
            "https://i.imgur.com/So3TIVK.gif",
            "https://i.imgur.com/q340AoA.gif",
            "https://i.imgur.com/OjTBV8G.gif",
            "https://i.imgur.com/SeCRpPp.gif",
            "https://i.imgur.com/LRPJt19.gif"]
     
    rgifs = random.choice(gifs)
    
    embed.set_image(url=rgifs)
    
    await ctx.send(embed=embed)

@help.command()
async def kiss(ctx):
    em = discord.Embed(
        title =  "kiss",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =kiss {user you want to kiss}", value = "Sends an embed that shows an anime kiss gif", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  
    
@client.command()
async def hug(ctx, user : discord.Member = None):
    sender = ctx.author
    
    if user == None:
        user = ctx.author
    
    embed = discord.Embed(
        description = (sender.mention + " hugs " + user.mention ),
        color = discord.Color.red()
        )
    
    gifs = ["https://i.imgur.com/r9aU2xv.gif",
            "https://i.imgur.com/BPLqSJC.gif",
            "https://i.imgur.com/v47M1S4.gif",
            "https://i.imgur.com/4oLIrwj.gif",
            "https://i.imgur.com/XEs1SWQ.gif",
            "https://i.imgur.com/VgP2ONn.gif",
            "https://i.imgur.com/iKPs2AJ.gif",
            "https://i.imgur.com/KFZNUZl.gif"]
     
    rgifs = random.choice(gifs)
    
    embed.set_image(url=rgifs)
    
    await ctx.send(embed=embed)

@help.command()
async def hug(ctx):
    em = discord.Embed(
        title =  "hug",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =hug {user you want to hug}", value = "Sends an embed showing an anime hug gif", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def lolgif(ctx):
    embed = discord.Embed(
        description = ("lol"),
        color = discord.Color.blue()
        )
    
    gifs = ["https://i.imgur.com/3sV8JoV.gif",
            "https://i.imgur.com/DLsoPMI.gif",
            "https://i.imgur.com/Z08kCMj.gif",
            "https://i.imgur.com/T4yXRtW.gif",
            "https://i.imgur.com/ptxNNQX.gif",
            "https://i.imgur.com/rZd0meE.gif",
            "https://i.imgur.com/wzUd9os.gif",
            "https://i.imgur.com/QnWP38H.gif",
            "https://i.imgur.com/Aq6RqkT.gif"]
     
    rgifs = random.choice(gifs)
    
    embed.set_image(url=rgifs)
    
    await ctx.send(embed=embed)

@help.command()
async def lolgif(ctx):
    em = discord.Embed(
        title =  "lolgif",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =lolgif", value = "Sends and embed that might make you laugh.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  
    
@client.command()
async def membed(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author
        
    else:
        user = ctx.author
        
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    title2q = await ctx.send('Waiting for a title')
    title2 = await client.wait_for('message', check=check)
  
    desc2 = await ctx.send('Waiting for a description')
    desc = await client.wait_for('message', check=check)
    
    fieldt2 = await ctx.send('Waiting for a field title')
    fieldt = await client.wait_for('message', check=check)
    
    fieldd2 = await ctx.send('Waiting for a field description')
    fieldd = await client.wait_for('message', check=check)

    embed = discord.Embed(title=title2.content, description=desc.content, color=discord.Color.blurple())
    embed.add_field(name = fieldt.content, value = fieldd.content, inline = False)
    #embed.set_author(ctx.author.mention, icon_url = ctx.author.avatar_url)
    embed.set_footer(text = "Made by " + str(user.name))
    
    todelete1 = await ctx.channel.fetch_message(title2q.id)
    todelete2 = await ctx.channel.fetch_message(desc2.id)
    todelete3 = await ctx.channel.fetch_message(fieldt2.id)
    todelete4 = await ctx.channel.fetch_message(fieldd2.id)
    await todelete1.delete()
    await todelete2.delete()
    await todelete3.delete()
    await todelete4.delete()
    
    
    
    todelete12 = await ctx.channel.fetch_message(title2.id)
    todelete22 = await ctx.channel.fetch_message(desc.id)
    todelete32 = await ctx.channel.fetch_message(fieldt.id)
    todelete42 = await ctx.channel.fetch_message(fieldd.id)
    await todelete12.delete()
    await todelete22.delete()
    await todelete32.delete()
    await todelete42.delete()
    
    todeleteforgod = await ctx.channel.fetch_message(ctx.message.id)
    await todeleteforgod.delete()
    #await ctx.channel.purge(limit=9)
    
    await ctx.send(embed=embed)

@help.command()
async def membed(ctx):
    em = discord.Embed(
        title =  "membed",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =membed", value = "Asks for a title, description, field title and field description after the command has been run, then makes an embed out of it", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  



@client.command()
async def bruh(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author
    else:
        user = ctx.author
    
    #await ctx.message.delete()
    embed = discord.Embed(
        color = discord.Color.blue()
        )
    
    gifs = 'https://i.imgur.com/qslkBXI.gif'
         
    embed.set_image(url=gifs)
    embed.set_footer(text = ("Requested by " + str(user.name)))
    await ctx.send(embed=embed)    
    
@help.command()
async def bruh(ctx):
    em = discord.Embed(
        title =  "bruh",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =bruh", value = "Sends a `bruh` gif", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def waitwhat(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author
        
    else:
        user = ctx.author
    
    #await ctx.message.delete()
    embed = discord.Embed(
        color = discord.Color.blue()
        )
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/759001253644206098/787935410528583700/what_1.png')
    embed.set_footer(text = ("Requested by " + str(user.name)))
    await ctx.send(embed=embed)    
      
@help.command()
async def waitwhat(ctx):
    em = discord.Embed(
        title =  "waitwhat",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =waitwhat", value = "Shows the `wait what` meme face", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def sweat(ctx, user : discord.Member = None):
    
    
    #await ctx.message.delete()
    
    gif  = "https://i.imgur.com/76o5wSJ.gif"
    
    if user == None:
        user = ctx.author
    else:
        user = ctx.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
        )
         
    embed.set_image(url=gif)
    embed.set_footer(text = ("Requested by " + str(user.name)))
    
    await ctx.send(embed=embed)  

@help.command()
async def sweat(ctx):
    em = discord.Embed(
        title =  "sweat",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sweat", value = "Shows a `sweat` gif", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def nice(ctx, user : discord.Member = None):
    
    
    #await ctx.message.delete()
    
    gif  = "https://i.imgur.com/prGfadj.gif"
    
    if user == None:
        user = ctx.author
    else:
        user = ctx.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
        )
         
    embed.set_image(url=gif)
    embed.set_footer(text = ("Requested by " + str(user.name)))
    
    await ctx.send(embed=embed)    

@help.command()
async def nice(ctx):
    em = discord.Embed(
        title =  "nice",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =nice", value = "Shows the `SOUUURP *tah* ***noice*** meme gif.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)     
    
@client.command()
async def yn(ctx, *, question):
    
    yon = ["yes",
           "no"]
    
    ryon = str(random.choice(yon))
    
    embed = discord.Embed(
        color = discord.Color.blurple()
        )
    
    embed.add_field(name = "Question : " + question, value = "Answer : " + ryon)
    
    await ctx.send(embed=embed)

@help.command()
async def yn(ctx):
    em = discord.Embed(
        title =  "yn",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =yn {Any question that can be answered with yes or no}", value = "Answers the question with `yes` or `no`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def pp(ctx, user : discord.Member = None):
    
    if user == None:
        user = ctx.author
    
    tomention = user
    
    pps= ['<=8',
          '<===8',
          '<======8',
          '<==========8',
          '<===================8',
          '<==========================================================8']
    
    rpp = random.choice(pps)
    
    await ctx.send(tomention.mention + "'s pp is \n" + rpp)

@help.command()
async def pp(ctx):
    em = discord.Embed(
        title =  "pp",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =pp {User's pp you want to measure} \n -_-", value = "Sends a random size pp?", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command(aliases=["randomcolour"])
async def randomcolor(ctx):
    colors = ["https://cdn.discordapp.com/attachments/785222159110504488/786268994503704596/marooon.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268993504935956/lightgray.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268991252725760/lightblue.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268989696770058/green.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268988320907274/darkerblue.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268979895074846/black.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268982629761074/blue.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268984982110225/blurple.png",
              "https://cdn.discordapp.com/attachments/785222159110504488/786268986747912203/brown.png"]
    
    embed = discord.Embed()
    rc = random.choice(colors)
    embed.set_image(url=rc)
    
    await ctx.send(embed=embed)

@help.command()
async def randomcolor(ctx):
    em = discord.Embed(
        title =  "randomcolor",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =randomcolor", value = "Sends a random color lol", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
@commands.has_permissions(manage_guild = True)
async def gstart(ctx, mins : int, *,prize):
    embed = discord.Embed(title = "Giveaway!", description = f"Prize = {prize}", color = ctx.author.color)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins * 60)
    
    embed.add_field(name="Ends At:", value=f"{end} UTC")
    embed.add_field(name="React with:", value="🎉 to Enter!")
    embed.set_footer(text = f"Ends {mins} minutes from now!")
    sender = ctx.author
    
    embed.set_footer(text = f"Hosted by {sender.name}.")
    my_msg = await ctx.send(embed=embed)
    
    await my_msg.add_reaction("🎉")
    
    await asyncio.sleep(mins * 60) #mins * 60

    new_msg = await ctx.channel.fetch_message(my_msg.id)
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    
    winner = random.choice(users)
    
    await ctx.send(f"{winner.mention}")
    embed = discord.Embed(title = ":partying_face: YAY! :tada:", description = f"Someone won {prize}!!!", color = discord.Color.blurple())
    embed.add_field(name = "GG'S " + winner.name, value = winner.mention + f" won the giveaway and {prize}!")
    
    
    await ctx.send(embed=embed)

@help.command()
async def gstart(ctx):
    em = discord.Embed(
        title =  "gstart",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =gstart {time till the giveaway ends in minutes} {the prize}", value = "Starts a giveaway that can be participated in by reacting with the :tada: on the embed sent \n Requires `Manage Server`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def textlang(ctx):
    textlangs = ["ttyl = talk to you later",
                 "idk = i dont know",
                 "ips = im pretty sure",
                 "ik = i know",
                 "yk/uk = you know",
                 "smh = shakin' my head",
                 "tbh = to be honest",
                 "gg = good game",
                 "gf = good fight",
                 "ty = thank you",
                 "yw = your welcome",
                 "wdym = what do you mean",
                 "lol = laughing out loud",
                 "rly = really",
                 "brb = be right back",
                 "tom = tomorrow",
                 "abt = about",
                 "ngl = not gonna lie",
                 "ikr = i know right"]
    
    rtl = random.choice(textlangs)
    
    embed = discord.Embed(
        title = "Random Text Language Shortcut",
        color = discord.Color.blurple()
        )
    embed.add_field(name = rtl, value = ".", inline = False)
    await ctx.send(embed = embed)

@help.command()
async def textlang(ctx):
    em = discord.Embed(
        title =  "textlang",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =textlang", value = "Sends a random text language shortcut", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)     
    
@client.command()
async def timerm(ctx, mins : int):
    
    embed = discord.Embed(
        title = "Set Timer",
        description = f"for {mins} minutes",
        color = ctx.author.color)
    
    await ctx.send(embed = embed)
    
    await asyncio.sleep(mins * 60)
    
    embed2 = discord.Embed(
        title = "Timers Done!",
        description = f"{mins} minutes have passed!",
        color = discord.Color.green()
        )
    
    await ctx.send(ctx.author.mention)
    
    await ctx.send(embed = embed2)

@help.command()
async def timerm(ctx):
    em = discord.Embed(
        title =  "timerm",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =timerm {how many minutes you want to set a timer for}", value = "Sets a timer for mentioned amount of minutes and then pings you when the timer has ended.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)  

@client.command()
async def timers(ctx, mins : int):
    
    embed = discord.Embed(
        title = "Set Timer",
        description = f"for {mins} seconds",
        color = ctx.author.color)
    
    await ctx.send(embed = embed)
    
    await asyncio.sleep(mins)
    
    embed2 = discord.Embed(
        title = "Timers Done!",
        description = f"{mins} seconds have passed!",
        color = discord.Color.green()
        )
    
    await ctx.send(ctx.author.mention)
    
    await ctx.send(embed = embed2)

@help.command()
async def timers(ctx):
    em = discord.Embed(
        title =  "timers",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =timers {how many seconds you want to set a timer for}", value = "Sets a timer for mentioned amount of seconds and then pings you when the timer has ended.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def timerh(ctx, mins : int):
    
    embed = discord.Embed(
        title = "Set Timer",
        description = f"for {mins} hours",
        color = ctx.author.color)
    
    await ctx.send(embed = embed)
    
    await asyncio.sleep(mins * 60 * 60)
    
    embed2 = discord.Embed(
        title = "Timers Done!",
        description = f"{mins} hours have passed!",
        color = discord.Color.green()
        )
    
    await ctx.send(ctx.author.mention)
    
    await ctx.send(embed = embed2)

@help.command()
async def timerh(ctx):
    em = discord.Embed(
        title =  "timerh",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =timerh {how many hours you want to set a timer for}", value = "Sets a timer for mentioned amount of hours and then pings you when the timer has ended.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)    
 
@client.command()
async def no(ctx, user : discord.Member = None):
    #await ctx.message.delete()
    gif  = "https://cdn.discordapp.com/attachments/785222159110504488/786917355543592980/png.png"
    
    if user == None:
        user = ctx.author
    else:
        user = ctx.author
    
    embed = discord.Embed(
        color = discord.Color.blue()
        )
         
    embed.set_image(url=gif)
    embed.set_footer(text = ("Requested by " + str(user.name)))
    
    await ctx.send(embed=embed)

@help.command()
async def no(ctx):
    em = discord.Embed(
        title =  "no",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =no", value = "Sends a `no` image", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def wanted(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("wanted.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((245,245))
    wanted.paste(pfp, (117, 243))
    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))

@help.command()
async def wanted(ctx):
    em = discord.Embed(
        title =  "wanted",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =wanted {user who you want to make wanted}", value = "Sends a wanted image with the wanted person being the mentioned user's avatar", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command(aliases = ['googel11','g11'])
async def google11(ctx, farg : str, sarg : str):
    if farg == discord.Member:
        await ctx.send("Don't mention a person. Write text. Like this =googel11 reality")
        
    else:
        wanted = Image.open("googel2.jpg")
        
        font = ImageFont.truetype("arial2.ttf", 24) 
        
        draw = ImageDraw.Draw(wanted)
        
        text = str(farg)
        draw.text((33,193), text, (0,0,0), font=font)
        
        text2 = str(sarg)
        draw.text((33,517), text2, (0,0,0), font=font)
        
        wanted.save("profile69.jpg")
    
        await ctx.send(file = discord.File("profile69.jpg"))

@help.command()
async def google11(ctx):
    em = discord.Embed(
        title =  "google11",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name='Format : =google11 "{original search}" "{search after 11 minutes}"', value = 'Sends a google image with two searches 11 minutes apart \n make sure to use "  " around both arguments', inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =googel11, =g11")
    await ctx.send(embed=em)

@help.command()
async def googel11(ctx):
    em = discord.Embed(
        title =  "google11",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name='Format : =google11 "{original search}" "{search after 11 minutes}"', value = 'Sends a google image with two searches 11 minutes apart \n make sure to use "  " around both arguments', inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =googel11, =g11")
    await ctx.send(embed=em)

@help.command()
async def g11(ctx):
    em = discord.Embed(
        title =  "google11",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name='Format : =google11 "{original search}" "{search after 11 minutes}"', value = 'Sends a google image with two searches 11 minutes apart \n make sure to use "  " around both arguments', inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =googel11, =g11")
    await ctx.send(embed=em)

@client.command()
async def imp(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("imp.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((100,100))
    wanted.paste(pfp, (579, 359))
    
    font = ImageFont.truetype("ob.ttf", 26) 
    
    draw = ImageDraw.Draw(wanted)
    
    text = str(user.name)
    draw.text((585,530), text, (255,255,255), font=font)
      
    
    wanted.save("profile2.jpg")

    await ctx.send(file = discord.File("profile2.jpg"))
    
@help.command()
async def imp(ctx):
    em = discord.Embed(
        title =  "imp",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =imp {user who should be impostor}", value = "Sends the among us impostor screen with the impostor name and picture being that of the mentioned user", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

@client.command(aliases=['g'])
async def gradient(ctx, c1 : str, c2 : str):
    async with ctx.typing():
        def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
                c1=np.array(mpl.colors.to_rgb(c1))
                c2=np.array(mpl.colors.to_rgb(c2))
                return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

        n=500

        fig, ax = plt.subplots(figsize=(8, 5))
        for x in range(n+1):
            ax.axvline(x, color=colorFader(c1,c2,x/n), linewidth=4) 
        plt.show()

        plt.savefig("glol.jpg",dpi=72)


    await ctx.send(file = discord.File("glol.jpg"))

@help.command()
async def gradient(ctx):
    em = discord.Embed(
        title =  "gradient",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =gradient {color 1} {color 2}", value = "Makes a gradient out of 2 colors", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =g")
    await ctx.send(embed=em)

@help.command()
async def g(ctx):
    em = discord.Embed(
        title =  "gradient",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =gradient {color 1} {color 2}", value = "Makes a gradient out of 2 colors", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =g")
    await ctx.send(embed=em)


@client.command()
async def av(ctx, user : discord.Member = None):
    if user == None:
        user= ctx.author
        
    wanted = Image.open("white.jpg")
    asset = user.avatar_url_as(size=256)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((128,128))
    wanted = wanted.resize((128,128))
    wanted.paste(pfp,(0,0))
    
    
    wanted.save("av.gif")
    
    await ctx.send(file = discord.File("av.gif"))

@client.command()
@commands.has_permissions(manage_channels = True)
async def mark_nsfw(ctx, conf : str):
    if conf == "y":
        await ctx.channel.edit(nsfw=True)
        await ctx.send(":underage: Marked  ||" + str(ctx.channel.mention) + "||  as nsfw! :smirk:")
    
    elif conf == "n":
        await ctx.channel.edit(nsfw=False)
        await ctx.send(":cool: Marked  ||" + str(ctx.channel.mention) + "||  as not NSFW. :angel:")

    else:
        await ctx.send("MAKE SURE YOU USE THE RIGHT FORMAT! `=mark_nsfw y` or `=mark_nsfw n`!")
    
@help.command()
async def mark_nsfw(ctx):
    em = discord.Embed(
        title = "mark_nsfw",
        color = ctx.author.color
    )
    em.add_field(name = "=mark_nsfw {y if you want to mark it NSFW, or n if you want to mark it not NSFW} \n For eg: =mark_nsfw n --> would mark it as **not** NSFW", value = "Marks the specific channel as NSFW or not. \n Requires `Manage Channels`", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)


@help.command()
async def av(ctx):
    em = discord.Embed(
        title =  "av",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =av {mention whose avatar you want to get}", value = "Sends the avatar of the mentioned user", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def headache(ctx, *, text2):
    if text2 == discord.Member:
        await ctx.send("Don't mention a person. Write text. Like this =headache reality")
        
    else:
        wanted = Image.open("head.jpg")
        
        font = ImageFont.truetype("arial2.ttf", 24) 
        
        draw = ImageDraw.Draw(wanted)
        
        text = str(text2)
        draw.text((335,494), text, (0,0,0), font=font)
          
        
        wanted.save("profile3.jpg")
    
        await ctx.send(file = discord.File("profile3.jpg"))
    
@help.command()
async def headache(ctx):
    em = discord.Embed(
        title =  "headache",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =headache {What should be the cause of the headache}", value = "Sends the `Stress, Hypertension` meme", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def google(ctx, *, text2):
    
    randomn = random.randrange(1, 6900)#614,7

    wanted = Image.open("f.jpg")
        
    font = ImageFont.truetype("arial2.ttf", 28) 
    font2 = ImageFont.truetype("arial2.ttf", 18) 
    draw = ImageDraw.Draw(wanted)
        
    text = str(text2)
    text3 = str(randomn)
    draw.text((125,204), text, (0,0,0), font=font)
    draw.text((614, 7), (text3 + " results"), (0,0,0), font=font2)
          
        
    wanted.save("profile4.jpg")
    
    await ctx.send(file = discord.File("profile4.jpg"))

@help.command()
async def google(ctx):
    em = discord.Embed(
        title =  "google",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =google {what you want to google}", value = "Sends an image with the google homepage and shows the *what you want to google* in the search bar", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def servers(ctx):

    #s = {len(client.guilds)}
      
    await ctx.send(f"`I am currently in {len(client.guilds)} servers.`")

@help.command()
async def servers(ctx):
    em = discord.Embed(
        title =  "",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =servers", value = "Sends how many servers the bot is in", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)
    
@client.command()
async def test(ctx):
    await ctx.send("i'm working alrit? IM WORKING STOPDOINGTHETESSTCOMMANDIMWORKINGAAAAAAAAAAAA")

@client.command()
async def think(ctx):
    
    #await ctx.message.delete()
    
    await ctx.send("<:blobhyperthink:762704635122286632>")
    


@client.command()
async def simp(ctx):
   # await ctx.message.delete()
    
    await ctx.send("<:simp:788082857653960704>")

@client.command()
async def thonk(ctx):
    #await ctx.message.delete()
    
    await ctx.send("<:thonk:788082561427308605>")
    
@client.command()
async def ohno(ctx):
    #await ctx.message.delete()
    
    await ctx.send("<:ohno:788084015575990343>")
    
@client.command()
async def give(ctx, person : str, *, thing):
    await ctx.send(f"`Gave {person} {thing}.`")
    
@help.command()
async def give(ctx):
    em = discord.Embed(
        title =  "give",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =give {who you want to give[no mentioning,or spaces]} {what you want to give}", value = "Returns *Gave `user` `what you wanted to give` *", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def kill(ctx, *, person):
    kills = [f"{person} fell out of the world.",
             f"{person} died.",
             f"{person} was pricked to death.",
             f"{person} did not want to live in the same world as Enderman.",
             f"{person} committed notalive.exe.",
             f"{person} was shot by Reality.",
             f"{person} was bonked."]
    
    rkill = random.choice(kills)
    
    await ctx.send(f"`{rkill}`")

@help.command()
async def kill(ctx):
    em = discord.Embed(
        title =  "kill",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =kill {what/who you want to kill[no spaces or mentioning]}", value = "Returns a random choice from the list of messages aka kill messages.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)
  
@client.command()
async def tp(ctx, thing1 : str, *, thing2):
    await ctx.send(f"`Teleported {thing1} to {thing2}.`")

@help.command()
async def tp(ctx):
    em = discord.Embed(
        title =  "tp",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =tp {thing you want to tp} {where you want to tp it to}", value = "*Returns `Teleported {thing} {where}`*", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def repair(ctx, *, thing):
    await ctx.send(f"`Repaired {thing}.`")

@help.command()
async def repair(ctx):
    em = discord.Embed(
        title =  "repair",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =repair {what you want to repair}", value = "*Returns `Repaired {whatever you said before}`*", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def info(ctx):
    embed = discord.Embed(
        title = "Info about ohnobot",
        color = discord.Color.blurple()
        )
    
    embed.add_field(name = "`Library`", value = "discord.py", inline=False)
    embed.add_field(name = "`Developer`", value = "materwelon#7555", inline=False)
    embed.add_field(name = "`Servers`", value = f"ohnobot is currently in {len(client.guilds)} servers.", inline=False)
    embed.add_field(name = "`Invite Link`", value = "https://discord.com/api/oauth2/authorize?client_id=790639657226469436&permissions=8&scope=bot", inline=False)
    #embed.add_field(name = "`Commands`", value = "64", inline=False)
    embed.set_footer(text = "Use =supportinvite to join the support server!")
    
    await ctx.send(embed=embed)

@help.command()
async def info(ctx):
    em = discord.Embed(
        title =  "info",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =info", value = "Returns info about the bot", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)    

@client.command()
async def roleperms(ctx, theid : int):
    role = get(ctx.guild.roles, id = theid)
    
    roleperms = role.permissions
    
    #emlist = []
    
    
    em = discord.Embed(
                title = "Role permissions for",
                description = role.mention,
                color = discord.Color.blurple()
                )
    
    for perm, granted in roleperms:
        if perm == "administrator":
            em.add_field(name = "Administrator", value = str(granted), inline = True)
        elif perm == "manage_messages":
            em.add_field(name = "Manage Messages", value = str(granted), inline = True)
        elif perm == "manage_nicknames":
            em.add_field(name = "Manage Nicknames", value = str(granted), inline = True)
        elif perm == "manage_guild":
            em.add_field(name = "Manage Server", value = str(granted), inline = True)
        elif perm == "administrator":
            em.add_field(name = "Manage Messages", value = str(granted), inline = True)
        elif perm == "kick_members":
            em.add_field(name = "Kick Memebers", value = str(granted), inline = True)
        elif perm == "ban_members":
            em.add_field(name = "Ban Members", value = str(granted), inline = True)
        elif perm == "view_audit_log":
            em.add_field(name = "View Audit Log", value = str(granted), inline = True)
        elif perm == "manage_roles":
            em.add_field(name = "Manage Roles", value = str(granted), inline = True)
        elif perm == "manage_channels":
            em.add_field(name = "Manage Channels", value = str(granted), inline = True)
        elif perm == "manage_emojis":
            em.add_field(name = "Manage Emojis", value = str(granted), inline = True)
        elif perm == "manage_webhooks":
            em.add_field(name = "Manage Webhooks", value = str(granted), inline = True)
        elif perm == "mute_members":
            em.add_field(name = "Mute Members(Voice)", value = str(granted), inline = True)
        elif perm == "deafen_members":
            em.add_field(name = "Deafen Members(Voice)", value = str(granted), inline = True)
        elif perm == "move_members":
            em.add_field(name = "Move Members(Voice)", value = str(granted), inline = True)
        elif perm == "send_messages":
            em.add_field(name = "Send Messages", value = str(granted), inline = True)

    await ctx.send(embed=em)

@help.command()
async def roleperms(ctx):
    em = discord.Embed(
        title =  "",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =roleperms {*ID* of the role whose permissions you want}", value = "Returns the permissions for the role IN THE SPECIFIC CHANNEL", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def perms(ctx, user : discord.Member = None):
    #role = get(ctx.guild.roles, id = theid)
    
    if user == None:
        user = ctx.author
    
    
    
    
    roleperms = user.permissions_in(ctx.channel)
    
    #emlist = []
    
    
    em = discord.Embed(
                title = "User permissions for",
                description = user.mention,
                color = discord.Color.blurple()
                )
    
    for perm, granted in roleperms:
        if perm == "administrator":
            em.add_field(name = "Administrator", value = str(granted), inline = True)
        elif perm == "manage_messages":
            em.add_field(name = "Manage Messages", value = str(granted), inline = True)
        elif perm == "manage_nicknames":
            em.add_field(name = "Manage Nicknames", value = str(granted), inline = True)
        elif perm == "manage_guild":
            em.add_field(name = "Manage Server", value = str(granted), inline = True)
        elif perm == "administrator":
            em.add_field(name = "Manage Messages", value = str(granted), inline = True)
        elif perm == "kick_members":
            em.add_field(name = "Kick Memebers", value = str(granted), inline = True)
        elif perm == "ban_members":
            em.add_field(name = "Ban Members", value = str(granted), inline = True)
        elif perm == "view_audit_log":
            em.add_field(name = "View Audit Log", value = str(granted), inline = True)
        elif perm == "manage_roles":
            em.add_field(name = "Manage Roles", value = str(granted), inline = True)
        elif perm == "manage_channels":
            em.add_field(name = "Manage Channels", value = str(granted), inline = True)
        elif perm == "manage_emojis":
            em.add_field(name = "Manage Emojis", value = str(granted), inline = True)
        elif perm == "manage_webhooks":
            em.add_field(name = "Manage Webhooks", value = str(granted), inline = True)
        elif perm == "mute_members":
            em.add_field(name = "Mute Members(Voice)", value = str(granted), inline = True)
        elif perm == "deafen_memebrs":
            em.add_field(name = "Deafen Members(Voice)", value = str(granted), inline = True)
        elif perm == "move_members":
            em.add_field(name = "Move Members(Voice)", value = str(granted), inline = True)
        elif perm == "send_messages":
            em.add_field(name = "Send Messages", value = str(granted), inline = True)

    await ctx.send(embed=em)

@help.command()
async def perms(ctx):
    em = discord.Embed(
        title =  "perms",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =perms {user [if none mentiones, yourself]}", value = "Rerurns the permissions of the specified user", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def roleid(ctx, role : discord.Role):
    toreturn = role.id
    await ctx.send(str(toreturn))

@help.command()
async def roleid(ctx):
    em = discord.Embed(
        title =  "roleid",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =roleid {mention the role}", value = "Returns the ID of the role mentioned", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def dogfact(ctx):

        
    URL = "https://some-random-api.ml/facts/dog"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def dogfact(ctx):
    em = discord.Embed(
        title =  "dogfact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =dogfact", value = "Returns a dog fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)


@client.command()
async def catfact(ctx):

        
    URL = "https://some-random-api.ml/facts/cat"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def catfact(ctx):
    em = discord.Embed(
        title =  "catfact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =catfact", value = "Returns a cat fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def pandafact(ctx):

        
    URL = "https://some-random-api.ml/facts/panda"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def pandafact(ctx):
    em = discord.Embed(
        title =  "pandafact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =pandafact", value = "Returns a panda fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def foxfact(ctx):

        
    URL = "https://some-random-api.ml/facts/fox"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def foxfact(ctx):
    em = discord.Embed(
        title =  "foxfact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =foxfact", value = "Returns a fox fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def birdfact(ctx):

        
    URL = "https://some-random-api.ml/facts/bird"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def birdfact(ctx):
    em = discord.Embed(
        title =  "birdfact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =birdfact", value = "Returns a bird fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)
           
@client.command()
async def koalafact(ctx):

        
    URL = "https://some-random-api.ml/facts/koala"
    
    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
            
        else:
            await ctx.send("There was an error with the API")

@help.command()
async def koalafact(ctx):
    em = discord.Embed(
        title =  "koalafact",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =koalafact", value = "Returns a koala fact", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command(aliases = ['c'])
async def chat(ctx, *,message):
    #yes = 1
    
    responses = ["Sure!",
                 "I don't think so...",
                 "Sorry",
                 "bruh",
                 "Why though",
                 "sorry my bren is not workin properlee",
                 ":)",
                 "ohno",
                 ":smirk:",
                 ":thumbsup:",
                 "yes",
                 "no",
                 "uwu",
                 "owo"]
    
    if message in ('How are you' , 'how are u' , 'how r u'):
        res2 = ["Good, Thanks!",
                "currently dying, maybe call an ambulance",
                "depressed",
                "**IM ON THE TOP OF THE WORRRRRRRRRRRRLLLLLLLLLLLLDDDDDDDDDDDDDD**",
                "cheese",
                "dead",
                "weewooweewoo",
                "owo",
                "uwu",
                "im going through a existential crisis but good thanks for asking #whenurnotfinebutyouhavetosaythaturfine"]
        
        await ctx.send(random.choice(res2))
        
    elif message in ('male or female' , 'boy or girl'):
        res3 = ["*we never know*",
                "I'm a bot mate, a bot. You're talkin to a bot! #wheredidhisfriendsgo",
                "boygirlmalefemale thing",
                "beep boop",
                "a thing",
                "no"]
        await ctx.send(random.choice(res3))

    else:
        await ctx.send(random.choice(responses))

@help.command()
async def chat(ctx):
    em = discord.Embed(
        title =  "chat",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =chat {any message}", value = "Sends a message, maybe based on what you said, like a chatbot, but suckier", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =c")
    await ctx.send(embed=em)

@client.command()
async def wasted(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
            
        url = f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}"
        wastedsession = ClientSession()
        #wastedget = await wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as img:
        async with request("GET", url, headers={}) as img:
            if img.status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()
                
            else:
                data = BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'wasted.jpg'))
                await wastedsession.close()    

@help.command()
async def wasted(ctx):
    em = discord.Embed(
        title =  "wasted",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =wasted {user you want to *waste*}", value = "Adds the *WASTED* overlay to the users avatar", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def triggered(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
            
        url = f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='jpg')}"
        wastedsession = ClientSession()
        #wastedget = await wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as img:
        async with request("GET", url, headers={}) as img:
            if img.status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()
                
            else:
                data = BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'triggered.jpg'))
                await wastedsession.close()  

@help.command()
async def triggered(ctx):
    em = discord.Embed(
        title =  "triggered",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =triggered {user who is triggered}", value = "Adds the ***TRIGGERED*** overlay to the users avatar", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def glass(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
            
        url = f"https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format='jpg')}"
        wastedsession = ClientSession()
        #wastedget = await wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as img:
        async with request("GET", url, headers={}) as img:
            if img.status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()
                
            else:
                data = BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'glass.jpg'))
                await wastedsession.close()

@help.command()
async def glass(ctx):
    em = discord.Embed(
        title =  "glass",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =glass {user who should be in glass}", value = "Adds a glass overlay to the users avatar", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)
               
"""@client.command()
async def invert(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
            
        url = f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='jpg')}"
        wastedsession = ClientSession()
        #wastedget = await wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='jpg')}") as img:
        async with request("GET", url, headers={}) as img:
            if img.status != 200:
                await ctx.send("Unable to get image")
                await wastedsession.close()
                
            else:
                data = BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'invert.jpg'))
                await wastedsession.close()  """
@client.command()
async def pixelate(ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
     
                
        asset = member.avatar_url_as(size = 256, format='jpg')
        data = BytesIO(await asset.read())
        pfp = Image.open(data) 
        
        imgSmall = pfp.resize((16,16),resample=Image.BILINEAR)
        
        result = imgSmall.resize(pfp.size,Image.NEAREST)
        
        result.save("pixelated.jpg")
        
        await ctx.send(file = discord.File("pixelated.jpg"))

@help.command()
async def pixelate(ctx):
    em = discord.Embed(
        title =  "pixelate",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =pixelate {user who should be pixelated}", value = "Pixelates the users avatar to 16x16 and then sends it", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

                

                
                
                
@client.command(aliases=['stats','statsearch','ss'])
async def statussearch(ctx, tosearch : str):
    
    
    thing = {}
    
    
    em = discord.Embed(
        title = "Searching for " + tosearch,
        color = ctx.author.color
        )
    for member in ctx.guild.members:
            if tosearch in str(member.activity).lower():
                    thing[member.name] = member.activity
                    #em.add_field(name = member.name, value = member.activity, inline = True)
                    
                    #heck1 = 1
           
            """if tosearch not in str(member.activity):
                       
            em.add_field(name = ":(", value = "No other activities found for your search, `" + tosearch + "`.")"""
                
    #check1 = 
    
    list1 = list(thing.keys())
    list2 = list(thing.values())
    
    #val = int
    val = 0
    for _ in thing:
        em.add_field(name = list1[val], value = list2[val], inline = False)
        val += 1
    await ctx.send(embed=em)
    
@help.command()
async def statussearch(ctx):
    em = discord.Embed(
        title =  "statussearch",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =statussearch {what you want to search for}", value = "Searches for whatever you searched for in other people's status, **NO CAPITAL LETTERS**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =ss, =stats, =statsearch")
    await ctx.send(embed=em)    

@help.command()
async def ss(ctx):
    em = discord.Embed(
        title =  "statussearch",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =statussearch {what you want to search for}", value = "Searches for whatever you searched for in other people's status, **NO CAPITAL LETTERS**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =ss, =stats, =statsearch")
    await ctx.send(embed=em)  

@help.command()
async def stats(ctx):
    em = discord.Embed(
        title =  "statussearch",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =statussearch {what you want to search for}", value = "Searches for whatever you searched for in other people's status, **NO CAPITAL LETTERS**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =ss, =stats, =statsearch")
    await ctx.send(embed=em)    

@help.command()
async def statsearch(ctx):
    em = discord.Embed(
        title =  "statussearch",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =statussearch {what you want to search for}", value = "Searches for whatever you searched for in other people's status, **NO CAPITAL LETTERS**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =ss, =stats, =statsearch")
    await ctx.send(embed=em)         
        
import PIL.ImageOps
@client.command()
async def invert(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
        
    asset = user.avatar_url_as(size = 256, format='jpg')
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
        
    
    image = PIL.ImageOps.invert(pfp)
    image.save("save.jpg")
    await ctx.send(file = discord.File("save.jpg"))

@help.command()
async def invert(ctx):
    em = discord.Embed(
        title =  "invert",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =invert {any user}", value = "Inverts the colors in the user's avatar and sends it", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command(aliases=['sget','sociuxg','sg'])
async def sociuxget(ctx, *,toconvert):

    my_dict = {}
    my_dict[97]="ko"
    my_dict[98]="r"
    my_dict[99]="t"
    my_dict[100]="pdo"
    my_dict[101]="re"
    my_dict[102]="tai"
    my_dict[103]="qi"
    my_dict[104]="no"
    my_dict[105]="vi"
    my_dict[106]="gh"
    my_dict[107]="jo"
    my_dict[108]="ne"
    my_dict[109]="li"
    my_dict[110]="wo"
    my_dict[111]="wae"
    my_dict[112]="shi"
    my_dict[113]="iiy"
    my_dict[114]="te"
    my_dict[115]="io"
    my_dict[116]="yui"
    my_dict[117]="ru"
    my_dict[118]="ith"
    my_dict[119]="nok"
    my_dict[120]="kshe"
    my_dict[121]="mey"
    my_dict[122]="xui"

    await ctx.send(toconvert.translate(my_dict))

@help.command()
async def sociuxget(ctx):
    em = discord.Embed(
        title =  "sociuxget",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sociuxget {what you want to convert to sociux}", value = "Turns the text you typed into sociux", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =sg, =sget, =sociuxg")
    await ctx.send(embed=em)

@help.command()
async def sg(ctx):
    em = discord.Embed(
        title =  "sociuxget",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sociuxget {what you want to convert to sociux}", value = "Turns the text you typed into sociux", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =sg, =sget, =sociuxg")
    await ctx.send(embed=em)

@help.command()
async def sget(ctx):
    em = discord.Embed(
        title =  "sociuxget",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sociuxget {what you want to convert to sociux}", value = "Turns the text you typed into sociux", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =sg, =sget, =sociuxg")
    await ctx.send(embed=em)

@help.command()
async def sociuxg(ctx):
    em = discord.Embed(
        title =  "sociuxget",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sociuxget {what you want to convert to sociux}", value = "Turns the text you typed into sociux", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : =sg, =sget, =sociuxg")
    await ctx.send(embed=em)

@client.command()
async def sociux(ctx):
    em = discord.Embed(
        title = "Sociux Conversion List",
        color = discord.Color.blue()
    )
    em.add_field(name = "a = ko \n b = r \n c = t \n d = pdo \n e = re \n f = tai \n g = qi \n h = no \n i = vi \n j = gh \n k = jo \n l = ne \n m = li \n n = wo \n o = wae \n p = shi \n q = iiy \n r = te \n s = io \n t = yui \n u = ru \n v = ith \n w = nok \n x = kshe \n y = mey \n z = xui", value="sociux is a language created by materwelon and is implemented in the discord bot ohnobot. Made in around 10 minutes using the advanced AI library pre-built into the amazing-yet-ordinary human brain.", inline = False)

    await ctx.send(embed=em)

@help.command()
async def sociux(ctx):
    em = discord.Embed(
        title =  "sociux",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =sociuxget", value = "Sends a help message about sociux \n Use =help sociuxget", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def scr(ctx, site):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(colour = discord.Colour.blurple(), timestamp=ctx.message.created_at)
        tosend = f"http://image.thum.io/get/width/1080/crop/675/http://{site}"
        embed.set_image(url=tosend)
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        #await ctx.send(f"https://image.thum.io/get/width/1080/crop/675/http://{site}")
        await ctx.send(embed=embed)  
    else:
        await ctx.send("To avoid abuse, we restrict this command to `NSFW Channels` ONLY.")

@help.command()
async def scr(ctx):
    em = discord.Embed(
        title =  "scr",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =scr {website, must *NOT* include the http://}", value = "Sends the screenshot of the top part of the page of the URL \n Must be used in `NSFW Channels` only.", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)


@client.command()
async def msginfo(ctx, chan : discord.TextChannel, theid : int):

    themsg = await chan.fetch_message(theid)

    em = discord.Embed(
        title = "Info about a message",
        description = "*" + themsg.content + "*",
        color = ctx.author.color
    )
    em.add_field(name="Message Content : ", value = str(themsg.content))
    em.add_field(name = "Message ID : ", value = str(themsg.id),inline = False)
    em.add_field(name = "Message Author : ", value = str(themsg.author.name),inline = False)
    #em.add_field(name = "Was messages Text-To-Speech? : ", value = str(themsg.tts),inline = False)    
    em.add_field(name = 'Jump URL : ', value = themsg.jump_url)
    #em2.add_field(name="Guild/Server : ", value = str(themsg.guild))

    em2 = discord.Embed(
        title = "Info about a message(Page 2)",
        description = "*" + themsg.content + "*",
        color = ctx.author.color
    )
    em2.add_field(name="Guild/Server : ", value = (themsg.guild).name, inline=False)
    em2.add_field(name="Channel : ", value = (themsg.channel).name ,inline=False)
    em2.add_field(name="Is message Pinned? : ", value = str(themsg.pinned), inline=False)
    em2.add_field(name="Was/Is Message a Text-To-Speech Message? : ", value = str(themsg.tts), inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️','first')
    paginator.add_reaction('◀️','back')
    #paginator.add_reaction('🔐','lock')
    paginator.add_reaction('▶️','next')
    paginator.add_reaction('⏭️','last')

    embeds = [em,em2]
    await paginator.run(embeds)

@help.command()
async def msginfo(ctx):
    em = discord.Embed(
        title =  "msginfo",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =msginfo {channel in which the message was sent} {the message id}", value = "Returns information about a message. \n **Any Message ID that is Invalid or Not in the channel mentioned will return an error!**", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em)

@client.command()
async def math(ctx, no1 : int, no2 : int):
    em = discord.Embed(title = "Addition", description =  f"{no1} + {no2} = " + str(no1 + no2),inline=False)
    em2 = discord.Embed(title = "Subtraction(Way 1)", description = f"{no1} - {no2} = " + str(no1 - no2),inline=False)
    em3 = discord.Embed(title = "Subtraction(Way 2)", description = f"{no2} - {no1} = " + str(no2 - no1),inline=False)
    em4 = discord.Embed(title = "Multiplication", description =  f"{no1} * {no2} = " + str(no1 * no2),inline=False)
    em5 = discord.Embed(title = "Division(Way 1)", description = f"{no1} / {no2} = " + str(no1 / no2),inline=False)
    em6 = discord.Embed(title = "Division(Way 2)", description = f"{no2} / {no1} = " + str(no2 / no1),inline=False)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️','first')
    paginator.add_reaction('◀️','back')
    #paginator.add_reaction('🔐','lock')
    paginator.add_reaction('▶️','next')
    paginator.add_reaction('⏭️','last')

    embeds = [em,em2,em3,em4,em5,em6]
    await paginator.run(embeds)

@help.command()
async def math(ctx):
    em = discord.Embed(
        title =  "math",
        #description = "Category : Fun, =helpfun",
        color = ctx.author.color
    )

    em.add_field(name="Format : =math {any number} {any number}", value = "Returns basic math calculations ", inline = False)
    em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    em.set_footer(text="Aliases : None")
    await ctx.send(embed=em
    




client.run(YOUR TOKEN)
