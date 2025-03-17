from typing import List, Optional
import nextcord
from nextcord.components import SelectOption
from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord.utils import MISSING, get
from nextcord import Interaction
from nextcord import Intents
import sqlite3
import requests
import ro_py
import ro_py.utilities.errors
from ro_py.thumbnails import ThumbnailSize
from ro_py import Client
from ro_py.groups import Group
database = sqlite3.connect("discharges.db")
cursor = database.cursor()



client = Client()




bot = commands.Bot()




class SelectMenu(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Squadron 1",description=""),
            nextcord.SelectOption(label="Squadron 2",description=""),
            nextcord.SelectOption(label="Squadron 3",description=""),
            nextcord.SelectOption(label="Mariniers",description="")
            
        ]
        super().__init__(placeholder="What unit would you like to enlist in?",options=options,min_values=1,max_values=1)
    
    async def callback(self, interaction: Interaction):
        for member in interaction.guild.members:
            print(member.display_name)

class viewmenu(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())






@bot.slash_command()
async def remove(interaction:Interaction,robloxusername,reason):
    try:
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  robloxusername + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        mi = f.split("N")[1]
        moar = mi.split(",")[0]
        fina = moar.split(":")[1]
        name = fina.replace(fina[0],"")
        if robloxusername == name:
            listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'AND name LIKE " + "'" + robloxusername + "';").fetchall()
            if listOfTables == []:
                cursor.execute("CREATE TABLE IF NOT EXISTS " + robloxusername + "('reason')")
                cursor.execute("INSERT INTO " + robloxusername +  " VALUES" + "(" + "'" + str(reason) + "'" + ")")
                await interaction.response.send_message("User has been removed",ephemeral=True)
                database.commit()
            else:
                cursor.execute("INSERT INTO " + robloxusername +  " VALUES" + "(" + "'" + str(reason) + "'" + ")")
                await interaction.response.send_message("User has been removed",ephemeral=True)
                database.commit()
        else:
            await interaction.response.send_message("The account doesn't exist or it's typed wrong,try again...",ephemeral=True)
    except IndexError:
        await interaction.response.send_message("The account doesn't exist or it's typed wrong,try again...",ephemeral=True)
