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

xs,ys,xvs,yvs=boids

length_numerator = 0.01
def fly_to_middle(a,b):
    xvs[a]=xvs[a]+(xs[b]-xs[a])*length_numerator/len(xs)
    yvs[a]=yvs[a]+(ys[b]-ys[a])*length_numerator/len(xs)

def fly_away(a, b):
    if (xs[b]-xs[a])**2 + (ys[b]-ys[a])**2 < 100:
	xvs[a]=xvs[a]+(xs[a]-xs[b])
	yvs[a]=yvs[a]+(ys[a]-ys[b])
    return xvs[a], yvs[b]
    
def match_nearby_speeds(a,b):
    if (xs[b]-xs[a])**2 + (ys[b]-ys[a])**2 < 10000:
        xvs[a]=xvs[a]+(xvs[b]-xvs[a])*0.125/len(xs)
	yvs[a]=yvs[a]+(yvs[b]-yvs[a])*0.125/len(xs)
	
def move_with_velocities(a):
      xs[a]=xs[a]+xvs[a]
      ys[a]=ys[a]+yvs[a]      

def update_boids(boids):
	for i in range(len(xs)):
		for j in range(len(xs)):
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
