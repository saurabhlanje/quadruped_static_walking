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
2) Duty factor $\beta_i$: fraction of cycle time for which the leg $i$ is on ground
3) Leg phase $\phi_i$: normalised time by which the placement of leg i on ground lags behind the placement of leg 1. Leg 1 is always considered as a reference for timming event
4) Stance phase or Support phase: The stance phase is the period of time when the foot under consideration is in contact with the floor
5) Transfer phase or Swing phase: The swing phase of gait begins when the foot first leaves the ground and ends when the same foot touches the ground again.
6) Leg stroke $R$: Distance which a foot is moved relative to body during the support phase. It must be within the workspace of leg
7) Stroke pitch: Distance between the strokes centers of adjacent legs
8) Stride length $\lambda$: Distacne travelled by center of gravity of body within a gait cycle


Useful resources
1) Book https://www.google.co.in/books/edition/Quadrupedal_Locomotion/3ZlDAAAAQBAJ?hl=en&gbpv=0
2) https://youtu.be/cCEm9mHTExo
3) https://youtu.be/xd8dKY6Ozrg
4) https://youtu.be/O_2swSMecB4
5) https://youtu.be/b0ZUfi8MHY8
6) https://youtu.be/26BDA4ycCfo
