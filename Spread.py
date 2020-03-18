import Particle
import random
import collision_detection as cd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Spread(object):
    """
    Simulates the spreading of an infection by way of physical interaction
    """
    def __init__(self,population,initial_infected,params):
        self.params=params
        self.particles = [Particle.Particle([random.randint(self.params["bottom"],self.params["top"]),random.randint(self.params["left"],self.params["right"])],
                              [random.randint(self.params["min speed"],self.params["max speed"])*(-1)**random.randint(1,2),random.randint(self.params["min speed"],self.params["max speed"])*(-1)**random.randint(1,2)],
                              random.randint(self.params["min size"], self.params["max size"]),self.params) for i in range(0,population)]
        self.stats = {"healthy":population,"infected":initial_infected,"cured":0,"dead":0}
        self.num=population
        self.init_inf=initial_infected
        self.patches=[]

    def count_states(self):
        count_infected=0
        count_cured=0
        count_dead=0
        count_healthy=0
        for particle in self.particles:
            if(particle.inf):
                count_infected+=1
            elif(particle.cured):
                count_cured+=1
            elif(particle.dead):
                count_dead+=1
            else:
                count_healthy+=1
        self.stats["healthy"]=count_healthy
        self.stats["dead"]=count_dead
        self.stats["cured"]=count_cured
        self.stats["infected"]=count_infected
        return self.stats

    def isolate_Particles(self,low):
        if low:
            for particle in self.particles:
                if random.random()<0.3:
                    particle.still=True
        elif not low:
            for particle in self.particles:
                if random.random()<0.7:
                    particle.still=True

    def init_anim(self):
        return self.patches

    def animate(self,i):
        cd.detect_collisions(self.particles,self.params)
        self.stats=self.count_states()
        return [particle.animate(i) for particle in self.particles]

    def setup_display(self):
        fig=plt.figure()
        ax=plt.axes()
        ax.axis("scaled")
        ax.set_ylim(self.params["bottom"],self.params["top"])
        ax.set_xlim(self.params["left"],self.params["top"])
        plt.axis("off")
        self.patches = [particle.patch() for particle in self.particles]
        for patch in self.patches: ax.add_patch(patch)
        return fig,ax

    def run(self,isolate=False,low=True,display=True):
        if isolate:
            isolate_Particles(low)
        fig,ax=self.setup_display()
        for i in range(0,self.init_inf): self.particles[i].inf=True
        anim = FuncAnimation(fig,self.animate,init_func = self.init_anim, repeat = False, interval = 1, blit = True)
        plt.show()
