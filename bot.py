import discord
from discord.ext import commands,tasks
import random
import asyncio
from datetime import datetime


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

    s_m_k=list(filter(lambda x: x.id==769870819881910302,ctx.message.author.guild.channels))[0]
    current_time = datetime.now().strftime("%H:%M:%S")

    if ctx.channel.id==770567200360759317:

        embed=discord.Embed(description=ctx.message.author.mention+' a incercat sa stearga '+str(numar)+' mesaje pe canalul '+ctx.message.channel.name+' la ora '+current_time,color=discord.Colour.red())
        await s_m_k.send(embed=embed)
        return

    else:

        await ctx.channel.purge(limit=numar)
        embed=discord.Embed(description=ctx.message.author.mention+' a sters '+str(numar)+' mesaje pe canalul '+ctx.message.channel.name+' la ora '+current_time,color=discord.Colour.red())
        await s_m_k.send(embed=embed)

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


@bot.event
async def on_command_error(ctx,error):

    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(ctx.message.author.mention+" trebuie un prost")
    elif isinstance(error,commands.MemberNotFound):
        await ctx.send("Da cu tag cumetre "+ctx.message.author.mention)
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("Nu pot asta, ce esti asa prost? "+ctx.message.author.mention)
    elif isinstance(error,commands.CommandOnCooldown):
        await ctx.send(ctx.message.author.mention+' suge-o din nou in: '+str(round(error.retry_after,2))+'s')
    elif isinstance(error,asyncio.exceptions.TimeoutError):
        await ctx.send('A expirat timpu cumetre')


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
        embed=discord.Embed(description=member.mention+' este abuzat',color=discord.Colour.gold())
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


    semne=['+','-','*']
    
    numar_1=random.randint(0,1001)
    numar_2=random.randint(0,1001)
    semn=random.choice(semne)
    
    if semn=='+':
        rezultat=numar_1+numar_2
    elif semn=='-':
        rezultat=numar_1-numar_2
    elif semn=='*':
        numar_1=random.randint(0,31)
        numar_2=random.randint(0,31)
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

        await asyncio.sleep(20)

        await sclav.remove_roles(rol_sclav)
        await sclav.add_roles(honor)

    else:
            await sclav.add_roles(rol_sclav)

            await m(ctx,sclav)

            await asyncio.sleep(20)

            await sclav.remove_roles(rol_sclav)


    await ctx.send(sclav.mention+' a fost maltrafoxat')




@m.after_invoke
async def reset_cooldown(ctx):
    if ctx.message.author.id==442038246726172683:
        m.reset_cooldown(ctx)

# @bot.command()
# async def id(ctx):
#     lista=[member.id for member in ctx.guild.members]
#     print(lista)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(int(bot.latency*1000)))

################################################################ registru conectari
@bot.event
async def on_voice_state_update(member, before, after):


    s_m_k=list(filter(lambda x: x.id==769870819881910302,member.guild.channels))[0]

    current_time = datetime.now().strftime("%H:%M:%S")

    if before.channel is None and after.channel is not None and before.self_mute!=True and after.self_mute!=True :

        embed=discord.Embed(description=member.mention+'s-a conectat la '+after.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.channel is not None and after.channel is  None and before.self_mute!=True and after.self_mute!=True:

        embed=discord.Embed(description=member.mention+'s-a deconectat de la '+before.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.channel is not None and after.channel is  not None and ((before.self_mute!=True and after.self_mute!=True) or (before.self_mute!=False and after.self_mute!=False)):

        if before.channel.name==after.channel.name:

            variabila='deaf/mute/stream'if member.voice.deaf==True or member.voice.mute==True else 'undeaf/unmute/unstream'

            embed=discord.Embed(description=member.mention+'si-a luat '+variabila+' pe '+before.channel.name+' la '+after.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        else:

            embed=discord.Embed(description=member.mention+'s-a mutat de la '+before.channel.name+' la '+after.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.self_deaf==False and after.self_deaf==True:

        embed=discord.Embed(description=member.mention+' si-a dat deaf pe canalul '+before.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.self_mute==False and after.self_mute==True:

        embed=discord.Embed(description=member.mention+' s-a amutit pe canalul '+before.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.self_deaf==True and after.self_deaf==False:

        embed=discord.Embed(description=member.mention+' si-a dat undeaf pe canalul '+before.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)

    elif before.self_mute==True and after.self_mute==False:

        embed=discord.Embed(description=member.mention+' s-a dezamutit pe canalul '+before.channel.name+' la ora '+current_time,color=discord.Colour.dark_blue())
        await s_m_k.send(embed=embed)




bot.run('NzY0ODIwNzk4OTg3ODI5MjQ4.X4L04A.4XS-fwocZke9B0dcW2BLpoEpBVc')
