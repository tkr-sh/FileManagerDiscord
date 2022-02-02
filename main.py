from discord.ext import commands
import discord
import xml.etree.ElementTree as ET


bot = commands.Bot(command_prefix="&")
token = "token_of_your_bot" # Token of the Bot

client = discord.Client()


tree = ET.parse('data.xml') # Name of the XML doc
name_bot = "the_name_of_your_bot#tag"
root = tree.getroot()
pwd=[]
print(tree,root)

@client.event
async def on_message(message):
    global root,pwd
    if str(message.author)!=name_bot:
        
        # ██████╗██████╗ 
        #██╔════╝██╔══██╗
        #██║     ██║  ██║
        #██║     ██║  ██║
        #╚██████╗██████╔╝
        #╚═════╝╚═════╝
        if str(message.content).split()[0] == "cd": # Change Directory
            #Syntax: {cd} {dir}
            found = False
            for child in root:
                if child.get('name') == str(message.content)[3:]:
                    root = child
                    print(root.attrib," AHHH")
                    pwd+=[child.get('name')]
                    found = True
                    break
            try:
                if not found:
                    embedVar = discord.Embed(title="**Didn't find the directory** \t :x: ", description="", color=0xda2d43)
                    await message.channel.send(embed=embedVar)
            except discord.errors.HTTPException:
                pass


        # ██████╗██████╗       
        #██╔════╝██╔══██╗      
        #██║     ██║  ██║      
        #██║     ██║  ██║      
        #╚██████╗██████╔╝██╗██╗
        # ╚═════╝╚═════╝ ╚═╝╚═╝
        elif str(message.content).replace(" ","") == "cd..":
            #Syntax: {cd..}
            for p in tree.iter():
                for child in p:
                    print(str(child),root)
                    if str(child) == str(root):
                        root = p
                        pwd = pwd[:-1]
                        break

        
        #██╗     ███████╗
        #██║     ██╔════╝
        #██║     ███████╗
        #██║     ╚════██║
        #███████╗███████║
        #╚══════╝╚══════╝
        elif str(message.content).split()[0] == "ls": # List
            #Syntax: {ls}
            l = [[":page_facing_up: ",":file_folder: "][str(child).split()[1]=="'main'"]+child.get('name') for child in root if child.get('name')!=None] # Get all "name"s of the root, if name is None, thant don't add it
            try:
                embedVar = discord.Embed(title="\n".join(l), description="/"+"/".join(pwd), color=0x4353c2)
                await message.channel.send(embed=embedVar)
            except discord.errors.HTTPException:
                pass
        

        #██████╗ ██╗    ██╗██████╗ 
        #██╔══██╗██║    ██║██╔══██╗
        #██████╔╝██║ █╗ ██║██║  ██║
        #██╔═══╝ ██║███╗██║██║  ██║
        #██║     ╚███╔███╔╝██████╔╝
        #╚═╝      ╚══╝╚══╝ ╚═════╝
        elif str(message.content).split()[0] == "pwd": # List
            #Syntax: {pwd}
            stp = "/"+"/".join(pwd) #stp == string to print
            try:
                embedVar = discord.Embed(title=stp, description="", color=0x4353c2)
                await message.channel.send(embed=embedVar)
            except discord.errors.HTTPException:
                pass


        #██╗  ██╗ ██████╗ ███╗   ███╗███████╗
        #██║  ██║██╔═══██╗████╗ ████║██╔════╝
        #███████║██║   ██║██╔████╔██║█████╗  
        #██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  
        #██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗
        #╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
        elif str(message.content) == "home":
            #Syntax: {home}
            root = tree.getroot()
            pwd=[]

        
        #███╗   ███╗██╗  ██╗██████╗ ██╗██████╗ 
        #████╗ ████║██║ ██╔╝██╔══██╗██║██╔══██╗
        #██╔████╔██║█████╔╝ ██║  ██║██║██████╔╝
        #██║╚██╔╝██║██╔═██╗ ██║  ██║██║██╔══██╗
        #██║ ╚═╝ ██║██║  ██╗██████╔╝██║██║  ██║
        #╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝
        elif str(message.content).split()[0] == "mkdir": # Make Directory
            #Syntax: {mkdir} {dir name}
            ET.SubElement(root, 'main').set('name',str(message.content)[6:].strip())


        #████████╗ ██████╗ ██╗   ██╗ ██████╗██╗  ██╗
        #╚══██╔══╝██╔═══██╗██║   ██║██╔════╝██║  ██║
        #   ██║   ██║   ██║██║   ██║██║     ███████║
        #   ██║   ██║   ██║██║   ██║██║     ██╔══██║
        #   ██║   ╚██████╔╝╚██████╔╝╚██████╗██║  ██║
        #   ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
        elif str(message.content).split()[0] == "touch" and len(str(message.content).split()) > 2: # Touch
            #Syntax: {touch} {filename} {message_ID}
            ET.SubElement(root, 'file').set('name', " ".join(str(message.content).split()[1:-1]))
            for child in root:
                if child.get('name') == " ".join(str(message.content).split()[1:-1]):
                    child.text = str(message.content).split()[-1]
                    break
            embedVar = discord.Embed(title=f"**{' '.join(str(message.content).split()[1:-1])} file created. With an ID of {str(message.content).split()[-1]}** \t :white_check_mark: ", description="", color=0x77B255)
            await message.channel.send(embed=embedVar)


        # ██████╗
        #██╔════╝
        #██║     
        #██║     
        #╚██████╗
        # ╚═════╝
        elif str(message.content).split()[0] == "c": # See
            #Syntax: {c} {filename}
            msg_id=0
            found = False
            for child in root: # Detect if the file that you want to see (c) is in it :)
                if child.get('name') == str(message.content)[2:] and child.tag == "file": # If the filename is OK and it's a file and not a dir
                    msg_id = int(child.text) # The message ID will be that
                    found = True
                    break
            
            if found: # If the file exist
                for chan in message.guild.text_channels: 
                    try:
                        msg = await chan.fetch_message(msg_id) # Getting the message
                        if msg.content != "":
                            await message.channel.send(msg.content) # Msg.content
                        for attachment in msg.attachments: #Files with the message
                            await message.channel.send("Fichier avec le message: "+attachment.filename)
                            await message.channel.send(attachment)  
                    except RuntimeWarning:
                        pass
                    except discord.errors.NotFound:
                        pass
            else:
                embedVar = discord.Embed(title="**There is not file with this name** \t :x: ", description="", color=0xda2d43)
                await message.channel.send(embed=embedVar)


        #███╗   ███╗██████╗ ██╗██████╗ 
        #████╗ ████║██╔══██╗██║██╔══██╗
        #██╔████╔██║██║  ██║██║██║  ██║
        #██║╚██╔╝██║██║  ██║██║██║  ██║
        #██║ ╚═╝ ██║██████╔╝██║██████╔╝
        #╚═╝     ╚═╝╚═════╝ ╚═╝╚═════╝
        elif str(message.content).split()[0] == "mdid": # Modify ID
            #Syntax: {mdid} {filename} {newid}
            msg_id=0
            found = False
            for child in root: # Detect if the file that you want to MDID is in 
                if child.get('name') == str(message.content).split()[1] and child.tag == "file" : # If the filename is OK and it's a file and not a dir
                    child.text =  str(message.content).split()[2]
                    found = True
                    break
            
            if not found: # If the file doesn't exist
                embedVar = discord.Embed(title="**There is not file with this name** \t :x: ", description="", color=0xda2d43)
                await message.channel.send(embed=embedVar)


        #██████╗ ███╗   ███╗
        #██╔══██╗████╗ ████║
        #██████╔╝██╔████╔██║
        #██╔══██╗██║╚██╔╝██║
        #██║  ██║██║ ╚═╝ ██║
        #╚═╝  ╚═╝╚═╝     ╚═╝
        elif str(message.content).split()[0] == "rm": # Remove
            #Syntax: {rm} {dir or file} {name}
            tag = ["main","file"][str(message.content).split()[1] == "file"]
            found = False
            for child in root: # Detect if the file that you want to rm is in 
                if child.get('name') == ' '.join(str(message.content).split()[2:]) and child.tag == tag : # If the filename is OK and it's a file and not a dir
                    root.remove(child)
                    found = True
                    break
            
            if not found: # If the file doesn't exist
                embedVar = discord.Embed(title="**There is not file with this name** \t :x: ", description="", color=0xda2d43)
                await message.channel.send(embed=embedVar)
        


        #██████╗ ███╗   ██╗
        #██╔══██╗████╗  ██║
        #██████╔╝██╔██╗ ██║
        #██╔══██╗██║╚██╗██║
        #██║  ██║██║ ╚████║
        #╚═╝  ╚═╝╚═╝  ╚═══╝
        elif str(message.content).split()[0] == "rn": # Rename
            #Syntax: {rn} {dir or file} {old_name} {>} {new_name}
            tag = ["main","file"][str(message.content).split()[1] == "file"]
            found = False
            for child in root: # Detect if the file that you want to rename is in
                if child.get('name') == ' '.join(str(message.content).split()[2:]).split(">")[0].strip() and child.tag == tag : # If the filename is OK and it's a file and not a dir
                    child.set('name', ' '.join(str(message.content).split()[2:]).split(">")[1].strip())
                    embedVar = discord.Embed(title="**Done** \t :white_check_mark: ", description="", color=0x77B255)
                    await message.channel.send(embed=embedVar)
                    found = True
                    break
            
            if not found: # If the file doesn't exist
                embedVar = discord.Embed(title="**There is not file with this name** \t :x: ", description="", color=0xda2d43)
                await message.channel.send(embed=embedVar)
        

        #███╗   ███╗██╗   ██╗
        #████╗ ████║██║   ██║
        #██╔████╔██║██║   ██║
        #██║╚██╔╝██║╚██╗ ██╔╝
        #██║ ╚═╝ ██║ ╚████╔╝ 
        #╚═╝     ╚═╝  ╚═══╝
        elif str(message.content).split()[0] == "mv": # Move
            #Syntax: {mv} {dir or file} {name} {>} {dir}
            tag = ["main","file"][str(message.content).split()[1] == "file"]
            found = False
            for child in root: # Detect if the file that you want to rename is in
                if child.get('name') == ' '.join(str(message.content).split()[2:]).split(">")[0].strip() and child.tag == tag: # If the filename is OK and it's a file and not a dir
                    for dir in root:
                        if dir.get('name') == ' '.join(str(message.content).split()[2:]).split(">")[1].strip() and dir.tag == "main":
                            dir.append(child)
                            root.remove(child)
                            embedVar = discord.Embed(title=f"**Moved {child.get('name')} to {dir.get('name')}** \t :white_check_mark: ", description="", color=0x77B255)
                            await message.channel.send(embed=embedVar)
                            found = True
                            break

            if not found: # If the file doesn't exist
                embedVar = discord.Embed(title="**There is not file with this name** \t :x: ", description="", color=0xda2d43)
                await message.channel.send(embed=embedVar)
        

        #███╗   ███╗██╗   ██╗     
        #████╗ ████║██║   ██║     
        #██╔████╔██║██║   ██║     
        #██║╚██╔╝██║╚██╗ ██╔╝     
        #██║ ╚═╝ ██║ ╚████╔╝██╗██╗
        #╚═╝     ╚═╝  ╚═══╝ ╚═╝╚═╝
        elif str(message.content).split()[0] == "mv..": # Move back
            #Syntax: {mv..} {dir or file} {name}
            tag = ["main","file"][str(message.content).split()[1] == "file"]
            found = False
            for p in tree.iter(): # Above root
                for child in p: # The root
        
                    if str(child) == str(root): 
                        for lilchild in child: # Child of root
                            print(str(lilchild),lilchild.get('name'))
                            if lilchild.get('name') == ' '.join(str(message.content).split()[2:]) and lilchild.tag == tag:
                                p.append(lilchild)
                                root.remove(lilchild)
                                break

        
        #██╗  ██╗███████╗██╗     ██████╗ 
        #██║  ██║██╔════╝██║     ██╔══██╗
        #███████║█████╗  ██║     ██████╔╝
        #██╔══██║██╔══╝  ██║     ██╔═══╝ 
        #██║  ██║███████╗███████╗██║     
        #╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ 
        elif str(message.content).split()[0] == "help": # HELP
            cmd = ["c","cd","cd..","help","home","ls","mdid","mkdir","mv","mv..","pwd","rm","rn","touch"]
            use = ["See a message","Change of Directory","Go back of Directory","help","Send you to the first directory","List of elements in the directory that you're in","Modify the ID of a file","Make a new Diretory","Move an element to a directory","Move an element to the previous directory","Print Working Directory","Remove a file or directory","Renale a file or Directory","Create a file"]
            syntax = ["c a_file", "cd a_dir", "cd..","help OR help a_cmd","home","ls","mdid the_filename the_new_id","mkdir name_of_dir","mv \"dir\" OR \"file\" name_of_dir_or_file > a_dir","mv.. \"dir\" OR \"file\" name_of_dir_or_file " ,"pwd","rm \"dir\" OR \"file\" name_of_dir_or_file","rn \"dir\" OR \"file\" old_name > new_name","touch name_of_file message_ID"]
            admin = ["rm"]
            if str(message.content) == "help":
                embedVar = discord.Embed(title="Commands Are:\n~ "+'\n~ '.join("**"+cmd[i]+"**"+[""," - ADMIN"][cmd[i] in admin]for i in range(len(cmd))), description="You can do: help the_name_of_the_cmd to learn about this command. Example: help cd", color=0x4353c2)
                await message.channel.send(embed=embedVar)
            
            else:
                found = False
                for i,command in enumerate(cmd):
                    if str(message.content).split()[1] == command:
                        msg = "**"+cmd[i]+"**:\n"+use[i]
                        found = True
                        embedVar = discord.Embed(title=msg, description="Syntax: "+syntax[i], color=0x4353c2)
                        await message.channel.send(embed=embedVar)
                if not found: # If the file doesn't exist
                    embedVar = discord.Embed(title="**The command "+str(message.content).split()[1] + " doesn't exist** \t :x: ", description="", color=0xda2d43)
                    await message.channel.send(embed=embedVar)
                     

    tree.write("data.xml")


client.run(token)
