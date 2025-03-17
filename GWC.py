from typing import List, Optional
import nextcord
from nextcord.components import SelectOption
from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord.utils import MISSING, get
from nextcord import Interaction
from nextcord import Intents
import nextcord.errors
import ro_py
import sqlite3
import requests
import roblox.utilities
from ro_py import groups
from ro_py.thumbnails import ThumbnailSize
from ro_py import Client
import ro_py.utilities.errors
from nextcord import Member
import roblox.utilities.exceptions
import roblox
database = sqlite3.connect("discharges.db")
cursor = database.cursor()



client = Client()
clientroblox = roblox.Client()





bot = commands.Bot()




class SelectMenu(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Squadron 1",description=""),
            nextcord.SelectOption(label="Squadron 2",description=""),
            nextcord.SelectOption(label="Squadron 3",description=""),
            nextcord.SelectOption(label="Mariniers",description="")
            
        ]

        super().__init__(placeholder="What unit would you like to enlist in?",options=options,max_values=1)
    async def callback(self, interaction: Interaction) -> None:
        with open("discordid.txt","r",encoding="utf-8") as readingdata:
            id = readingdata.read()
        with open("info.txt","r",encoding="utf-8") as readinguser:
            user = readinguser.read()
        userdiscord = await interaction.guild.fetch_member(id)
        units = self._selected_values
        for unit in units:
            s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  user + "&maxRows=1&startIndex=0")
            m = s.text
            p = "".join(m)
            f = p.replace(m[0],"")
            d = f.split("UserId")[1]
            fina = d.split(",")[0]
            id = fina.split(":")[1]
            clients = Client("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5F9C64124EA2F994E62649115E852B1438384D035A29BCDABFF485F7371BD5ED66AA774D692EE47984810EE1529FF16D8A8F5FE3348FC8C2356B6D05793835DA025895AF25ED9144F1AD39AA849DF8909CD63DA0A3A445CC04B275E5A3A3BEE40717F992AF9CF594D07748026B505C7F5AFA8052717E40726A0EC60D2A7D8C7D121315F5CAB209CA3523BAD686124E21AE47B09603462E03F7EF2DCB96A45F9F521DB4B3F4E8D047CC98580CE5913CCB6B0B6135CF4FBF6A21DCB12CA2FFA49BBD7050EBDF001E48583916F66D897E72F53F6BB36497B447C63736B11BE6C2498288B0B31B23E4F60049BBD102A20CD2C255032CBE05F2D1F3CD49A05CC16FDA16C963702F2D5BE3D3CFFA13D8F6DB2CF71EF58BF3B3D48173D1990A7C24D8AE672DE3C4F19F86690405C567117FC78C381386F2316E6684C2D3148A7731BD31EC1E93815F8D2CABF93D4DEE85C8483EED9A25D62809C11B5750F7B9B5582E099FF184138542123DFAA1C4D916CA70A93FB9179B8CA44C34315E096A9999B74BC397934EB85597D919F560A29CDDB2643D21592582E8BC08EB92F2326D9D4BFB83A29336000FDF67EB0542828A7BD88396637FE2D429E374B921CB1331FB54735423BE568EE2956ABF4B8389CD81032389F8777989F2DFF74C61D7D6D5817F9E655ECFA84050BBDB3CC3FDC1B8C8CDBB0265990AE27A9A91D5CBD8A661ABC28B707DE4ACB8A9424FC5ED6F48902649F4BCE4F2DD0CA9278DC7421A523DBDDA2CCA444219F2742BC3C8AE0147C1D73886C6ED5273CE5D50A54D2067E646C24FB4D0B0CFB50D872F7FEE588F780FC0CBBB494B3164258DEF6378B14216B94C0CF9DC5690434CA4813DBBA5BD5D4C98ACC164272FAB78AF5CAD955ECA7AFC03804B78C829871F4E164E6CB401687E34243BE136169F282DD312B7E6598CBAE9D179186C304A")
            group = await clients.get_group(32747381)
            if unit == "Squadron 1":
                s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  user + "&maxRows=1&startIndex=0")
                m = s.text
                p = "".join(m)
                f = p.replace(m[0],"")
                d = f.split("UserId")[1]
                fina = d.split(",")[0]
                id = fina.split(":")[1]
                desires_role = get(interaction.guild.roles,name="1st Squadron")
                desired_role2 =  get(interaction.guild.roles,name="Seaman")
                clients = Client("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5F9C64124EA2F994E62649115E852B1438384D035A29BCDABFF485F7371BD5ED66AA774D692EE47984810EE1529FF16D8A8F5FE3348FC8C2356B6D05793835DA025895AF25ED9144F1AD39AA849DF8909CD63DA0A3A445CC04B275E5A3A3BEE40717F992AF9CF594D07748026B505C7F5AFA8052717E40726A0EC60D2A7D8C7D121315F5CAB209CA3523BAD686124E21AE47B09603462E03F7EF2DCB96A45F9F521DB4B3F4E8D047CC98580CE5913CCB6B0B6135CF4FBF6A21DCB12CA2FFA49BBD7050EBDF001E48583916F66D897E72F53F6BB36497B447C63736B11BE6C2498288B0B31B23E4F60049BBD102A20CD2C255032CBE05F2D1F3CD49A05CC16FDA16C963702F2D5BE3D3CFFA13D8F6DB2CF71EF58BF3B3D48173D1990A7C24D8AE672DE3C4F19F86690405C567117FC78C381386F2316E6684C2D3148A7731BD31EC1E93815F8D2CABF93D4DEE85C8483EED9A25D62809C11B5750F7B9B5582E099FF184138542123DFAA1C4D916CA70A93FB9179B8CA44C34315E096A9999B74BC397934EB85597D919F560A29CDDB2643D21592582E8BC08EB92F2326D9D4BFB83A29336000FDF67EB0542828A7BD88396637FE2D429E374B921CB1331FB54735423BE568EE2956ABF4B8389CD81032389F8777989F2DFF74C61D7D6D5817F9E655ECFA84050BBDB3CC3FDC1B8C8CDBB0265990AE27A9A91D5CBD8A661ABC28B707DE4ACB8A9424FC5ED6F48902649F4BCE4F2DD0CA9278DC7421A523DBDDA2CCA444219F2742BC3C8AE0147C1D73886C6ED5273CE5D50A54D2067E646C24FB4D0B0CFB50D872F7FEE588F780FC0CBBB494B3164258DEF6378B14216B94C0CF9DC5690434CA4813DBBA5BD5D4C98ACC164272FAB78AF5CAD955ECA7AFC03804B78C829871F4E164E6CB401687E34243BE136169F282DD312B7E6598CBAE9D179186C304A")
                group = await clients.get_group(32747381)
                d = await group.get_member_by_id(id)
                await d.setrank(101401672)
                await userdiscord.add_roles(desires_role)
                await userdiscord.add_roles(desired_role2)
                embed1 = nextcord.Embed(title=user + " has been enlisted in " + unit,color=nextcord.Color.random())
                return await interaction.response.send_message(embed=embed1,ephemeral=True)
            elif unit == "Squadron 2":
                desires_role3 = get(interaction.guild.roles,name="2nd Squadron")
                desired_role4 =  get(interaction.guild.roles,name="Seaman")
                await userdiscord.add_roles(desires_role3)
                await userdiscord.add_roles(desired_role4)
                m = await group.get_member_by_id(id)
                await m.setrank(101401672)
                embed2 = nextcord.Embed(title=user + " has been enlisted in" + unit,color=nextcord.Color.blue())
                return await interaction.response.send_message(embed=embed2,ephemeral=True)
            elif unit == "Squadron 3":
                desires_role5 = get(interaction.guild.roles,name="3rd Squadron")
                desired_role6 =  get(interaction.guild.roles,name="Seaman")
                await userdiscord.add_roles(desires_role5)
                await userdiscord.add_roles(desired_role6)
                lol = await group.get_member_by_id(id)
                await lol.setrank(101401672)
                embed3 = nextcord.Embed(title=user + " has been enlisted in" + unit,color=nextcord.Color.blue())
                return await interaction.response.send_message(embed=embed3,ephemeral=True)
            elif unit == "Mariniers":
                desires_role7 = get(interaction.guild.roles,name="Korps Mariniers")
                desired_role8 =  get(interaction.guild.roles,name="Seaman")
                await userdiscord.add_roles(desires_role7)
                await userdiscord.add_roles(desired_role8)
                lols = await group.get_member_by_id(id)
                await lols.setrank(101401672)
                embed4 = nextcord.Embed(title=user + " has been enlisted in" + unit,color=nextcord.Color.blue())
                return await interaction.response.send_message(embed=embed4,ephemeral=True)