class Menu(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    @nextcord.ui.button(label="Removal History",style=nextcord.ButtonStyle.blurple)
    async def dischargelogs(self,button:nextcord.ui.Button,interaction:Interaction):
        with open("info.txt", "r") as readinfo:
            info = readinfo.read()
        listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'AND name LIKE " + "'" + info + "';").fetchall()
        if listOfTables == []:
            await interaction.response.send_message("There are no removes for this user",ephemeral=True)
        else:
            with open("discharges.txt","w",encoding="utf-8") as writingdat:
                for row in cursor.execute("SELECT * FROM " + info):
                    s = "".join(row)
                    writingdat.write("--------" + "\n" + s  + "\n" + "--------")
            with open("discharges.txt","r",encoding="utf-8") as readingdat:
                d = readingdat.read()
                embed = nextcord.Embed(title="Remove Logs")
                embed.add_field(name="",value=d,inline=True)
                await interaction.response.send_message(embed=embed,ephemeral=True)
    @nextcord.ui.button(label="Wipe Removals",style=nextcord.ButtonStyle.red)
    async def wipedischarges(self,button:nextcord.ui.Button,interaction:Interaction):
        with open("info.txt",'r') as inforead:
            data = inforead.read()
        listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'AND name LIKE " + "'" + data + "';").fetchall()
        if listOfTables == []:
            await interaction.response.send_message("There are no removes for this user",ephemeral=True)
        else:
            cursor.execute("DROP TABLE IF EXISTS " + data)
            await interaction.response.send_message("Removes have been wiped",ephemeral=True)
    @nextcord.ui.button(label="Friend List",style=nextcord.ButtonStyle.grey)
    async def friendlist(self,button:nextcord.ui.Button,interaction:Interaction):
        with open("info.txt","r",encoding="utf-8") as readinginfo:
            robloxusername = readinginfo.read()
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  robloxusername + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        d = f.split("UserId")[1]
        fina = d.split(",")[0]
        id = fina.split(":")[1]
        d = await  client.get_user(id)
        m = await d.get_friends()
        with open("friends.txt","w",encoding="utf-8") as writingfriends:
            for friend in m:
                writingfriends.write(friend.name + "\n")
        with open("friends.txt",'r',encoding="utf-8") as readingfriends:
            d = readingfriends.read()
            await interaction.response.send_message(d,ephemeral=True)
    @nextcord.ui.button(label="Group List",style=nextcord.ButtonStyle.green)
    async def grouplist(self,button:nextcord.ui.Button,interaction:Interaction):
        with open("info.txt",'r',encoding="utf-8") as readingdata:
            username = readingdata.read()
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  username + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        d = f.split("UserId")[1]
        fina = d.split(",")[0]
        id = fina.split(":")[1]
        user = await client.get_user(id)
        b = await user.get_groups()
        with open("groups.txt","w",encoding="utf-8") as writinggroups:
            for group in b:
                writinggroups.write(group.name + "\n")
        with open("groups.txt","r",encoding="utf-8") as read :
            groups = read.read()
            await interaction.response.send_message(groups,ephemeral=True)
    @nextcord.ui.button(label="Enlist User",style=nextcord.ButtonStyle.blurple)
    async def enlist(self,button:nextcord.ui.button,interaction:Interaction):
        with open("info.txt","r",encoding="utf-8") as readingdata:
            username = readingdata.read()

        view = viewmenu()
        await interaction.response.send_message(view=view,ephemeral=True)


























@bot.slash_command()
async def role(interaction:Interaction,user:nextcord.Member,rank:str):
    try:
        nick = user.nick
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  nick + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        mi = f.split("N")[1]
        moar = mi.split(",")[0]
        fina = moar.split(":")[1]
        name = fina.replace(fina[0],"")
        if nick == name:
            s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  nick + "&maxRows=1&startIndex=0")
            m = s.text
            p = "".join(m)
            f = p.replace(m[0],"")
            d = f.split("UserId")[1]
            fina = d.split(",")[0]
            id = fina.split(":")[1]
            client = Client("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5F9C64124EA2F994E62649115E852B1438384D035A29BCDABFF485F7371BD5ED66AA774D692EE47984810EE1529FF16D8A8F5FE3348FC8C2356B6D05793835DA025895AF25ED9144F1AD39AA849DF8909CD63DA0A3A445CC04B275E5A3A3BEE40717F992AF9CF594D07748026B505C7F5AFA8052717E40726A0EC60D2A7D8C7D121315F5CAB209CA3523BAD686124E21AE47B09603462E03F7EF2DCB96A45F9F521DB4B3F4E8D047CC98580CE5913CCB6B0B6135CF4FBF6A21DCB12CA2FFA49BBD7050EBDF001E48583916F66D897E72F53F6BB36497B447C63736B11BE6C2498288B0B31B23E4F60049BBD102A20CD2C255032CBE05F2D1F3CD49A05CC16FDA16C963702F2D5BE3D3CFFA13D8F6DB2CF71EF58BF3B3D48173D1990A7C24D8AE672DE3C4F19F86690405C567117FC78C381386F2316E6684C2D3148A7731BD31EC1E93815F8D2CABF93D4DEE85C8483EED9A25D62809C11B5750F7B9B5582E099FF184138542123DFAA1C4D916CA70A93FB9179B8CA44C34315E096A9999B74BC397934EB85597D919F560A29CDDB2643D21592582E8BC08EB92F2326D9D4BFB83A29336000FDF67EB0542828A7BD88396637FE2D429E374B921CB1331FB54735423BE568EE2956ABF4B8389CD81032389F8777989F2DFF74C61D7D6D5817F9E655ECFA84050BBDB3CC3FDC1B8C8CDBB0265990AE27A9A91D5CBD8A661ABC28B707DE4ACB8A9424FC5ED6F48902649F4BCE4F2DD0CA9278DC7421A523DBDDA2CCA444219F2742BC3C8AE0147C1D73886C6ED5273CE5D50A54D2067E646C24FB4D0B0CFB50D872F7FEE588F780FC0CBBB494B3164258DEF6378B14216B94C0CF9DC5690434CA4813DBBA5BD5D4C98ACC164272FAB78AF5CAD955ECA7AFC03804B78C829871F4E164E6CB401687E34243BE136169F282DD312B7E6598CBAE9D179186C304A")
            d = await  client.get_group(32747381)
            m = await d.get_member_by_id(id)

            if rank == "Rekruut":
                roleid = 99616618
            elif rank == "Soldat":
                roleid = 99616686
            elif rank == "Lance Korporaal":
                roleid = 99617024
            elif rank == "Korporaal":
                roleid = 99617033
            elif rank == "Serjent":
                roleid = 99617064
            elif rank == "Serjent Majeur":
                roleid = 99617141
            elif rank == "Unterlieutenant":
                roleid = 99617277
            elif rank == "Oberlieutenant":
                roleid = 99617278
            elif rank == "Hauptmann":
                roleid = 99617289
            elif rank == "Major":
                roleid = 99617302
            elif rank == "Oberstlieutenant":
                roleid = 99617324 
            
            await m.setrank(roleid)
            await interaction.response.send_message("The user has been roled",ephemeral=True)
        else:
            await interaction.response.send_message("The user doesn't exist or you typed it wrong...",ephemeral=True)
    except ro_py.utilities.errors.NotFound:
        await interaction.response.send_message("The user is not in the group",ephemeral=True)
    except TypeError:
        await interaction.response.send_message("Couldn't find the user make sure the user is verified",ephemeral=True)
    except ro_py.utilities.errors.Forbidden:
        await interaction.response.send_message("You have no permission to role this user in the group",ephemeral=True)  
    except UnboundLocalError:
        await interaction.response.send_message("The rank doesn't exist in the group",ephemeral=True)      

