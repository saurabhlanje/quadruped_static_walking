#! /usr/bin/env python

import rospy 
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random

def my_publisher():
    # control part

    rospy.init_node('trajectory_commander')
    control_publisher = rospy.Publisher('/spidy/joint_group_position_controller/command', JointTrajectory, queue_size=10)
    r=rospy.Rate(0.5)
    #j1 = float(input("Enter J1 number : "))
    #j2 = float(input("Enter J2 number : "))
    #j3 = float(input("Enter J3 number : "))
    leg_seq_1=[0.0,0.0,0]
    leg_seq_2=[0.0,0.3,0]
    leg_seq_3=[0.3,0.3,0]
    leg_seq_4=[0.3,0.0,0]
    leg_seq_5=[-0.3,0.0,0]

    joint_seq_1=leg_seq_2+leg_seq_2+leg_seq_1+leg_seq_1
    joint_seq_2=leg_seq_3+leg_seq_3+leg_seq_1+leg_seq_1
    joint_seq_3=leg_seq_4+leg_seq_4+leg_seq_1+leg_seq_1
    joint_seq_4=leg_seq_5+leg_seq_5+leg_seq_1+leg_seq_1
    joint_seq_5=leg_seq_1+leg_seq_1+leg_seq_1+leg_seq_1

    joint_seq_6=leg_seq_1+leg_seq_1+leg_seq_1+leg_seq_1
    joint_seq_7=leg_seq_1+leg_seq_1+leg_seq_2+leg_seq_2
    joint_seq_8=leg_seq_1+leg_seq_1+leg_seq_3+leg_seq_3
    joint_seq_9=leg_seq_1+leg_seq_1+leg_seq_4+leg_seq_4
    joint_seq_10=leg_seq_1+leg_seq_1+leg_seq_5+leg_seq_5


    #print(type(leg_seq_5))
    #print(joint_seq)
    seq=0

    while not rospy.is_shutdown():
        
        msg = JointTrajectory()

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['base2upleg_fr_le','mleg2upleg_fr_le','mleg2lleg_fr_le','base2upleg_ba_ri','mleg2upleg_ba_ri','mleg2lleg_ba_ri','base2upleg_re_le','mleg2upleg_re_le','mleg2lleg_re_le','base2upleg_fr_ri','mleg2upleg_fr_ri','mleg2lleg_fr_ri']

        point = JointTrajectoryPoint()
        j1 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j2 = 2 * (random.random() - 0.5)
        j3 = 2 * (random.random() - 0.5)

        j4 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j5 = 2 * (random.random() - 0.5)
        j6 = 2 * (random.random() - 0.5)

        j7 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j8 = 2 * (random.random() - 0.5)
        j9 = 2 * (random.random() - 0.5)


        j10 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        j11 = 2 * (random.random() - 0.5)
        j12 = 2 * (random.random() - 0.5)




        



        #point.positions = [j1,j2,j3,0,0,0,0,0,0,0,0,0]

        if seq==9:
            point.positions=joint_seq_10
            seq=0

        if seq==8:
            point.positions=joint_seq_8
            seq=9

        if seq==7:
            point.positions=joint_seq_8
            seq=8


        if seq==6:
            point.positions=joint_seq_7
            seq=7


        if seq==5:
            point.positions=joint_seq_6
            seq=6

        if seq==4:
            point.positions=joint_seq_5
            seq=5

        if seq==3:
            point.positions=joint_seq_4
            seq=4

        if seq==2:
            point.positions=joint_seq_3
            seq=3

        if seq==1:
            point.positions=joint_seq_2
            seq=2

        if seq==0:
            point.positions=joint_seq_1
            seq=1
        

        

        



        
        
        #point.positions = [0,0,0,0,0,0,0,0,0,0,0,0]

        #point.positions = [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append( point )

        control_publisher.publish( msg )
        rospy.loginfo( msg ) 
        r.sleep()


if __name__ == '__main__':

    my_publisher()


