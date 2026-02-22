# System storage (acts like a database)
devices = []


def add_device():
    device_name = input("Enter device name: ").strip()
    device_type = input("Enter device type (router/switch/firewall): ").strip().lower()
    status = input("Enter status (active/inactive): ").strip().lower()

    device_details = {
        "device_name": device_name,
        "device_type": device_type,
        "status": status
    }

    device_exists = False

    for device in devices:
        if device["device_name"] == device_name:
            device_exists = True
            break
        else:
            device_exists = False

    if device_exists == True:
        print(" Device already exists")
    else:
        devices.append(device_details)
        print(" Device added successfully")


def view_devices():
    if len(devices) == 0:
        print(" No devices found")
    else:
        print("\n--- Device Inventory ---")
        for device in devices:
            print(
                "Name:", device["device_name"],
                "| Type:", device["device_type"],
                "| Status:", device["status"]
            )


def search_device():
    search_name = input("Enter device name to search: ").strip()
    found = False

    for device in devices:
        if device["device_name"] == search_name:
            print(" Device Found:")
            print(device)
            found = True
            break
        else:
            found = False

    if found == False:
        print(" Device not found")


# Main Menu Loop
while True:
    print("\n=== Device Management System ===")
    print("1. Add Device")
    print("2. View Devices")
    print("3. Search Device")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_device()
    elif choice == "2":
        view_devices()
    elif choice == "3":
        search_device()
    elif choice == "4":
        print(" Exiting system")
        break
    else:
        print(" Invalid option")