@bot.slash_command()
async def removeroles(interaction:Interaction,user:nextcord.Member):
    try:
        nick = user.nick
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  nick + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        mi = f.split("N")[1]
        moar = mi.split(",")[0]
        fina = moar.split(":")[1]
        name = fina.replace(fina[0],"")
        if nick == name:
            s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  nick + "&maxRows=1&startIndex=0")
            m = s.text
            p = "".join(m)
            f = p.replace(m[0],"")
            d = f.split("UserId")[1]
            fina = d.split(",")[0]
            id = fina.split(":")[1]
            client = Client("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5F9C64124EA2F994E62649115E852B1438384D035A29BCDABFF485F7371BD5ED66AA774D692EE47984810EE1529FF16D8A8F5FE3348FC8C2356B6D05793835DA025895AF25ED9144F1AD39AA849DF8909CD63DA0A3A445CC04B275E5A3A3BEE40717F992AF9CF594D07748026B505C7F5AFA8052717E40726A0EC60D2A7D8C7D121315F5CAB209CA3523BAD686124E21AE47B09603462E03F7EF2DCB96A45F9F521DB4B3F4E8D047CC98580CE5913CCB6B0B6135CF4FBF6A21DCB12CA2FFA49BBD7050EBDF001E48583916F66D897E72F53F6BB36497B447C63736B11BE6C2498288B0B31B23E4F60049BBD102A20CD2C255032CBE05F2D1F3CD49A05CC16FDA16C963702F2D5BE3D3CFFA13D8F6DB2CF71EF58BF3B3D48173D1990A7C24D8AE672DE3C4F19F86690405C567117FC78C381386F2316E6684C2D3148A7731BD31EC1E93815F8D2CABF93D4DEE85C8483EED9A25D62809C11B5750F7B9B5582E099FF184138542123DFAA1C4D916CA70A93FB9179B8CA44C34315E096A9999B74BC397934EB85597D919F560A29CDDB2643D21592582E8BC08EB92F2326D9D4BFB83A29336000FDF67EB0542828A7BD88396637FE2D429E374B921CB1331FB54735423BE568EE2956ABF4B8389CD81032389F8777989F2DFF74C61D7D6D5817F9E655ECFA84050BBDB3CC3FDC1B8C8CDBB0265990AE27A9A91D5CBD8A661ABC28B707DE4ACB8A9424FC5ED6F48902649F4BCE4F2DD0CA9278DC7421A523DBDDA2CCA444219F2742BC3C8AE0147C1D73886C6ED5273CE5D50A54D2067E646C24FB4D0B0CFB50D872F7FEE588F780FC0CBBB494B3164258DEF6378B14216B94C0CF9DC5690434CA4813DBBA5BD5D4C98ACC164272FAB78AF5CAD955ECA7AFC03804B78C829871F4E164E6CB401687E34243BE136169F282DD312B7E6598CBAE9D179186C304A")
            d = await  client.get_group(32747381)
            m = await d.get_member_by_id(id)
            await m.setrank(99615873)
            await interaction.response.send_message("User has been deroled succesfully",ephemeral=True)
    except TypeError:
        await interaction.response.send_message("Couldn't find the user based off their discord,make sure they are verified",ephemeral=True)
    except ro_py.utilities.errors.NotFound:
        await interaction.response.send_message("Couldn't find the user in the group",ephemeral=True)
    
        


