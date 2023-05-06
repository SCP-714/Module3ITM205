print("Please use command 'help' to learn the commands for your adventure");
command = ""

while True:
    command = input(": ").lower()
    if command == 'start':
        print('You started your car!')
    elif command == 'stop':
        print('You stopped your car!')
    elif command == 'help':
        print("""
Please type > 'start' to start your car
Please type > 'stop' to stop your car
Please type > 'quit' to quit your game session
         """);
    elif command == 'quit':
        break
    else:
        print("Sorry I don't recognize this command!");