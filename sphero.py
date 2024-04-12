from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import socket
import pickle

class UDP:
    HOST = '127.0.0.1'  # The IP address of the receiver
    PORT = 65432        # The port the receiver is listening on

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create the socket once
    s.bind((HOST, PORT))

    @staticmethod
    def get_data():
        serialized_data, addr = UDP.s.recvfrom(1024)
        data = pickle.loads(serialized_data)
        return data


toy = scanner.find_toy()

with SpheroEduAPI(toy) as droid:
    
    print("Conectado")
    droid.set_main_led(Color(r=0, g=0, b=255))

    while True:
        
        data = UDP.get_data()
        action = data['action']
        print(action)
        '''
        "actions": [
            "neutral",
            "push",
            "pull",
            "lift",
            "drop",
            "left",
            "right",
            "rotateLeft",
            "rotateRight",
            "rotateClockwise",
            "rotateCounterClockwise",
            "rotateForwards",
            "rotateReverse",
            "disappear"
        ]
        '''

        match action:
            case "rotateForwards":
                droid.set_heading(0)
                droid.set_speed(10)
            case "rotateReverse":
                droid.set_heading(180)
                droid.set_speed(10)
            case "rotateLeft":
                droid.set_heading(270)
                droid.set_speed(10)
            case "rotateRight":
                droid.set_heading(90)
                droid.set_speed(10)
            case _:
                droid.stop_roll()
