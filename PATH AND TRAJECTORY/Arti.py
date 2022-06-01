import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH,ERobot, ELink, ETS
import numpy as np

# link lengths in mm
a1 = float(input("a1 = ")) 
a2 = float(input("a2 = ")) 
a3 = float(input("a3 = ")) 

# link mm to meters converter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)

# Create Links
# [robot variable]=DHRobot([RevoluteDH(d,r/a,alpha,offset)])
Arti_Elbow = DHRobot([
    RevoluteDH(a1,0,(90/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a2,0,0,qlim=[(-20/180)*np.pi,(90/180)*np.pi]),
    RevoluteDH(0,a3,0,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
], name= 'Arti_Elbow')

print(Arti_Elbow)

# degrees to radian converter
def deg_to_rad(T):
    return (T/180.0)*np.pi

# q Paths
# for ARTICULATED joint variables = ([T1,T2,T3])
q0 = np.array([0,0,0]) # origin

q1 = np.array([mm_to_meter(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 1st path

q2 = np.array([mm_to_meter(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 2nd path

q3 = np.array([mm_to_meter(float(input("T1 = "))),
                deg_to_rad(float(input("T2 = "))),
                deg_to_rad(float(input("T3 = ")))]) # 3rd path

# Trajectory commands
traj1 = rtb.jtraj(q0,q1,50)
traj2 = rtb.jtraj(q1,q2,50)
traj3 = rtb.jtraj(q2,q3,50)

#plot scale
x1 = -0.3
x2 = 0.3
y1 = -0.3
y2 = 0.3
z1 = -0.3
z2 = 0.3


# plot command
Arti_Elbow.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2], movie='Articulated1.gif')
Arti_Elbow.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2], movie='Articulated2.gif')
Arti_Elbow.plot(traj3.q,limits=[x1,x2,y1,y2,z1,z2], movie='Articulated3.gif', block=True)

Arti_Elbow.teach(jointlabels=1)
