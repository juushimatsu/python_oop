class Device:
    def __init__(self, is_on: bool, battery_level: int) -> None:
        self.is_on = is_on
        self.battery_level = battery_level

    def __bool__(self):
        return self.is_on and self.battery_level > 10

device1 = Device(True, 20)
device2 = Device(True, 5)
device3 = Device(False, 50)
device4 = Device(False, 0)

print(bool(device1))
print(bool(device2))
print(bool(device3))
print(bool(device4))
