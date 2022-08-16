from ...controller import Controller

# Example will connect to a light, then toggle it on and off reading its value
def main():
    controller = False

    while True:
        choice = input("> ")
        args = choice.split(" ")

        validCommand = False

        if args[0] == "connect":
            if len(args) != 4:
                print("Incorrect number of args")
            else:
                controller = Controller(1, args[1], int(args[2]), int(args[3]))
            validCommand = True

        elif args[0] == "help":
            print("List of available commands:")
            print("- connect <ip address> <setup pin code> <node id> - initialise the controller to these device values")
            print("- help - display this menu")
            print("- exit, quit, q - close the cli")
            print("\nCommands requiring you to connect first:")
            print("- commission - commission the light device with the values given by the 'connect' command")
            print("- toggle - toggle the on/off value of the light")
            print("- read - read the on/off value of the light")
            print("- address - print the address and port of the currently connected device")
            print("- scan - start a scan for new devices to connect to")
            print("- discovered - print discovered devices by a scan")
            validCommand = True

        elif args[0] == "exit" or args[0] == "quit" or args[0] == "q":
            if controller:
                controller.shutdown()
            exit()

        elif controller:
            if args[0] == "commission":
                controller.commission_device()
                validCommand = True

            elif args[0] == "toggle":
                print(controller.toggle_light())
                validCommand = True

            elif args[0] == "read":
                print(controller.read_light())
                validCommand = True

            elif args[0] == "address":
                print(controller.devCtrl.GetAddressAndPort(1234))
                validCommand = True

            elif args[0] == "scan":
                print("Scanning devices in background...")
                controller.scan()
                validCommand = True
                
            elif args[0] == "discovered":
                controller.print_discovered()
                validCommand = True
        
        if not validCommand:
            print("Unsupported choice")

if __name__ == "__main__":
    main()