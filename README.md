# quadruped_static_walking
Here I am gathering all the details required to make a quadruped robot with static walking gait
Target is to make something like this https://www.instructables.com/ARDUINO-SPIDER-ROBOT-QUADRUPED/
but with detailed understanding of gait generation and quadruped locomotion stability
Desired features are as follows
1) Mechanical structure taken from instructables mentioned above
2) Control system is to be developed from scratch
3) ESP32 based control electronics
4) MPU9250 for realtime attitude estimation
5) Integrated with ROS for implementation of complicated gait generation algorithms

Types of gaits are
1) Continous (wave) gait - body moves continously in desired direction
Most widely used by natura and artificial quadrupeds
2) Discontinous gait - body move intermittently in desired direction
For difficult terrain discontinous gait is preferred.
In this body moves in forward direction only when all legs are placed on ground securely
These are easier to implement

Important definitions
1) Gait: time and location of placement and lifting of each leg along with co ordinated movement of body with 6DOF so as to move the body from one place to another
2) Duty factor($\beta_i$): 

Useful resources
1) Book https://www.google.co.in/books/edition/Quadrupedal_Locomotion/3ZlDAAAAQBAJ?hl=en&gbpv=0
2) https://youtu.be/cCEm9mHTExo
3) https://youtu.be/xd8dKY6Ozrg
4) https://youtu.be/O_2swSMecB4
5) https://youtu.be/b0ZUfi8MHY8
6) https://youtu.be/26BDA4ycCfo