class viewmenu(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectMenu())

class SelectRoles(nextcord.ui.Select):
    def __init__(self) -> None:
        options = [
            nextcord.SelectOption(label="Seaman",description=""),
            nextcord.SelectOption(label="Able Seaman",description=""),
            nextcord.SelectOption(label="Petty Officer",description=""),
            nextcord.SelectOption(label="Chief Petty Officer",description=""),
            nextcord.SelectOption(label="Warrant Officer",description=""),
            nextcord.SelectOption(label="Ensign",description=""),
            nextcord.SelectOption(label="Sub-Lieutenant",description=""),
            nextcord.SelectOption(label="Lieutenant",description=""),
            nextcord.SelectOption(label="Lieutenant Commander",description=""),
            nextcord.SelectOption(label="Commander",description=""),
            nextcord.SelectOption(label="Captain",description=""),
            nextcord.SelectOption(label="Commodore",description=""),
            nextcord.SelectOption(label="Rear Admiral",description=""),
            nextcord.SelectOption(label="Admiral",description="")



        ]
        super().__init__(placeholder="Please select the rank",max_values=1,options=options)
    async def callback(self, interaction: Interaction) -> None:
        with open("info.txt","r",encoding="utf-8") as readingdata:
            user = readingdata.read()
        with  open("discordid.txt","r",encoding="utf-8") as readingid:
            id = readingid.read()
        userdiscord =  await interaction.guild.fetch_member(id)
        values = self._selected_values
        s = requests.get("https://www.roblox.com/search/users/results?keyword="  +  user + "&maxRows=1&startIndex=0")
        m = s.text
        p = "".join(m)
        f = p.replace(m[0],"")
        d = f.split("UserId")[1]
        fina = d.split(",")[0]
        id = fina.split(":")[1]
        client = Client("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5F9C64124EA2F994E62649115E852B1438384D035A29BCDABFF485F7371BD5ED66AA774D692EE47984810EE1529FF16D8A8F5FE3348FC8C2356B6D05793835DA025895AF25ED9144F1AD39AA849DF8909CD63DA0A3A445CC04B275E5A3A3BEE40717F992AF9CF594D07748026B505C7F5AFA8052717E40726A0EC60D2A7D8C7D121315F5CAB209CA3523BAD686124E21AE47B09603462E03F7EF2DCB96A45F9F521DB4B3F4E8D047CC98580CE5913CCB6B0B6135CF4FBF6A21DCB12CA2FFA49BBD7050EBDF001E48583916F66D897E72F53F6BB36497B447C63736B11BE6C2498288B0B31B23E4F60049BBD102A20CD2C255032CBE05F2D1F3CD49A05CC16FDA16C963702F2D5BE3D3CFFA13D8F6DB2CF71EF58BF3B3D48173D1990A7C24D8AE672DE3C4F19F86690405C567117FC78C381386F2316E6684C2D3148A7731BD31EC1E93815F8D2CABF93D4DEE85C8483EED9A25D62809C11B5750F7B9B5582E099FF184138542123DFAA1C4D916CA70A93FB9179B8CA44C34315E096A9999B74BC397934EB85597D919F560A29CDDB2643D21592582E8BC08EB92F2326D9D4BFB83A29336000FDF67EB0542828A7BD88396637FE2D429E374B921CB1331FB54735423BE568EE2956ABF4B8389CD81032389F8777989F2DFF74C61D7D6D5817F9E655ECFA84050BBDB3CC3FDC1B8C8CDBB0265990AE27A9A91D5CBD8A661ABC28B707DE4ACB8A9424FC5ED6F48902649F4BCE4F2DD0CA9278DC7421A523DBDDA2CCA444219F2742BC3C8AE0147C1D73886C6ED5273CE5D50A54D2067E646C24FB4D0B0CFB50D872F7FEE588F780FC0CBBB494B3164258DEF6378B14216B94C0CF9DC5690434CA4813DBBA5BD5D4C98ACC164272FAB78AF5CAD955ECA7AFC03804B78C829871F4E164E6CB401687E34243BE136169F282DD312B7E6598CBAE9D179186C304A")
        d = await  client.get_group(32747381)
        m = await d.get_member_by_id(id)
        for value in values:
            if value == "Seaman":
                rankid = 101401672
                role1  =  get(interaction.guild.roles,name="Seaman")
                await m.setrank(rankid)
                await userdiscord.add_roles(role1)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Able Seaman":
                rankid = 99615873
                role2  =  get(interaction.guild.roles,name="Able Seaman")
                await m.setrank(rankid)
                await userdiscord.add_roles(role2)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Petty Officer":
                rankid = 99616618
                role3  =  get(interaction.guild.roles,name="Petty Officer")
                await userdiscord.add_roles(role3)
                await m.setrank(rankid)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Chief Petty Officer":
                rankid = 99616686
                role4 = get(interaction.guild.roles,name="Chief Petty Officer")
                await userdiscord.add_roles(role4)
                await m.setrank(rankid)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Warrant Officer":
                rankid = 99617024
                role5 = get(interaction.guild.roles,name="Warrant Officer")
                await userdiscord.add_roles(role5)
                await m.setrank(rankid)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Ensign":
                rankid = 99617033
                role6 = get(interaction.guild.roles,name="Ensign")
                await userdiscord.add_roles(role6)
                await m.setrank(rankid)
                await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Sub-Lieutenant":
               rankid = 99617064
               role7 = get(interaction.guild.roles,name="Sub-Lieutenant")
               await userdiscord.add_roles(role7)
               await m.setrank(rankid)
               await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Lieutenant":
               rankid = 99617141
               role8 = get(interaction.guild.roles,name="Lieutenant")
               await m.setrank(rankid)
               await userdiscord.add_roles(role8)
               await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Lieutenant Commander":
               rankid = 99617277
               role9 = get(interaction.guild.roles,name="Lieutenant Commander")
               await userdiscord.add_roles(role9)
               await m.setrank(rankid)
               await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Commander":
              rankid = 99617278
              role10 = get(interaction.guild.roles,name="Commander")
              await userdiscord.add_roles(role10)
              await m.setrank(rankid)
              await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Captain":
              rankid = 99617289
              role11 = get(interaction.guild.roles,name="Captain")
              await userdiscord.add_roles(role11)
              await m.setrank(rankid)
              await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Commodore":
              rankid = 99617302
              role12 = get(interaction.guild.roles,name="Commodore")
              await userdiscord.add_roles(role12)
              await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Rear Admiral":
              rankid = 99617324
              role13 = get(interaction.guild.roles,name="Rear Admiral")
              await m.setrank(rankid)
              await userdiscord.add_roles(role13)
              await interaction.response.send_message("User has been roled.",ephemeral=True)
            elif value == "Admiral":
              rankid = 99763224
              role14 = get(interaction.guild.roles,name="Admiral")
              await userdiscord.add_roles(role14)
              await m.setrank(rankid)
              await interaction.response.send_message("User has been roled.",ephemeral=True)
            










