#!/usr/bin/env python3

#suck my arse

def main():

	import time

	print("\n\"Welcome to the coffee shop, I'm your robot server, and no, not that kind of server, the kind that serves you coffee.\"\n")
	order=input('"So, what would you like?"\n').lower().strip()

	menu_list=["Dark Coffee", "Iced Coffee", "Hot Coffee",]

	ans=0
	
#fuck this "while" bullshit took me so damn long just to loop this part
	while(ans==0):

		if order=="help":
			time.sleep(0.200)
			print("\n\"If you want to do an action, you can add a '*' symbol at the beggining and end of the said action")

		elif order=="menu":
			print("\n")
			print(menu_list)
			order=input("\n").lower().strip()

		elif order=="dark coffee":
			ans=1

		#elif order == "iced coffee":
			
		else:
			order=input("\nwhat? I can't seem to understand...\n").lower().strip()
			
	print("\n\"Okay, you'll get your "+order+" shortly...\"")
	
if __name__=="__main__":
	main()
	
exit()
main()
