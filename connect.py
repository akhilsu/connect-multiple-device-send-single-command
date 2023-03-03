from netmiko import ConnectHandler

devices = ["10.10.10.10","10.10.10.20","10.10.10.30","10.10.10.40","10.10.10.50"]

for i in devices:
    device = {
        "device_type" : "cisco_ios",
        "ip" : i,
        "username" : "root",
        "password" : "root@123",
        "port" : 22
    }

    connectdevice = ConnectHandler(**device)
    fetch = connectdevice.send_command("show version")
    print(fetch)
    connectdevice.disconnect()
