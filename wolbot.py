import os

# installing all pip programs
print("installing pip programs")
os.system("pip install py-cord")
os.system("pip install wakeonlan")
os.system("pip install ")

import discord
from discord.ext import commands
import time
from wakeonlan import send_magic_packet

bot = commands.Bot()
print("online")


data = {
  "PCs": [
    {
      "Name": "localpc",
      "IP": "localhost",
      "Type":"test"
    },
     {
      "Name": "pc1",
      "mac": "00-00-00-00-00",
      "IP": "0.0.0.0",
      "Type":"pc"
    },
     {
      "Name": "pc2",
      "IP": "0.0.0.0",
       "mac": "00-00-00-00-00",
      "Type":"pc"
      
    },
    {
      "Name": "router",
      "IP": "192.168.1.1",
      "Type":"test"
    },
    {
      "Name": "cloudflair",
      "IP": "1.1.1.1",
      "Type":"test"
    }
  ]
}

# Function to get IP from name
def get_ip(name,find,get):
    print("finding " + get + " of " + find + " " + name)
    for count in data["PCs"]:
        if count[find] == name:
            print("found")
            return count[get]
    return None

def ping(ip):
    print("pinging " + ip)
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        return True
    else:
        return False

@bot.slash_command(name='ping', description='ping pc by name')
async def whitelist(ctx, name: str):
    print("command /ping " + name + "entered")
    iptp = get_ip(name,"Name","IP")
    if iptp == None:
        await ctx.respond("device \"" + name + " \" does not exist")
    else:
        await ctx.respond("pinging " + iptp)
        if ping(iptp):
             await ctx.respond(name + " is up :white_check_mark:")
        else:
            await ctx.respond(name + " is down :x:")

@bot.slash_command(name='pingall', description='ping all pcs')
async def whitelist(ctx):
    print("command /pingall entered")
    ctx.respond("please wait")
    out = ""
    run = "1"
    dead = "1"
    for count in data["PCs"]:
        if ping(count["IP"]):
            out = out + "\n" + ":white_check_mark: "+ count["Name"] 
        else:
            out = out + "\n" + ":x: " + count["Name"] 
    dead = dead + run
    await ctx.respond(out)


   
@bot.slash_command(name='wake', description='wake up pc')
async def whitelist(ctx, name2: str):
    print("command /wakeonlan " + name2 + "entered")
    ip = get_ip(name2,"Name","IP")
    if ip == none:
        await ctx.respond("device \"" + name2 + " \" does not exist")
    else:
        canwake = get_ip(name2,"Name","type")
        if canwake == "pc":
            send_magic_packet(mac,ip_address=iptp)
            ctx.respond("sent packet")
            time.sleep(10)
            if ping(ip):
                ctx.respond("sucsess")
            else:
                ctx.respond("Failure")
        else:
            ctx.respond("this device dosent suport wol and is here for network testing")


bot.run("api key")