class ViewRoles(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(SelectRoles())
    





@bot.slash_command()
async def remove(interaction:Interaction,robloxusername,reason):
    try:
        d = await clientroblox.get_user_by_username(robloxusername)
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
    except roblox.utilities.exceptions.UserNotFound:
        await interaction.response.send_message("User doesn't exist")

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
    @nextcord.ui.button(label="Role User",style=nextcord.ButtonStyle.gray)
    async def roleuser(self,button:nextcord.ui.button,interaction:Interaction):
        view = ViewRoles()
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
            client = Client("The Roblox key here")
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
async def info(interaction:Interaction,member:nextcord.Member):
    d = member.id
    r = await interaction.guild.fetch_member(d)
    with open("discordid.txt","w",encoding="utf-8") as idwrite:
        idwrite.write(str(d))
    if r.nick[0] == "[":
        robloxusername = r.nick.split(" ")[1]
    else:
        robloxusername = r.nick

    try:
        robl2 = await clientroblox.get_user_by_username(robloxusername)
        id4 = robl2.id
        user = await client.get_user(id4)
        d = await user.thumbnails.get_avatar_image(size=ThumbnailSize.size_420x420)
        m = user.id
        f = user.display_name
        is_banned = user.is_banned
        something  = user.description
        created = user.created
        follower_count = await user.get_followers_count()
        group = await client.get_group(32747381)
        members = await group.get_member_by_id(user_id=id4)
        rank = members.role.name 
        with open("info.txt","w",encoding="utf-8") as writingdata:
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
    except roblox.utilities.exceptions.NotFound:
            robl2 = clientroblox.get_user_by_username(robloxusername)
            user = await client.get_user(robl2)
            d = await user.thumbnails.get_avatar_image(size=ThumbnailSize.size_420x420)
            m = user.id
            f = user.display_name
            is_banned = user.is_banned
            something  = user.description
            created = user.created
            follower_count = await user.get_followers_count()
            with open("info.txt","w",encoding="utf-8") as writingdata:
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












bot.run("Key Here")