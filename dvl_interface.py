from a50_dvl.dvl import DVL

class DVL_Interface:

    def __init__(self, x, y, z, pitch, roll, yaw):
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.dvl = DVL()

    def update(self):
        dvl_data = self.dvl.recieveData()
        if dvl_data != None:
            self.yaw = dvl_data[0]
            self.pitch = dvl_data[1]
            self.roll = dvl_data[2]
            self.x = dvl_data[3]
            self.y = dvl_data[4]
            self.z = dvl_data[5]

    def run_loop(self):
        self.update()

