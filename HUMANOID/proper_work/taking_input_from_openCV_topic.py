import rospy
from std_msgs.msg import String

pub=rospy.Publisher('topic',String,queue_size=10)
rospy.init_node('data_from_openCV')
 
while not rospy.is_shutdown():
    a=raw_input()    
    pub.publish(a)
    if a=='r':
       print a,"so you should move right" 
    if a=='l':
       print a,"so you should move left"
    if a=='f':
       print a,"so you should move forward"
    if a=='b':
       print a,"so you should move backword"
    if a=='tb':
       print a,"so you should take up bow"
    if a=='fa':
       print a,"so you should fit an arrow"
    if a=='rs':
       print a,"so you should be ready to shout"
    if a=='S':
       print a,"SHOUT!!" 
    
    

