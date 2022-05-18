from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.editor import *
from ursina.editor import level_editor
from random import randrange

#opens window part 1
app = Ursina()

#environment stuff gets done here

#lighting
#creates the ground
ground = Entity(model = 'plane',
                scale = (250, 1 ,250),
                texture = 'grass',
                texture_scale=(64,64),
                y = 0,
                collider = 'plane'
                )

#prevents you from falling through the ground by making you collide with the floor
BoxCollider(ground)
#makes some random blocks
box = Entity(model = 'cube', scale = 2, texture = 'white_cube', x = 5, y = 1, collider = 'box')
box2 = Entity(model = 'cube', scale = 4, texture = 'rainbow', x = 9, y = 2, collider = 'box')
box3 = Entity(model = 'cube', scale = 6, texture = 'brick', x = 14, y = 3, collider = 'box')
#scene light source diabled for now may be readded later but for now i want to keep things kinda dark

sun = DirectionalLight(shadows = True, position = (100, 100, 100))
sun.look_at(Vec3(1,0,1))
#skybox
Sky()

#player code below
'''
experimental code for seperating the player code from everything else
#makes the autocannon weapon for the player
autocannon = Entity(model='cube',
                 parent=camera,
                 position=(.5,-.25,.25),
                 scale=(.3,.2,1),
                 origin_z=-.5,
                 color=color.red,
                 on_cooldown=False,
                 name = 'autocannon',
                 ammo = 15,
                 maxAmmo = 15
                 )
#makes player
player = Player(gun = autocannon, weaponList = [autocannon])
'''




#create player entity
player = FirstPersonController(height = 2, speed = 15)
#provides collider for player
player.collider = BoxCollider(player)
#sets player health
player.health = 100
#makes the autocannon weapon for the player
autocannon = Entity(model='cube',
                 parent=camera,
                 position=(.5,-.25,.25),
                 scale=(.3,.2,1),
                 origin_z=-.5,
                 color=color.red,
                 on_cooldown=False,
                 name = 'autocannon',
                 ammo = 15,
                 maxAmmo = 15
                 )
player.gun = autocannon
player.gun.muzzle_flash = Entity(parent=player.gun,
                                  z=1,
                                  world_scale=.5,
                                  model='quad',
                                  color=color.yellow,
                                  enabled=False
                                  )
#list of the players weapons so when more are added we can do some stuff more easily
player.weaponList = [autocannon]
#player UI code
ammoCount = Text(scale_override = 2,
            text = str(player.gun.ammo)
            )
ammoCount.position = (0.8,-0.45)
health = Text(text = str(player.health))
health.position = (-0.8,-0.45)
health.scale_override = 2
def input(key):
    if key == 'escape':
        quit()
    if key == 'r':
        Func(reload(), delay = 0.5)
    if key == 'l':
        BasicEnemy()

def shoot():
    if player.gun == player.weaponList[0]:
        if not player.gun.on_cooldown and player.gun.ammo > 0:
            from ursina.prefabs.ursfx import ursfx
            player.gun.on_cooldown = True
            player.gun.muzzle_flash.enabled=True
            player.gun.ammo -= 1
            ammoCount.text = str(player.gun.ammo)
            ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
            invoke(player.gun.muzzle_flash.disable, delay=.05)
            invoke(setattr, player.gun, 'on_cooldown', False, delay=.2)
            if hasattr(mouse.hovered_entity, 'hp'): #code that ive removed for now: mouse.hovered_entity and 
                mouse.hovered_entity.hp -= 10
                mouse.hovered_entity.blink(color.red)
                if mouse.hovered_entity.hp == 0:
                    destroy(mouse.hovered_entity)
            '''
            totally not stolen code for a bullet animation that im unsure about implementing
            
            bullet = Entity(parent=player.gun, model='cube', scale=.1, color=color.black)
            bullet.world_parent = scene
            bullet.animate_position(bullet.position+(bullet.forward*50), curve=curve.linear, duration=1)
            destroy(bullet, delay=1)
            '''

def update():
    if held_keys['left mouse']:
        shoot()
        
#this will be removed soon
def reload():
    player.gun.ammo = player.gun.maxAmmo
    ammoCount.text = str(player.gun.ammo)

def damagePlayer():
    player.health -= 5
    health.text = str(player.health)

#enemy code below

class BasicEnemy(Entity):
    def __init__(self, **kwargs):
        super().__init__( model='cube', scale_y=2, origin_y=-.5, color=color.green, collider='box', x = 15, z = 15)
        #self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp
        self.onCooldown = False
    
    def hp(self):
        return self.hp

    def hp(self, value):
        self.hp = value
        if value <= 0:
            destroy(self)
            return
    
    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.look_at_2d(player.position, 'y')
        hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
        if hit_info.entity == player:
            if dist > 2:
                self.position += self.forward * time.dt * 5
            elif dist <= 2:
                if not self.onCooldown:
                    self.onCooldown = True
                    damagePlayer()
                    invoke(setattr, self, 'onCooldown', False, delay = 1)
                    
                        
                


#creates our enemies
#BasicEnemy() disabled for now
   

app.run()
