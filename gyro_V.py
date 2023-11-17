"""
Example of how to read all the parameters from the Autopilot with pymavlink
"""

# Disable "Broad exception" warning
# pylint: disable=W0703

import time
import sys

# Import mavutil
from pymavlink import mavutil


# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict()['yaw'])
    except:
        pass
    time.sleep(0.1)
