from vpython import *
g = [vec(0,-9.8,0)]
size =[2]
pos =[vec(10,10,0)]
v = [vec(10,0,0)]
N=1
mass=[20]
trail=[True]
dt = 0.001 # time step
t=0
scene = canvas(width=800, height=800, center =vec(0,0,0), background=vec(0.5,0.5,0)) # open a window
floor = box(length=1000, height=0.01, width=10, color=color.blue) # the floor
balls=[]
for i in range(N):
    balls.append(sphere(radius = size[i], color=color.red, make_trail = trail[i], trail_radius = 0.05))
    balls[i].a=g[i]
    balls[i].v=v[i]
    balls[i].pos=pos[i]
    balls[i].m=mass[i]
#graph
vt_gd = graph(title="Velocity of Center of Mass versus time", width=600, height=450, x=0, y=600,align ='right', xtitle="t(s)", ytitle="v(m/s)")
vt = gcurve(graph=vt_gd, color=color.red)
et_gd = graph(title="Mechanical Energy versus time", width=600, height=450, x=0, y=600,align ='right', xtitle="t(s)", ytitle="Energy(J)")
Ek_curve = gcurve(graph=et_gd, color=color.red)
Eu_curve = gcurve(graph=et_gd, color=color.blue)
total_E=gcurve(graph=et_gd, color=color.green)

#Some special function
def collision(a1, a2): 
    v1prime = a1.v - 2 * a2.m/(a1.m+a2.m) *(a1.pos-a2.pos)  * dot (a1.v-a2.v, a1.pos-a2.pos) / mag(a1.pos-a2.pos)**2 
    v2prime = a2.v - 2 * a1.m/(a1.m+a2.m) *(a2.pos-a1.pos)  * dot (a2.v-a1.v, a2.pos-a1.pos) / mag(a2.pos-a1.pos)**2 
    return v1prime, v2prime  

def floor_bounce(A):
    for ball in A:
        if ball.pos.y <= ball.radius and ball.v.y < 0: # new: check if ball hits the ground
            ball.v.y = - ball.v.y
def velocity_of_Mc(A):
    total_v=vec(0,0,0)
    total_m=0
    for ball in A:
        total_v += ball.m * ball.v
        total_m += ball.m
    return total_v/total_m
def Ek(A):
    total_ek=0
    for ball in A:
        total_ek+=0.5*ball.m*ball.v.mag2
    return total_ek
def Eu(A):
    total_eu=0
    for ball in A:
        total_eu+=ball.m*9.8*ball.pos.y
    return total_eu
def plot_Energy_plot(t,enk,enu):
    Ek_curve.plot(t,enk)
    Eu_curve.plot(t,enu)
    total_E.plot(t,enk+enu)
    
while True: # until the ball hit the ground
    rate(1000) # run 1000 times per real second
    t+=dt
    for i in range(N-1): # the first N-1 molecules 
        for j in range(i+1,N): # from i+1 to the last molecules, to avoid double checking 
            limit=size[i]+size[j]
            if mag(balls[i].pos-balls[j].pos)<=limit and dot(balls[i].pos-balls[j].pos, balls[i].v-balls[j].v)<=0: 
                balls[i].v, balls[j].v = collision(balls[i],balls[j])
    floor_bounce(balls)
    for ball in balls:
        ball.v+=ball.a*dt
    for ball in balls: 
        ball.pos += ball.v*dt
    vt.plot(t,mag(velocity_of_Mc(balls)))
#    plot_Energy_plot(t,Ek(balls),Eu(balls))


    


