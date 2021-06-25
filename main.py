@client.command()
async def url_kwarg(ctx):
    url_kwarg = discord.Embed(url = "https://www.python.org/", title = "URL KWARG TEST", color = discord.Color.green())
    await ctx.send(embed=url_kwarg)
