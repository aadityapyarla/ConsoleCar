print("Welcome to your Console-Car")
command = ""
started = False
stoppped = False
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To quit
        """)
    elif command == "start":
        if started:
            print("Car is already started !")
        else:
            print("Car is started..")
            started = True
    elif command == "stop":
        if stoppped:
            print("Car is already stopped !")
        else:
            print("Car is stopped..")
            stoppped = True
    elif command == "quit":
        break
    else:
        print("Sorry I didn't understand..")
