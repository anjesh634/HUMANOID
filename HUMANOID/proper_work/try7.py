#!/usr/bin/env python
import roslib
roslib.load_manifest('my_dynamixel_tutorial')
import time
import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg 
import control_msgs.msg  
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal



class Joint:
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            	self.name = motor_name   
		print(motor_name)        
		self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		rospy.loginfo('Waiting for joint trajectory action')
		self.jta.wait_for_server()
		rospy.loginfo('Found joint trajectory action!')

            
        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()                  
            char = self.name[0] #either 'f' or 'b'
            goal.trajectory.joint_names = ['motor6','motor3','motor2','motor4','motor7','motor1','motor5','motor19','motor8','motor9','motor10','motor11','motor12','motor13','motor14','motor15','motor16','motor17']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(0)              
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)
              
                       #     6         3        2         4         7       1        5           19        8          9        10      11         12      13      14        15       16      17       
def main():
	
	arm = Joint('f_arm')
	arm.move_joint([])
	


if __name__ == '__main__':
	rospy.init_node('trajectory_client')
	main()
print("Hello")
