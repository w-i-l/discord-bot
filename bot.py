import discord
from discord.ext import commands,tasks

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


@bot.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def m(ctx,member:discord.Member):

    await s(ctx,ctx.message.author)
    channel=list(filter(lambda x: x.name=='sclav',ctx.guild.voice_channels))[0]


    if member.id == 442038246726172683:

        await ctx.send(ctx.message.author.mention+"  altadata, suge-o acum")

    elif member.voice==None:
        await ctx.send(member.mention+' nu poate fi babardit, incearca alt ratat')

    elif member.voice.channel==channel:
        await ctx.send(member.mention+' si-o ia in cur, schimba prostu')

    else:

        await member.move_to(channel)
        await ctx.send(member.mention+' este abuzat!')


@m.after_invoke
async def reset_cooldown(ctx):
    if ctx.message.author.id==442038246726172683:
        m.reset_cooldown(ctx)



bot.run('NzY0ODIwNzk4OTg3ODI5MjQ4.X4L04A.re1tzYNV8AOOEq6ZBEuTr1M4J5k')
