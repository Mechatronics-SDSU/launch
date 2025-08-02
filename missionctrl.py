from multiprocessing                        import Process, Value
from shared_memory                          import SharedMemoryWrapper
from modules.motors.MotorInterface          import MotorInterface
from modules.pid.pid_interface              import PIDInterface
from modules.sensors.a50_dvl.dvl_interface  import DVL_Interface
from modules.vision.vision_main             import VideoRunner
from utils.kill_button_interface            import Kill_Button_Interface
import time
"""
    discord: @.kech
    github: @rsunderr

    Mission Control
    
"""

class MissionControl:
    def __init__(self):
        # create shared memory
        self.shared_memory_object = SharedMemoryWrapper()
        # set deadzone
        self.temp_x_hard_deadzone = 400 #FIXME
        # initial state
        self.state = None

        # create objects
        # normal
        self.vis_object = VideoRunner(self.shared_memory_object, self.temp_x_hard_deadzone) #, shared_memory_object.x_hard_deadzone)
        self.interface = MotorInterface(self.shared_memory_object)
        self.kill_btn = Kill_Button_Interface(self.shared_memory_object)
        # pid
        self.PID_interface = PIDInterface(self.shared_memory_object)
        self.dvl_object = DVL_Interface(self.shared_memory_object)        
                
        #create processes
        # normal
        self.vis_process = Process(target=self.vis_object.run_loop)
        self.interface_process = Process(target=self.interface.run_loop)
        self.kill_btn_process = Process(target=self.kill_btn.run_loop)
        # pid
        self.PID_process = Process(target=self.PID_interface.run_loop)
        self.dvl_process = Process(target=self.dvl_object.run_loop)
    
    def next_state(self, next):
        if next == self.state: return # do nothing if next state = current state
        # terminate previous state
        match(self.state):
            case "normal":
                self.vis_process.terminate()
                self.interface_process.terminate()
                self.kill_btn_process.terminate()
            case "pid":
                self.PID_process.terminate()
                self.dvl_process.terminate()
        # start next state
        self.state = next
        match(next):
            case "normal": # normal mode
                # start processes
                self.vis_process.start()
                self.interface_process.start()
                self.kill_btn_process.start()

                # wait for processes to finish
                self.vis_process.join()
                self.interface_process.join()
                self.kill_btn_process.join()

                #END
                print("Program has finished")

            case "pid": # pid testing mode
                # start processes
                self.PID_process.start()
                self.dvl_process.start()

                # wait for processes to finish
                self.PID_process.join()
                self.dvl_process.join()

                #END
                print("Program has finished")

            case None:
                print("None state")
            case _:
                print("invalid state")

    def loop(self):
        match(self.state):
            case "normal":
                pass
            case "pid":
                pass
            case None:
                print("None state")
                return
            case _:
                print("invalid state")
                return