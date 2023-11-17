from pymavlink import mavutil


master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return
    
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)
    
set_rc_channel_pwm(2, pwm=1500)
set_rc_channel_pwm(3, pwm=1500)
set_rc_channel_pwm(4, pwm=1500)
set_rc_channel_pwm(5, pwm=1500)