# implementation of Spaceship - program template for RiceRocks.
import simplegui
import math
import random

# globals for user interface
width = 800 # canvas width
height = 600 # canvas height
score = 0
lives = 3
time = 0
started = False # used to decide whether to display the splash screen
explosion_group = set([]) # holds the explosions according to collisions in collide_group

def restart():
    global started, rock_group, timer, score, lives, time, my_ship, soundtrack
    time = 0
    started = False # allows splash screen to be shown
    rock_group = set([]) # remove rocks
    timer.stop() # stop spawning rocks - they only spawn when the timer increments
    soundtrack.rewind() # stops the sound at the end of a game
    my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info) # creates new ship in center of canvas
    return

class ImageInfo: # provided with the code
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

# helper function to update and draw group sprites
def process_sprite_group(canvas, group):
    for item in group:
        item.update() # make sure we are drawing the latest version
        item.draw(canvas) # calls the item's (sprite) draw method
        # if update returns false then the sprite is too old
        if item.update() == False:
            group.remove(item)        
    return
    
# helper function to detect collisions between a sprite and a group
def group_collide(group, other_object):
    global explosion_group, explosion_image, explosion_sound
    remove_set = set([]) # used to store items to be removed. Can't remove as we go: bad form when dealing with sets
    for item in group:
        if item.collide(other_object):
            remove_set.add(item) # e.g. if item is ship then remove rock
            # Where there's a collison there's a bang! Add a new bang item - this will effectively swap places with the other_object
            # Values for the bang are those of the item being removed (blown up)
            a_bang = Sprite(item.pos, item.vel, 0, item.angle_vel, explosion_image, explosion_info, explosion_sound)
            a_bang.animated = True # It needs to be an animated sprite to go through the 24 tiled images when being drawn
            explosion_group.add(a_bang) # explosion_group is drawn with the canvas
    group.difference_update(remove_set) # standard set function to remove items in remove_set from 'group'
    return len(remove_set) # tested later to see if there was a collision. i.e. if this is >0

# Helper function to detect collisions between groups of missiles and asteroids
def group_group_collide(group, other_group):
    remove_set = set([])
    total_collisions = 0 # this is the value returned and tested to see if >0 i.e. there has been a collision
    collisions = 0
    for source in group:        
        collisions += group_collide(other_group, source) # a 'sub-loop' to test the current loop item against other objects
        if collisions > 0:
            remove_set.add(source) # 'source' has collided and needs to be removed           
            total_collisions += collisions #            
    group.difference_update(remove_set) # removes collided items from 'group'    
    return total_collisions

# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
            
        self.vel[0] *= .99
        self.vel[1] *= .99

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       
    def increment_angle_vel(self):
        self.angle_vel += .05
        
    def decrement_angle_vel(self):
        self.angle_vel -= .05
        
    def shoot(self):
        global missile_group # provided by coursera 
        forward = angle_to_vector(self.angle) # returns coordinate values of angle
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        missile_sound.play()
    #the following are required to help with collision detection 
    def collide(self, other_object):
        # dist(x,y) is a function to return distance between 2 objects
        if dist(self.pos, other_object.pos) <= self.radius + other_object.radius:
            return True
        return False
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            image_width = self.image_size[0] # image_width is also the distance between image tiles
            image_horizontal = self.image_center[0] + (image_width * self.age) # horizontal position of new image
            image_vertical = self.image_center[1] # No change to vertical position because image is on row of tiles
            image_location = [image_horizontal, image_vertical] # this is the new 'centre'
            canvas.draw_image(self.image, image_location, self.image_size,
                          self.pos, self.image_size, self.angle)
        else:
             canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
                       
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        #Is the sprite still alive. Used for the missiles
        self.age += 1
        if self.age <= self.lifespan:
            return True
        else:
            return False
    #the following are required to help with collision detection 
    def collide(self, other_object):
        if dist(self.pos, other_object.pos) <= self.radius + other_object.radius:
            return True
        return False
    def get_position(self):
        return self.pos
    def get_radius(self):
        return self.radius
    
        
# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score
    lives = 3
    score = 0
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        timer.start() # needed to respawn rocks
        started = True

def draw(canvas):
    global time, started, lives, score
    # If ship hits a rock lose a life
    if group_collide(rock_group, my_ship) > 0:
        lives -= 1
    if lives <= 0:
        restart()
        
    # If a missile hits a rock increase the score
    score += group_group_collide(missile_group, rock_group)
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])

    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    process_sprite_group(canvas, rock_group)
    process_sprite_group(canvas, missile_group)
    process_sprite_group(canvas, explosion_group)
    
    # update ship and sprites
    my_ship.update()
    #a_rock.update()
    #a_missile.update()

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [width/2, height/2], 
                          splash_info.get_size())

# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len(rock_group) >= 12:
        # print rock_group
        return
    rock_pos = [random.randrange(0, width), random.randrange(0, height)]
    difficulty = score / 5 #as you get better it gets harder
    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    rock_vel[0] *= difficulty
    rock_vel[1] *= difficulty
    rock_avel = random.random() * .2 - .1
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
    rock_group.add(a_rock)
                
# initialize stuff
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])


# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
