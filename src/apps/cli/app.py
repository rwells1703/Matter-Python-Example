from ...controller import Controller

# Example will connect to a light, then toggle it on and off reading its value
def main():
    controller = Controller(1, "2a00:23a8:89b:da01:5bac:df45:7887:b359", 20202021, 1234)
    
    while True:
        choice = input(">")

        if choice == "commission":
            controller.commission_device()
        elif choice == "toggle":
            print(controller.toggle_light())
        elif choice == "read":
            print(controller.read_light())
        elif choice == "address":
            print(controller.devCtrl.GetAddressAndPort(1234))
        elif choice == "exit" or choice == "quit" or choice == "q":
            controller.shutdown()
            exit()
        else:
            print("Unsupported choice")

if __name__ == "__main__":
    main()