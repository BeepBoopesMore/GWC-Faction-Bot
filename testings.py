import roblox 
from roblox     import Client
from roblox import groups




import asyncio
import ro_py
from ro_py import Client
import roblox

client = Client()
d = roblox.Client()
async def main():
    m  = await  d.get_user_by_username("BottleTower")
    id = m.id
    b = await client.get_user(id)
    print(b.description)
asyncio.get_event_loop().run_until_complete(main())