import random
import matplotlib.pyplot as plt
class Particle(object):
    """
    Single particle/person. Can have any of 5 states
    Uninfected
    Infected
    Cured
    Dead
    Stationary
    """
    def __init__(self,position,velocity,radius,params):
        self.pos=position
        self.vel=velocity
        self.rad=radius
        self.inf=False
        self.cured=False
        self.dead=False
        self.still=False
        self.time_inf=0
        self.params=params

    #set default string
    def __str__(self):
        return f"Person: pos = {self.pos}, vel = {self.vel}, size = {self.rad}, infected = {self.inf}, cured = {self.cured}, dead = {self.dead}, isolating = {self.still}"

    #handles when the particle bumps into another, makes them move apart and probabalistically infects the particle
    def collide(self,particle):
        vel=particle.vel
        particle.vel=[self.vel[0]*-1,self.vel[1]*-1]
        self.vel=[vel[0]*-1,vel[1]*-1]
        if(not self.cured):
            if(not self.dead):
                if(particle.inf):
                    if(not self.inf):
                        if(random.random()<self.params["inf_prob"]):
                            self.inf=True

    #moves the particle in a straight line, transfers particle at an edge to opposite edge
    def move(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        if(self.pos[0]>self.params["top"]):
            self.pos[0]=self.params["bottom"]
        if(self.pos[0]<self.params["bottom"]):
            self.pos[0]=self.params["top"]
        if(self.pos[1]<self.params["left"]):
            self.pos[1]=self.params["right"]
        if(self.pos[1]>self.params["right"]):
            self.pos[1]=self.params["left"]

    #to be called once per timestep, moves the particle if not isolating and checks to see if the particle has died or become immune
    def update(self,dt):
        if(not self.still):
            if(not self.dead):
                self.move()
        if(self.inf):
            self.time_inf+=dt
            if(self.time_inf>=self.params["recovery period"]):
                if(random.random()<self.params["fatality"]):
                    self.dead=True
                    self.inf=False
                    self.cured=False
                else:
                    self.inf=False
                    self.cured=True
                    self.dead=False

    def patch(self):
        self.patch=plt.Circle(self.pos,self.rad,color='b',animated=True)
        return self.patch

    def check_collision(self,particle):
        if (((self.pos[0]-particle.pos[0])**2+(self.pos[1]-particle.pos[1])**2)**0.5<self.rad):
                self.collide(particle)

    def animate(self, i):
        self.update(i)
        self.patch.center = (self.pos[0],self.pos[1])
        if(self.inf):
            self.patch.set_color("r")
        elif(self.cured):
            self.patch.set_color("g")
        elif(self.dead):
            self.patch.set_color("gray")
        return self.patch
