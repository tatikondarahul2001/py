# step the simulation through one time interval
def step( self ):
dt = self.dt
# step all the robots
for robot in self.robots:
# step robot motion
robot.step_motion( dt )

# apply physics interactions
self.physics.apply_physics()

# NOTE: The supervisors must run last to ensure they are observing the "current" world
# step all of the supervisors
for supervisor in self.supervisors:
supervisor.step( dt )

# increment world time
self.world_time += dt
