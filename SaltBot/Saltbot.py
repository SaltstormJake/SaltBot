import discord
from discord.ext import commands

kirbyThemeFirst = False
kirbyThemeSecond = False
kirbyThemeThird = False
kirbyThemeFourth = False
kirbyThemeFifth = False
kirbyThemeSixth = False
kirbyCount = 0
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    if member.id == 528432284555149343: #plippers
        print('Like clockwork.')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(160197389032882176)
    if member.id == 528432284555149343: #plippers
        await channel.send('There she goes again.')
    elif member.id == 405457847233806337: #jake
        await channel.send('Trust me, he probably has a reason.')
    elif member.id == 225837816234377217: #daniel
        await channel.send('Wow, his departure shocks me.')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'clim' in message.content:
        await message.channel.send('HEE HEE HEE HEEEEEEEUUUUUUUUE')
    
    #kirby theme song!
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    sentence = message.content.lower()
    global kirbyThemeFirst
    global kirbyThemeSecond
    global kirbyThemeThird
    global kirbyThemeFourth
    global kirbyThemeFifth
    global kirbyCount
    global kirbyThemeSixth
    for char in sentence:
        if char in punc:
            sentence = sentence.replace(char, '')
    if 'kirby kirby kirby' == sentence:
        if not kirbyThemeThird:
            if not kirbyThemeFirst:
                await message.channel.send("That's a name you should know!")
                kirbyThemeFirst = True
            else:
                await message.channel.send("He's the star of the show!")
                kirbyThemeFirst = False
        else:
            if not kirbyThemeFourth:
                await message.channel.send("Savin' the day!")
                kirbyThemeFourth = True
            else:
                await message.channel.send("He's here to stay!")
                kirbyThemeFourth = False
    elif "thats a name you should know" == sentence:
        await message.channel.send("Kirby Kirby Kirby, he's the star of the show!")
    elif "hes the star of the show" == sentence:
        await message.channel.send("He's more than you think!")
    elif "hes more than you think" == sentence:
        await message.channel.send("He's got maximum pink!")
    elif "hes got maximum pink" == sentence:
        await message.channel.send("Kirby Kirby Kirby's the one!")
    elif "kirby kirby kirbys the one" == sentence:
        await message.channel.send("He comes-a right back at ya!")
        kirbyThemeSecond = True
    elif "he comes right back at ya" == sentence or "he comesa right back at ya" == sentence:
        if not kirbyThemeSecond:
            await message.channel.send("He comes-a right back at ya!")
            kirbyThemeSecond = True
        else:
            await message.channel.send("Give it all that you got!")
            kirbyThemeSecond = False
    elif "give it all that you got" == sentence:
        await message.channel.send("Take your very best shot!")
    elif "take your very best shot" == sentence:
        await message.channel.send("He'll send it right back at ya for sure, yeah!")
    elif "give it all that you got take your very best shot" == sentence:
        await message.channel.send("He'll send it right back at ya for sure, yeah!")
    elif "hell send it right back at ya for sure" == sentence or "hell send it right back at you for sure yeah" == sentence or "hell send it right back at ya for sure yeah" == sentence or "hell send it right back at you for sure" == sentence:
        await message.channel.send("How can I help you, King Dedede?")
    elif "how can i help you king dedede" == sentence:
        await message.channel.send("I need a monster to clobber that there Kirby!")
    elif "i need a monster to clobber that there kirby" == sentence:
        await message.channel.send("That's what we do best at N.M.E.!")
    elif "thats what we do best at nme" == sentence:
        await message.channel.send("You'd better get it with a money-back guarantee!")
        kirbyThemeThird = True
    elif "youd better get it with a money back guarantee" == sentence:
        await message.channel.send("*plays trumpet*")
        kirbyThemeThird = True
    elif "saving the day" == sentence or "savin the day" == sentence:
        await message.channel.send("Kirby kirby kirby, he's here to stay!")
    elif "hes here to stay" == sentence:
        await message.channel.send("Don't be fooled by his size, you won't believe your eyes!")
        kirbyThemeFifth = True
    elif "dont be fooled by his size" == sentence:
        await message.channel.send("You won't believe your eyes!")
        kirbyThemeFifth = True
    elif "kirby" == sentence and kirbyThemeFifth:
        if(kirbyCount < 2):
            await message.channel.send("Kirby!")
            kirbyCount = kirbyCount + 1
        else:
            await message.channel.send("Kirby, Kirby, Kirby Kirby Kirby's the one!")
            kirbyThemeSixth = True
    elif "right back at ya" == sentence and kirbyThemeSixth:
        await message.channel.send("YEAH! *fist bump*")
        kirbyThemeFirst = False
        kirbyThemeSecond = False
        kirbyThemeThird = False
        kirbyThemeFourth = False
        kirbyThemeFifth = False
        kirbyCount = 0
        kirbyThemeSixth = False





client.run('NzUzMzc0MzEyMjM2NDQ5OTcy.X1lQgQ.xO_ylv1g726mw8u-s76QDZBVsJA')

