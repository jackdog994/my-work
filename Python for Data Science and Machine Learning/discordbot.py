import discord

from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('pdb!','pdb.'), description="Pierian Data Common-Questions Bot")

@bot.listen()
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("pdb!help to see all commands"), afk=False)

@bot.command()
async def python(ctx):
    """Informs on how to format your code within Discord with Python formatting.
    Makes it much easier for others to read and help!"""
    await ctx.send("Please prefix your code with ```python")
    await ctx.send(" and suffix it with ``` e.g.")
    await ctx.send("def my_cool_func():"
                   "\n    print('formatting is cool')"
                   "\nbecomes:"
                   "\n```python"
                   "\ndef my_cool_func():"
                   "\n    print('formatting is cool')```")

@bot.command()
async def dict(ctx):
    """Informs on dictionary format, indexing and key/value selection"""
    await ctx.send("Dictionaries are a data object type composed of key:value pairs, e.g.```python\n"
                   "my_dict = {'key1':'value1','key2':'value2'}```"
                   "You can retrieve the keys by ```python\n"
                   "my_dict.keys()```"
                   "You can retrieve the values by ```python\n"
                   "my_dict.values()```"
                   "Retrieving a specific value can be done either by key or index, e.g. ```python\n"
                   "my_dict[1]``` or```python\n"
                   "my_dict['key2']```"
                   "will both return```python\n"
                   "'value2'```")

@bot.command()
async def list(ctx):
    """Informs on .append(), .pop() and .sort() methods"""
    await ctx.send("Common list methods, my_list for each of the below:```python\n"
                   "my_list = [1,2,3]```"
                   ".append(object) adds the object to the end of the list:```python\n"
                   "my_list.append(4)\n"
                   "my_list = [1,2,3,4]```"
                   ".pop(index_position) 'pops' the item from the list, removing it```python\n"
                   "my_list.pop(2)\nmy_list = [1,2,4]```"
                   ".sort(reverse=bool) sorts the list ascendingly. Include reverse=True for descending sort. Default is True so does not need to be included for ascending sort.```python\n"
                   "my_list.sort(reverse=True)\n"
                   "my_list = [3,2,1]```")

@bot.command()
async def string_formats(ctx):
    """Informs on .capitalize(), .title(), .upper() and .lower() methods"""
    await ctx.send("Common string format operators, my_string for each of the below:```python\n"
                   "my_string = 'this is my sTrInG'```"
                   ".capitalize() Capitalises the first letter of the string, all others lowercase:```python\n"
                   "my_string.capitalize() = 'This is my string'```"
                   ".title() Capitalises the first letter of every word, all others lowercase:```python\n"
                   "my_string.title() = 'This Is My String'```"
                   ".upper() Capitalises every letter in the string, all uppercase```python\n"
                   "my_string.upper() = 'THIS IS MY STRING'```"
                   ".lower() Every letter in the string lowercase```python\n"
                   "my_string.lower()='this is my string'```")

@bot.command()
async def string_manipulators(ctx):
    """Informs on .startswith(), .endswith(), .replace(),  .split() and .join() methods"""
    await ctx.send("Common string manipulators, my_string for each of the below:```python\n"
                   "my_string = 'this is my sTrInG'```"
                   ".startswith(string) .endswith(string) returns a boolean value for whether the string starts or ends with string```python\n"
                   "my_string.endswith('G') = True```"
                   ".replace(replacethis,withthis) replaces the first argument with the second```python\n"
                   "my_string.replace(' ','*') = 'this*is*my*sTrInG'```"
                   ".split(string) creates a list of the elements in your string, split by string```python\n"
                   "my_string.split(' ') = ['this', 'is', 'my', 'sTrInG']```"
                   "string.join(iterable) = joins the elements in the iterable together to form one string, each element seperated by string```python\n"
                   "split_string = my_string.split(' ')\ns = ' '\ns.join(split_string) = 'this is my sTrInG'```")

@bot.command()
async def list_comp(ctx):
    """Informs on list comprehensions"""
    await ctx.send("List comprehension enables you to iterate through the objects in a list on one line instead of using a for loop. They take the format:```python\n"
                   "[operator for object in iterable]```e.g. in the case where ```python\n"
                   "my_list = [1,2,3]\n[i*2 for i in my_list] = [2,4,6]```")

@bot.command()
async def suggestions(ctx):
    """If you have any suggestions for further commands to add please @noneideticmemory"""
    await ctx.send("If you have any suggestions for further commands to add please @noneideticmemory")

bot.run("NTA4MzI0MjQ2MjUxMTEwNDIy.Dr9lnw.wNSMkF7aMmMnDBkqnM8X6vT0FR4")