from chip import FabricAdmin
from chip import ChipStack

class Controller:
    def __init__(self, controller_node_id, device_ip, device_setup_pin_code, device_node_id):
        # Define comissionable device's network info (IP and Matter)
        self.device_ip = device_ip
        self.device_setup_pin_code = device_setup_pin_code
        self.device_node_id = device_node_id

        self.controller_node_id = controller_node_id

        self.startup()

    # Initial setup for the device controller
    def startup(self):
        self.chipStack = ChipStack.ChipStack(persistentStoragePath='/tmp/chip-device-ctrl-storage.json', installDefaultLogHandler=False, bluetoothAdapter=None)
        self.fabricAdmin = FabricAdmin.FabricAdmin()
        self.devCtrl = self.fabricAdmin.NewController(nodeId=self.controller_node_id, useTestCommissioner=True)

    # Connect to the device and commission it onto the fabric via the existing IP network
    def commission_device(self):
        # Commission the device over the existing IP network
        self.devCtrl.CommissionIP(self.device_ip.encode("utf-8"), self.device_setup_pin_code, self.device_node_id)

    # Switch the light on/off
    def toggle_light(self):
        cluster = "OnOff"
        command = "Toggle"
        endpoint = 1
        group_id = 1
        args = {}

        response = self.devCtrl.ZCLSend(cluster, command, self.device_node_id, endpoint, group_id, args)
        return response

    # Read the on/off value of the light
    def read_light(self):
        cluster = "OnOff"
        attribute = "OnOff"
        endpoint = 1
        group_id = 1

        result = self.devCtrl.ZCLReadAttribute(cluster, attribute, self.device_node_id, endpoint, group_id)
        return result

    # Shutdown device controller
    def shutdown(self):
        self.devCtrl.Shutdown()


# Example will connect to a light, then toggle it on and off reading its value
def main():
    controller = Controller(1, "2a00:23a8:89b:da01:5bac:df45:7887:b359", 20202021, 1234)

    while True:
        choice = input(">>>")

        if choice == "commission":
            controller.commission_device()
        elif choice == "toggle":
            print(controller.toggle_light())
        elif choice == "read":
            print(controller.read_light())
        elif choice == "exit" or choice == "quit" or choice == "q":
            controller.shutdown()
            exit()
        else:
            print("Unsupported choice")

if __name__ == "__main__":
    main()