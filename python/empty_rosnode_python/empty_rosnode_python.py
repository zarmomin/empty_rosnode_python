#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import numpy as np


class SomeNode(object):
    """
    Some Node
    """

    def __init__(self):
        self.node_name = 'mynode'

        # Setup the publishers and subscribers
        self.sub_some_odometry = rospy.Subscriber("sometopic", Odometry, self.odometry_callback)
        self.pub_other_odometry = rospy.Publisher("someOtherTopic", Odometry, queue_size=5)

        rospy.loginfo("[%s] has started", self.node_name)

    def odometry_callback(self, msg):
        """
        Do stuff
        """
        self.publish_updated_covariance(msg)

    def publish_updated_covariance(self, some_msg):
        """
        Publishes some other odometry
        """
        self.pub_other_odometry.publish(some_msg)


if __name__ == '__main__':
    rospy.init_node('empty_rosnode_python', anonymous=False)
    mynode = SomeNode()
    rospy.spin()
