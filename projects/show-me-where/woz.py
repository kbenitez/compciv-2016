from utils.geocoding import geocode

B_S = "\033[1m"
B_E = "\033[0m"

COMMANDS = ["hello", "geocode", "help"]

def askUserWTD():
	numCommands = len(COMMANDS)
	stringOfCommands = ""
	for n in range(numCommands):
		stringOfCommands += (COMMANDS[n] + ", ")
	print("I can follow these commands: " + stringOfCommands[:-2])
	command = input("What do you want to do? ")
	while command.lower() not in COMMANDS:
		command = input("I can't do that. I can follow: " + stringOfCommands[:-2] + ". What do you want to do? ")	
	return command.lower();


command = askUserWTD()
if command == "hello":
    usertext = input("What's your name? ")
    print("Hello", B_S + usertext + B_E + "!")
elif command == "geocode":
    userlocation = input("What's your location? ")
    print("OK...geocoding:", userlocation)
    georesult = geocode(userlocation)
    print(georesult)
elif command == "help":
    print("hello \n")
    print("    Asks the user for his/her name then repeats it back in bold with a hello and exclamation point!")
    print("\n")
    print(geocode.__name__)
    print(geocode.__doc__)
else:
    print("Sorry, I don't know how to respond to", command)

