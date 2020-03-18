import Particle
import random
import copy
import collision_detection as cd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Spread(object):
    """
    Simulates the spreading of an infection by way of physical interaction
    """
    def __init__(self,population,initial_infected,params):
        self.particles = [Particle.Particle([random.randint(params["bottom"],params["top"]),random.randint(params["left"],params["right"])],
                              [random.randint(params["min speed"],params["max speed"])*(-1)**random.randint(1,2),random.randint(params["min speed"],params["max speed"])*(-1)**random.randint(1,2)],
                              random.randint(params["min size"], params["max size"]),params) for i in range(0,population)]
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
        stats["healthy"]=count_healthy
        stats["dead"]=count_dead
        stats["cured"]=count_cured
        stats["infected"]=count_infected
        return stats

    def isolate_Particles(self,low):
        if low:
            for particle in self.particles:
                if random.random()<0.3:
                    particle.still=True
        elif not low:
            for particle in self.particles:
                if random.random()<0.7:
                    particle.still=True

    def setup_display():
        fig=plt.figure()
        ax=plt.axes()

    def run(isolate=False,low=True,display=True):
        if isolate:
            isolate_Particles(low)
        for i in range(0,self.init_inf): self.particles[i].inf=True
        self.patches = [particle.patch() for particle in self.particles]
        def init():
            return patches
        def animate(i):
            cd.detect_collisions(self.particles)
            self.stats=count_states(self.particles)

            return [particle.animate(i) for particle in particles]
        for patch in patches: ax.add_patch(patch) 
        if display:
            anim = FuncAnimation(fig,animate,init_func = init, repeat = False, interval = 1, blit = True)
            ax.axis("scaled")
            ax.set_ylim(params["bottom"],params["top"])
            ax.set_xlim(params["left"],params["top"])
            plt.axis("off")
            plt.show()
        else:
            i=0
            while stats["infected"]>0:
                i+=1
                animate(i)

