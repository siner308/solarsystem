from visual import *
from visual.graph import *

class scene:
	#make scene
	def make(self, scene_name, scene_width, scene_height, scene_x,scene_y,scene_z):
		scene_name = display(title = scene_name, width = scene_width, height = scene_height, center = (scene_x,scene_y,scene_z))


class planet():
    
    #make planet
    def make(self, planet_name, planet_pos_x, planet_pos_y, planet_pos_z, planet_radius, planet_color_r, planet_color_g, planet_color_b, trail_boolean):
        planet_name = sphere(pos = (planet_pos_x, planet_pos_y, planet_pos_z), radius = planet_radius*5, color = (planet_color_r, planet_color_g, planet_color_b), make_trail = trail_boolean)
        
    #speed of planet
    def speed(self, speed_x, speed_y, speed_z):
        self.vector = (speed_x, speed_y, speed_z)

    #info
    #gd = gdisplay(title = "mercury" , x = 800, y=0, width = 600, height=600, foreground = color.black, background = color.white, xmax = 20000, xmin = 2, ymax =1010 , ymin = 0)

    def info(self, graph_name):
        self.gd = gdisplay(title = graph_name, x = 800, y = 0, width = 600, height = 600, foreground = color.black, background = color.white, xmax = 20000, xmin = 2, ymax = 1010, ymin = 0)
        self.f1 = gcurve(color = (1, 0.5, 0))
        self.t = 0
        self.graph1 = gdisplay()
    		
    def movePlanet(self, planet_name, const_gravity):
        #self.pos = self.pos + planet_vector
        planet_name.pos = planet_name.pos + planet_name.vector
        self.distance = (self.planet_pos_x**2 + self.planet_pos_y**2 + self.planet_pos_z**2)**0.5
        self.radial_vector = (self.pos - sun.pos)/self.distance
        self.force_gravity = (const_gravity*self.radial_vector)/(self.distance**2)
        self.vector = self.vector + self.force_gravity
        self.plot(pos = (t, mag(self.vector)))
        
class ring(planet):
    def make(self, ring_name, planet_pos, ring_axis_x, ring_axis_y, ring_axis_z, ring_radius, ring_color_r, ring_color_g, ring_color_b, ring_thickness):
        ring_name = ring(pos = planet_pos, axis = (ring_axis_x, ring_axis_y, ring_axis_z), radius = ring_radius*10, color = (ring_color_r, ring_color_g, ring_color_b), thickness = ring_thickness)
         
# scene reset period
value_rate = 100

# const_gravity
const_gravity_mercury = -0.055*502950000000
const_gravity_venus =  -0.815*31095000000
const_gravity_earth = -1.000*26095000000
const_gravity_mars = -0.1*260950000000
const_gravity_jupiter = -0.1*270950000000
const_gravity_saturn = -0.1*260950000000
const_gravity_uranus = -0.1*260950000000
const_gravity_neptune = -0.1*260950000000
const_gravity_moon = -0.012*26095000000000000
const_gravity_saturn_ring = -0.1*260950000000

# position variable
const_pos = 1.5*(10**5)

# set object
# set scene
scene = scene()
# set planets
sun = planet()
mercury = planet()
venus = planet()
earth = planet()
mars = planet()
jupiter = planet()
saturn = planet()
uranus = planet()
neptune = planet()
moon = planet()
saturn_ring = ring()

# make scene
scene.make('solarsystem', 1000, 1000, 0,0,0)

# make planets, sun, moon, ring
sun.make('sun', 0, 0, 0, 6957, 1, 0.3, 0, 0)
mercury.make('mercury', 0.4*const_pos, 0, 0, 244.0, 0.5, 0.5, 0.5, 1)
venus.make('venus',0.7*const_pos, 0, 0, 605.2, 1, 0.5, 0, 1)
earth.make('earth', 1*const_pos, 0, 0, 637.8, -7, 0.1, -0.1, 1)
mars.make('mars', 1.5*const_pos, 0, 0, 339.0, 1, 0.2, 0, 1)
jupiter.make('jupiter', 5.2*const_pos, 0, 0, 6991.1, 1, 0.8, 0.5, 1)
saturn.make('saturn', 9.5*const_pos, 0, 0, 5823.2, 1, 0.8, 0, 1)
uranus.make('uranus', 19.2*const_pos, 0, 0, 2536.2, 0, 0.8, 1, 1)
neptune.make('neptune', 30*const_pos, 0, 0, 2462.2, 0, 0.3, 1, 1)
moon.make('moon', 30*const_pos + (384.4*10), 0, 0, 160, 0.6, 0.6, 0.6, 1)
#saturn_ring.make('saturn_ring', saturn.pos, 0, 0, 1, 10000, 1, 0.8, 0.5, 1000)

# set vector
mercury.speed(0,473.6,0)
venus.speed(0,350.2,0)
earth.speed(0,297.8,0)
mars.speed(0,240.8,0)
jupiter.speed(0,130.6,0)
saturn.speed(0,96.39,0)
uranus.speed(0,67.95,0)
neptune.speed(0,54.3,0)
moon.speed(0,1002,0)
#saturn_ring.speed(0,96.39,0)

# set info to graph
mercury.info('mercury')
venus.info('venus')
earth.info('earth')
mars.info('mars')
jupiter.info('jupiter')
saturn.info('saturn')
uranus.info('uranus')
neptune.info('neptune')
moon.info('moon')

rate(value_rate)                              #speed of scene       
flag = 1
while(flag):  
    mercury.movePlanet(mercury, const_gravity_mercury)
    venus.movePlanet('venus', const_gravity_venus)
    earth.movePlanet('earth', const_gravity_earth)
    mars.movePlanet('mars', const_gravity_earth)
    jupiter.movePlanet('jupiter', const_gravity_jupiter)
    saturn.movePlanet('saturn', const_gravity_jupiter)
    uranus.movePlanet('uranus', const_gravity_uranus)
    neptune.movePlanet('neptune', const_gravity_neptune)
    moon.movePlanet('moon', const_gravity_neptune)
    #saturn_ring.movePlanet('saturn_ring', const_gravity_saturn_ring)
    
    if(scene.waitfor('keydown')):
        flag = 0
