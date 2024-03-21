user_input = ""

while True:
    user_input = input(" <<Give a command in lowercase letters:>> ")
    if user_input == "start":
        print("Car has started moving! ")
    elif user_input == "stop":
        print("Car has stopped moving")
    elif user_input == "help":
        print("""
        start - to start car
        stop - to stop car
        quit - to quit
        """)
    elif user_input == "quit":
        break
    else:
        print("Sorry I don't understand that...")


