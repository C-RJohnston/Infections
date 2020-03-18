def grid_partition(particles):
        top_right=[]
        top_left=[]
        bottom_right=[]
        bottom_left=[]
        for particle in self.particles:
            if(particle.pos[1]>=params["top"]/2):
                if(particle.pos[0]>=params["right"]/2):
                    top_right.append(particle)
                else:
                    top_left.append(particle)
            elif(particle.pos[0]>=params["right"]/2):
                bottom_right.append(particle)
            else:
                bottom_left.append(particle)
        return top_right,top_left,bottom_right,bottom_left


def detect_collisions(particles):
    quads=grid_partition(particles)
    for i in range(0,len(particles)):
        for quad in quads:
            if particles[i] in quad:
                temp = copy.copy(quad)
                temp.remove(particles[i])
                for j in range(0,len(temp)):
                    particles[i].check_collision(temp[j])
