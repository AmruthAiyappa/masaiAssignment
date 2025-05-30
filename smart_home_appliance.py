class Appliance:
    def status(self):
        print("This is a generic appliance.")

class Fan(Appliance):
    def status(self):
        print("Fan is running at medium speed.")

class Light(Appliance):
    def status(self):
        print("Light is turned ON.")

class AC(Appliance):
    def status(self):
        print("AC is set to 24°C.")

# Demo
devices = [Fan(), Light(), AC()]
for device in devices:
    device.status()
