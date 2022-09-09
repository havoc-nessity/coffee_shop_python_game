#!/usr/bin/env python3

#why

def main():

	import time
	import random

	print("\n--------------------------------------------------------------------\n\n\"Welcome to the coffee shop, I'm your robot server, and no, not that kind of server, the kind that serves you coffee.\"\n")
	order=input('"So, what would you like?"\n').lower().strip()

	menu_list=["Dark Coffee", "Iced Coffee", "Hot Coffee"];

#variables
	c1=0
	pnchs=0
	patience=0
	a=0

	darcof=0
	hotcof=0
	icecof=0

#looping this part was the hardest thing to do yet

	while(c1==0):

		#//// Loop Choices

		if order=="help":
			print("\n\"If you want to do an action, you can add a '*' symbol at the beginning and end of the said action, also make sure to be specific. Plain text will be automatically assumed to be speaking.\"")
			order=input("\n").lower().strip()

		elif "menu" in order:
			print("\n")
			print(menu_list)
			order=input("\n").lower().strip()

		elif order=="lol":
			order=input('\n"Who even actually says that?"\n').lower().strip()
			if order=="me":
				order==input("\n(._.)\n").lower().strip()

		elif order=="42":
			order=input('\n"I cannot compute, insufficient computing power."\n').lower().strip()
			
		elif order=="69":
			order=input('\n"nice but no."\n').lower().strip()

		elif order=="wd":
			order=input('\n"hmmm."\n').lower().strip()

		elif order=="/fh:j k/fdz{ ;ldltsf] k|ltj]bg @)^&":
			order=input('\n- Ministry of Finance\n').lower().strip()

		elif order=="abcdefghijklmnopqrstuvwxyz":
			order=input('\n"Were you singing that while typing that in?"\n').lower().strip()

		elif order=="420":
			order=input('\n"I\'m sorry, but we do not serve cannabis here."\n').lower().strip()

		elif order=="69420" or order=="420 69" or order=="69 420":
			order=input('\n"Quite the memer aren\'t you...?"\n').lower().strip()

		elif "fuck you" in order or "**** you" in order or "*** you" in order or "f*** you" in order or order=="shit yourself":
			order=input('\n"That\'s quite rude."\n').lower().strip()

		elif order==("bitches"):
			order=input('\n"I\'m afraid that is impossible... for you at least."\n').lower().strip()

		elif order=="punch":
			order=input('\n"We do not serve that I\'m afraid, we only serve coffee."\n').lower().strip()

		elif order=="fuck" or order=="a fuck":
			order=input('\n"Sorry, we don\'t serve that here. If you\'d like, you can go down the street and get that at the store called: \'3\'"\n').lower().strip()

		elif order==("isn't that just a barista?") or order==("isnt that just a barista?") or order==("you're just a barista") or order==("aint that just a barista") or order==("ain't that just a barista"):
			order=input('\n"Well, yes but I wanted to say it so I can say that little joke. Don\'t judge me."\n').lower().strip()

		elif "coffee machine" in order:
			order=input('\n"I\'m better than a coffee machine... :("\n').lower().strip()

		elif order=="w":
			order=input('\nYou move forward.\n').lower().strip()

		elif order=="a":
			order=input('\nYou move left.\n').lower().strip()

		elif order=="s":
			order=input('\nYou move backwards\n').lower().strip()

		elif order=="d":
				order=input('\nYou move right.\n').lower().strip()

		#//// end Loop Choices

		#//// Coffee choices (Main Routes)

		elif "dark coffee" in order:
			c1=1
			#ACS1
			darkcof=1

		elif "iced coffee" in order:
			c1=1
			#ACS1
			icecof=1

		elif "hot coffee" in order:
			c1=1
			#ACS1
			hotcof=1

		elif "coffee" in order or "drink" in order:
			order=input('\n"Please be more specific."\n').lower().strip()
			if order==("no"):
				order=input('\n"I cannot take your order if you do not specify..."\n').lower().strip()
				if order==("no"):
					print('\n"Okay... I\'m still not quite sure what coffee to give you but I\'ll try my luck."\n')

					time.sleep(1)
					print(".")
					time.sleep(1)
					print(".")
					time.sleep(1)
					print(".")

					#then give a randomized coffee from the menu

			elif order==("ok") or order==("okay") or order==("k"):
				order=input("\n\"Okay, let's try this again then.\"\n\"What would you like?\"\n").lower().strip()

		#//// Punch route

		elif order=="*punches*" or order=="*punch*": #ADD A COUNTER TO HOW MANY PUNCHES WERE GIVEN AND ADD LIMIT
			pnchs+=1
			punchr=input('\n"You cannot hurt me as I am merely a robot, but I can still be damaged, so please don\'t do that as you will have to pay for damages"\n').lower().strip()

			if punchr=="sorry" or punchr=="ok sorry":
				order=input('\n"It\'s okay. Just please don\'t do it again. :)"\n"Anyway, let\'s go back to what you wanted to order."\n').lower().strip()

			elif punchr=="*punch*" or punchr=="*punches*":
				pnchs+=1
				punchr=input('\n"Please stop that. This isn\'t a fight club."\n').lower().strip()

			else:
				order=input('\n"What? I can\'t seem to understand..."\n').lower().strip()

		elif pnchs==2:
			print("fuck you")

		#//// START punch route

		#//// SP Route

		elif "..." in order:
			silpror=input('\n"Ummm... Sir?"\n').lower().strip()

			if "..." in silpror:
				silpror=input('\n"Hello?"\n').lower().strip()

				while(a==0) or (a==1) or (a==3):
					if "..." in silpror:
						silpror=input('\n"..."\n').lower().strip()
						a+=1
					else:
						order=input('\n"What? I can\'t seem to understand..."\n').lower().strip()

			else:
				order=input('\n"What? I can\'t seem to understand..."\n').lower().strip()

		#//// START SP Route

		else:
			order=input('\n"What? I can\'t seem to understand..."\n').lower().strip()

#ACS1
		if icecof==1:
			order="Iced Coffee"
		elif hotcof==1:
			order="Hot Coffee"
		elif darcof==1:
			order="Dark Coffee"
#ACS1

	print("\n\"Okay, you'll get your "+order+" shortly...\"")

	time.sleep(1)
	print("\n.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".\n")

#GAME START

if __name__=="__main__":
	main()

exit()
main()