@bot.slash_command()
async def info(interaction:Interaction,robloxusername):
    try:
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  robloxusername + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        mi = f.split("N")[1]
        moar = mi.split(",")[0]
        fina = moar.split(":")[1]
        name = fina.replace(fina[0],"")
        if robloxusername == name:
            s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  robloxusername + "&maxRows=1&startIndex=0")
            m = s.text
            p = "".join(m)
            f = p.replace(m[0],"")
            d = f.split("UserId")[1]
            fina = d.split(",")[0]
            id = fina.split(":")[1]
            user = await client.get_user(id)
            d = await user.thumbnails.get_avatar_image(size=ThumbnailSize.size_420x420)
            m = user.id
            f = user.display_name
            is_banned = user.is_banned
            something  = user.description
            created = user.created
            follower_count = await user.get_followers_count()
            group = await client.get_group(32747381)
            members = await group.get_member_by_id(m)
            rank  = members.role.name
            with open("info.txt","w") as writingdata:
                writingdata.write(robloxusername)
                embed = nextcord.Embed(title="Details about " + robloxusername)
                embed.set_image(url=d)
                embed.add_field(name="Roblox ID",value=m)
                embed.add_field(name="Display Name",value=f)
                embed.add_field(name="Is banned",value=is_banned)
                embed.add_field(name="Description",value=something)
                embed.add_field(name="Created",value=created.year)
                embed.add_field(name="Follower Count",value=follower_count)
                embed.add_field(name="Rank",value=rank)
                view = Menu()
                await interaction.response.send_message(embed=embed,view=view,ephemeral=True)

        else:
           await interaction.response.send_message("The account doesn't exist or it's typed wrong,try again...",ephemeral=True)
    except IndexError:
        await interaction.response.send_message("The account doesn't exist or it's typed wrong,try again...",ephemeral=True)
    except ro_py.utilities.errors.NotFound:
        if robloxusername == name:
            s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  robloxusername + "&maxRows=1&startIndex=0")
            m = s.text
            p = "".join(m)
            f = p.replace(m[0],"")
            d = f.split("UserId")[1]
            fina = d.split(",")[0]
            id = fina.split(":")[1]
            user = await client.get_user(id)
            d = await user.thumbnails.get_avatar_image(size=ThumbnailSize.size_420x420)
            m = user.id
            f = user.display_name
            is_banned = user.is_banned
            something  = user.description
            created = user.created
            follower_count = await user.get_followers_count()
            with open("info.txt","w") as writingdata:
                writingdata.write(robloxusername)
                embed2 = nextcord.Embed(title="Details about " + robloxusername)
                embed2.set_image(url=d)
                embed2.add_field(name="Roblox ID",value=m)
                embed2.add_field(name="Is banned",value=is_banned)
                embed2.add_field(name="Description",value=something)
                embed2.add_field(name="Created",value=created.year)
                embed2.add_field(name="Follower Count",value=follower_count)
                embed2.add_field(name="Rank",value="Couldn't find the user in the group")
                view = Menu()
                await interaction.response.send_message(embed=embed2,view=view,ephemeral=True)
        else:
            await interaction.response.send_message("The account doesn't exist or it's typed wrong,try again...",ephemeral=True)



@bot.slash_command()
async def test(interaction:Interaction):
    guild = interaction.guild
    d = nextcord.utils.find(1095878682578534491,guild.members)
    print(d)
bot.run("KEY HERE")
