from pymavlink import mavutil
import time
master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()


def disarm():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        0, 0, 0, 0, 0, 0, 0)
    master.motors_disarmed_wait()
    print("disarm")
disarm()




