"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

span = 50

def uniformmotion(a,b):
    return random.uniform(a,b)

boids_x=[uniformmotion(-450,50.0) for x in range(span)]
boids_y=[random.uniform(300.0,600.0) for x in range(span)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(span)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(span)]

boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

xdisp,ydisp,xvel,yvel=boids

#ftm stands for "fly to middle"
ftm_length_numerator = 0.01
def fly_to_middle(a,b):
    xvel[a]=xvel[a]+(xdisp[b]-xdisp[a])*ftm_length_numerator/len(xdisp)
    yvel[a]=yvel[a]+(ydisp[b]-ydisp[a])*ftm_length_numerator/len(xdisp)

fly_away_distance = 100
def fly_away(a, b):
    if (xdisp[b]-xdisp[a])**2 + (ydisp[b]-ydisp[a])**2 < fly_away_distance:
	xvel[a]=xvel[a]+(xdisp[a]-xdisp[b])
	yvel[a]=yvel[a]+(ydisp[a]-ydisp[b])
    return xvel[a], yvel[b]

distance_for_speed_matching = 10000
sp_numerator = 0.125        
def match_nearby_speeds(a,b):
    if (xdisp[b]-xdisp[a])**2 + (ydisp[b]-ydisp[a])**2 < distance_for_speed_matching:
        xvel[a]=xvel[a]+(xvel[b]-xvel[a])*sp_numerator/len(xdisp)
	yvel[a]=yvel[a]+(yvel[b]-yvel[a])*sp_numerator/len(xdisp)
	
def move_with_velocities(a):
      xdisp[a]=xdisp[a]+xvel[a]
      ydisp[a]=ydisp[a]+yvel[a]      

def update_boids(boids):
	for i in range(len(xdisp)):
		for j in range(len(xdisp)):
		      fly_to_middle(i,j)
	              fly_away(i, j)
	              match_nearby_speeds(i,j)
	        move_with_velocities(i)
		      

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
