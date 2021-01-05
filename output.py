from vpython import *
g = [vec(0,-9.8,0)]
size =[1]
pos =[vec(0,0,0)]
v = [vec(0,0,0)]
N=1
dt = 0.001 # time step
scene = canvas(width=800, height=800, center =vec(0,0,0), background=vec(0.5,0.5,0)) # open a window
#ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball
balls=[]
for i in range(N):
    balls.append(sphere(radius = size[i], color=color.red, make_trail = True, trail_radius = 0.05))
    balls[i].a=g[i]
    balls[i].v=v[i]
    balls[i].pos=pos[i]
    balls[i].m=1


while True: # until the ball hit the ground
    rate(1000) # run 1000 times per real second
    for ball in balls:
        ball.v+=ball.a*dt
    for ball in balls: 
        ball.pos += ball.v*dt


