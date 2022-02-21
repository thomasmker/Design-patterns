class DroneAdapter:
    def __init__(self, drone):
        self.__drone = drone

    def quack(self):
        self.__drone.beep()

    def fly(self):
        self.__drone.spin_rotors()
        self.__drone.take_off()
