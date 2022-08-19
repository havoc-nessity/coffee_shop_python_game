#!/usr/bin/env python3

#i hate my life

def main():

	import time
	import random

	print("\n--------------------------------------------------------------------\n\n\"Welcome to the coffee shop, I'm your robot server, and no, not that kind of server, the kind that serves you coffee.\"\n")
	order=input('"So, what would you like?"\n').lower().strip()

	menu_list=["Dark Coffee", "Iced Coffee", "Hot Coffee"]

	c1=0
	

#looping this part was the hardest thing to do yet

	while(c1==0):

		if order=="help":
			print("\n\"If you want to do an action, you can add a '*' symbol at the beginning and end of the said action, also make sure to be specific.\"")
			order=input("\n").lower().strip()

		elif order=="menu":
			print("\n")
			print(menu_list)
			order=input("\n").lower().strip()

		elif order=="dark coffee":
			c1=1

		elif order=="iced coffee":
			c1=1
			
		elif order=="lol":
			order=input('\n"Who even actually says that?"\n').lower().strip()
			if order=="me":
				order==input("\n(._.)\n").lower().strip()

		elif order=="42":
			order=input('\n"I cannot compute, insufficient computing power."\n').lower().strip()
			
		elif order=="69":
			order=input('\n"nice but no."\n').lower().strip()

		elif order==("isn't that just a barista?") or order==("isnt that just a barista?") or order==("just a barista") or order==("aint that just a barista") or order==("ain't that just a barista"):
			order=input('\n"Well, yes but I wanted to say it so I can say that little joke. Don\'t judge me."\n').lower().strip()

		elif order==("coffee") or order==("drink"):
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

					#then give a randomized coffee in the menu

			elif order==("ok") or order==("okay") or order==("k"):
				order=input("\n\"Okay, let's try this again then.\"\n\"What would you like?\"\n").lower().strip()

		elif order==("bitches"):
			order=input('\n"I\'m afraid that is impossible... for you at least."\n')

		elif order=="punch":
			order=input('\n"We do not serve that I\'m afraid, we only serve coffee."\n')

		#//// Punch route
		elif order=="*punches*" or order=="*punch*": #ADD AN ELSE
			punchr=input('\n"You cannot hurt me as I am merely a robot, but I can still be damaged, so please don\'t do that as you will have to pay for damages"\n').lower().strip()
				#sorry and back to c1:
			if punchr=="sorry" or "ok sorry":
				order=input('\n"It\'s okay. Just please don\'t do it again. :)"\n"Anyway, let\'s go back to what you wanted to order."\n').lower().strip()

		#//// end punch route

		else:
			order=input("\nWhat? I can't seem to understand...\n").lower().strip()

	print("\n\"Okay, you'll get your "+order+" shortly...\"")

	time.sleep(1)
	print("\n.")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".\n")

if __name__=="__main__":
	main()

exit()
main()
