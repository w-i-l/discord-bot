import discord
from discord.ext import commands,tasks
import random
import asyncio


bot=commands.Bot(command_prefix="<k ")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Vezi medicamente pe <k h'))
    print('Bot is ready')

@bot.event
async def on_guild_join(guild):
    print('Bot has joined server: '+guild.name)

@bot.event
async def on_guild_remove(guild):
    print('Bot removed from: '+guild.name)

@bot.command()
async def sterge(ctx,numar=0):
    await ctx.channel.purge(limit=numar)

@bot.command()
async def s(ctx,member:discord.Member):
    async for mess in ctx.channel.history():
        if mess.author.id==member.id:
            await mess.delete()
            break

@bot.command(aliases=['h'])
async def hel(ctx):
    embed=discord.Embed(title='Ajutor pt saraci',description='Lista de alifii pt sclavi',color=discord.Colour.red())
    embed.add_field(name='Musamalizare cu numar //// sterge',value='Sterge ultimele n mesaje')
    embed.add_field(name='Musamalizare cu nume //// s',value='Sterge ultimul mesaj al prostului')
    embed.add_field(name='Fa o vizita la sclavi //// m',value='Ofera-i prietenului o excursie')
    embed.add_field(name='Duel in penis //// challange',value='Da pe fata')
    await ctx.send(embed=embed)


# @bot.event
# async def on_command_error(ctx,error):
#
#     if isinstance(error,commands.MissingRequiredArgument):
#         await ctx.send(ctx.message.author.mention+" trebuie un prost")
#     elif isinstance(error,commands.MemberNotFound):
#         await ctx.send("Da cu tag cumetre "+ctx.message.author.mention)
#     elif isinstance(error,commands.CommandNotFound):
#         await ctx.send("Nu pot asta, ce esti asa prost? "+ctx.message.author.mention)
#     elif isinstance(error,commands.CommandOnCooldown):
#         await ctx.send(ctx.message.author.mention+' suge-o din nou in: '+str(round(error.retry_after,2))+'s')
#     elif isinstance(error,asyncio.exceptions.TimeoutError):
#         await ctx.send('A expirat timpu cumetre')


@bot.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def m(ctx,member:discord.Member):

    message=ctx.message

    await s(ctx,ctx.message.author)

    channel=list(filter(lambda x: x.name=='sclav',ctx.guild.voice_channels))[0]

    if ctx.author.voice==None:

        embed=discord.Embed(description=message.author.mention+'Conecteza-te fiti-ar alifia de ras',color=discord.Colour.gold())
        await ctx.send(embed=embed)

    elif member.id == 442038246726172683:

        embed=discord.Embed(description=message.author.mention+' altadata, suge-o acum',color=discord.Colour.gold())
        await ctx.send(embed=embed)


    elif member.voice==None:

        embed=discord.Embed(description=message.author.mention+' nu poate fi babardit incearca alt fraier',color=discord.Colour.gold())
        await ctx.send(embed=embed)

    elif member.voice.channel==channel:

        embed=discord.Embed(description=message.author.mention+' si-o ia in cur schimba prostu',color=discord.Colour.gold())
        await ctx.send(embed=embed)
    else:

        await member.move_to(channel)
        embed=discord.Embed(description=message.author.mention+' este abuzat',color=discord.Colour.gold())
        await ctx.send(embed=embed)

@bot.command()
async def challange(ctx,member:discord.Member):

    em=discord.Embed(title=ctx.message.author.name,description='Te provoaca'+member.mention,color=discord.Colour.teal())
    em.add_field(name='Raspunde cu da/nu, y/n',value='daca nu esti pussy')

    await ctx.send(embed=em)

    accept= await bot.wait_for('message',check=lambda m:m.author==member and m.content in ['y','n','da','nu','DA','NU','Da','Nu','Y','N'],timeout=10.0)

    if accept.content.lower() in ['nu','n']:
        return
    elif accept==None:
        await(ctx,member)
    else:
        pass


    semne=['+','/','-','*']

    numar_1=random.randint(0,101)
    numar_2=random.randint(0,101)
    semn=random.choice(semne)

    if semn=='+':
        rezultat=numar_1+numar_2
    elif semn=='-':
        rezultat=numar_1-numar_2
    elif semn=='/':
        rezultat=round(numar_1/numar_2,2)
    elif semn=='*':
        rezultat=numar_1*numar_2



    embed=discord.Embed(title='Raspunde primul',description='Care este rezultatul?',color=discord.Colour.blue())
    embed.add_field(name=str(numar_1)+semn+str(numar_2),value='Maxim 2 zecimale')

    await ctx.send(embed=embed)

    msg=await bot.wait_for('message',check=lambda m:(m.author.id == ctx.message.author.id or m.author.id==member.id) and m.content==str(rezultat),timeout=30.0)

    if msg.author==ctx.message.author:

        sclav=member
    else:

        sclav=ctx.message.author

    print(rezultat)

    rol_sclav=ctx.guild.get_role(768533926602866709)
    elita=ctx.guild.get_role(749571862735880202)
    honor=ctx.guild.get_role(757864291922739280)

    if member.roles[-1].id==749571862735880202:
        await sclav.remove_roles(elita)
        await sclav.add_roles(rol_sclav)

        await m(ctx,sclav)

        await asyncio.sleep(20)



        await sclav.remove_roles(rol_sclav)
        await sclav.add_roles(elita)

    elif member.roles[-1].id==757864291922739280:
        await sclav.remove_roles(honor)
        await sclav.add_roles(rol_sclav)

        await m(ctx,sclav)

        await asyncio.sleep(5)

        await sclav.remove_roles(rol_sclav)
        await sclav.add_roles(honor)
    else:
            await sclav.add_roles(rol_sclav)

            await m(ctx,sclav)

            await asyncio.sleep(5)

            await sclav.remove_roles(rol_sclav)


    await ctx.send(sclav.mention+' a fost maltrafoxat')


# def checkTime():
#     lista_membri=[297423886570487808,298486584028954625,500403270888456214,626838359096164394,504737061480431628,264469327300919304,268840845766164481,
#             284426248841592833,297423029120794646,704253698183790672,264740601688227840,261058802516885504,465983314780749834,265841011777994754,
#             595701164629295105]
#     # This function runs periodically every 1 second
#     threading.Timer(1, checkTime).start()
#
#     now = datetime.now()
#
#     current_time = now.strftime("%H:%M:%S")
#
#     if current_time[3:5] in [str(x) for x in range(61) ] and current_time[6:]=='00':
#
#         ales=random.choice(lista_membri)
#
# checkTime()

@m.after_invoke
async def reset_cooldown(ctx):
    if ctx.message.author.id==442038246726172683:
        m.reset_cooldown(ctx)

@bot.command()
async def id(ctx):
    lista=[member.id for member in ctx.guild.members]
    print(lista)


#
# @bot.command()
# async def rol(ctx,member:discord.Member):
#     await ctx.send(member.roles[-1].id)
# @bot.command()
# async def voice(ctx,member:discord.Member):
#     if member.voice!=None:
#         print('connected')
#     else:
#         print('not connected')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

bot.run('NzY0ODIwNzk4OTg3ODI5MjQ4.X4L04A._V81ovzijeV7fO66k3FLlQLJNyw')
