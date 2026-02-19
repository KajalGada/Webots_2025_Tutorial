"""wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

def line_follower(my_robot):
    """Take robot instance, reads IR sensor to drive robot along the line"""

    # get the time step of the current world.
    timestep = 32
    max_speed = 6.28
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    
    # Enable motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    
    
    # Enable IR sensors
    left_ir = robot.getDevice('ir0')
    left_ir.enable(timestep)
    
    right_ir = robot.getDevice('ir1')
    right_ir.enable(timestep)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        
        # read ir sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print("left: {}, right:{}".format(left_ir_value,right_ir_value))
        
        left_speed = max_speed
        right_speed = max_speed
    
        # Process sensor data here.
        # If left sensors see the black line, go left
        if (left_ir_value > right_ir_value) and (6 < left_ir_value < 15):
            left_speed = -max_speed * 0.25
        # if right sensors seees the black line, go right
        elif (right_ir_value > left_ir_value) and (6 < right_ir_value < 15):
            right_speed = -max_speed * 0.25
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
    # Enter here exit cleanup code.
    

if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    line_follower(robot)

