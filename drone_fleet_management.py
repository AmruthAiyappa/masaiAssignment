class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Drone is flying...")

class Drone(Device, Flyer):
    def __init__(self, device_id, model):
        Device.__init__(self, device_id)
        self.model = model

    def capture_image(self):
        print("Image captured by drone.")

# Demo
drone1 = Drone("DR001", "SkyX")
drone1.info()
drone1.fly()
drone1.capture_image()
