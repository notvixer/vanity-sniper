import aiosonic, tasksio, asyncio
from aiosonic import HTTPClient as ClientSession

class Sniper:
  def __init__(self, token: str, vanity: str, target_guild: int, guild: int, amt_loop: int):
    self.token = token
    self.vanity_to_steal = vanity
    self.target_guild = target_guild
    self.guild = guild
    self.amount_loop = amt_loop
  
  async def remove_vanity(self, session):
    trying = await session.patch(f"https://discord.com/api/v10/guilds/{self.target_guild}/vanity-url", json={"Authorization": self.token,"code": "cityofhomos"})
    
    success = await session.patch(f"https://discord.com/api/v10/guilds/{self.guild}/vanity-url", json={"Authorization": self.token, "code": self.vanity_to_steal})
    
    if trying.status_code in (200, 201, 204):
      print("changed the vanity of the target guild")
    else:
      print("couldn't change it, sucks to be you")
      
    if success.status_code in (200, 201, 204):
      print("changed ur guilds' vanity to", self.vanity_to_steal)
    else:
      print("couldn't change ur guilds' vanity, sucks to be you")
 
 
  async def main(self):
    if self.amount_loop == None:
      async with ClientSession() as session:
        async with tasksio.TaskPool(2000) as pool:
          await pool.put(remove_vanity(session))
    elif self.amount_loop > 0:
      async with ClientSession() as session:
        async with tasksio.TaskPool(2999) as pool:
          for i in range(self.amount_loop):
            await pool.put(remove_vanity(session))
    else:
      async with ClientSession() as session:
        async with tasksio.TaskPool(2000) as pool:
          await pool.put(remove_vanity(session))



TOKEN = input("User Token =>")
VANITY = input("Target Vanity =>")
TARGET_GUILD = input("Target Guild Id =>")
GUILD = input("Your Guild Id => ")
AMT_LOOP = input("Amount Of Times To Retry =>")

sniper = Sniper(token=TOKEN, vanity=VANITY, target_guild=TARGET_GUILD, guild=GUILD, amt_loop=AMT_LOOP)
asyncio.get_event_loop().run_until_complete(sniper.main())
