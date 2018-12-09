import rospy
from std_msgs.msg import String

def reciver(recive):
    if recive.data=='S':
        rospy.loginfo('SHOOT!!')
    if recive.data=='r':
        rospy.loginfo('MOVING RIGHT')
    if recive.data=='l':
        rospy.loginfo('MOVING LEFT')
    if recive.data=='f':
        rospy.loginfo('MOVING FORWORD')
    if recive.data=='b':
        rospy.loginfo('MOVING BACKWORD')
    if recive.data=='rs':
        rospy.loginfo('BOT READY TO SHOOT')
    if recive.data=='fa':
        rospy.loginfo('BOT IS FITTING ARROW')
    if recive.data=='tb':
        rospy.loginfo('BOT IS PICKUPING BOW')

rospy.init_node('command_subscriber')
rospy.Subscriber('topic',String,reciver)
rospy.spin()
