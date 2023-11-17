from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()


def arm():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)


    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')
arm()
