from chip import FabricAdmin
from chip import ChipStack
from chip import ChipCommissionableNodeCtrl

# Initial setup
def setup_device_controller():
    controllerNodeId = 1

    chipStack = ChipStack.ChipStack(persistentStoragePath='/tmp/chip-device-ctrl-storage.json', installDefaultLogHandler=False, bluetoothAdapter=None)
    fabricAdmin = FabricAdmin.FabricAdmin()
    devCtrl = fabricAdmin.NewController(nodeId=controllerNodeId, useTestCommissioner=True)
    commissionableNodeCtrl = ChipCommissionableNodeCtrl.ChipCommissionableNodeController(chipStack)

    return devCtrl

# Connect to the device and commission it onto the fabric via the existing IP network
def commission_device(devCtrl, node_id):
    # Define comissionable device's network info (IP and Matter)
    ip = "fd11:1111:1122:0:d81e:e2ff:f8db:b323".encode("utf-8")
    setup_pin_code = 20202021

    # Commission the device over the existing IP network
    devCtrl.CommissionIP(ip, setup_pin_code, node_id)


# Switch the light on/off
def toggle_light(devCtrl, node_id, endpoint, group_id):
    cluster = "OnOff"
    command = "Toggle"
    args = {}

    response = devCtrl.ZCLSend(cluster, command, node_id, endpoint, group_id, args)
    return response

# Read the on/off value of the light
def read_light(devCtrl, node_id, endpoint, group_id):
    cluster = "OnOff"
    attribute = "OnOff"

    result = devCtrl.ZCLReadAttribute(cluster, attribute, node_id, endpoint, group_id)
    return result

# Example will connect to a light, then toggle it on and off reading its value
def main():
    devCtrl = setup_device_controller()

    node_id = 1234
    endpoint = 1
    group_id = 1

    commission_device(devCtrl, node_id)

    print(toggle_light(devCtrl, node_id, endpoint, group_id))
    print(read_light(devCtrl, node_id, endpoint, group_id))
    print(toggle_light(devCtrl, node_id, endpoint, group_id))
    print(read_light(devCtrl, node_id, endpoint, group_id))

    devCtrl.Shutdown()

if __name__ == "__main__":
    main()