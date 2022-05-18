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
environmentStatic = Entity()
ground = Entity(model = 'plane',
                scale = (260, 1 ,260),
                texture = 'grass',
                texture_scale=(64,64),
                y = 0,
                collider = 'mesh', 
                )
Entity(parent = environmentStatic, position=Vec3(-117.169, 16.2564, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-96.6202, 9.70114, 131.794), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-76.1745, 16.2574, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-55.6257, 9.70214, 131.794), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-34.6672, 16.2574, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-14.1184, 9.70214, 131.794), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(6.32727, 16.2584, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(26.8761, 9.70314, 131.794), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(47.3842, 16.2584, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(67.933, 9.70314, 131.794), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(88.3787, 16.2594, 131.794), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(111.122, 9.70414, 131.794), scale=Vec3(30.1312, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(117.848, 16.2574, -132.055), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(97.2989, 9.70216, -132.109), rotation=Vec3(0, 179.849, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(76.8533, 16.2584, -132.163), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(56.3045, 9.70316, -132.217), rotation=Vec3(0, 179.849, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(35.3461, 16.2584, -132.272), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(14.7973, 9.70316, -132.326), rotation=Vec3(0, 179.849, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-5.64821, 16.2594, -132.379), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-26.197, 9.70416, -132.433), rotation=Vec3(0, 179.849, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-46.705, 16.2594, -132.487), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-67.2538, 9.70416, -132.541), rotation=Vec3(0, 179.849, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-87.6994, 16.2604, -132.595), rotation=Vec3(0, 179.849, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-110.443, 9.70516, -132.655), rotation=Vec3(0, 179.849, 0), scale=Vec3(30.1312, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(132.315, 16.2584, 118.474), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(132.242, 9.70315, 97.9254), rotation=Vec3(0, 90.2029, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(132.17, 16.2594, 77.4799), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(132.097, 9.70416, 56.9312), rotation=Vec3(0, 90.2029, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(132.023, 16.2594, 35.9729), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.95, 9.70416, 15.4241), rotation=Vec3(0, 90.2029, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.878, 16.2604, -5.02131), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.805, 9.70516, -25.5701), rotation=Vec3(0, 90.2029, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.732, 16.2604, -46.078), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.659, 9.70516, -66.6267), rotation=Vec3(0, 90.2029, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.587, 16.2614, -87.0723), rotation=Vec3(0, 90.2029, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(131.506, 9.70616, -109.815), rotation=Vec3(0, 90.2029, 0), scale=Vec3(30.1312, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.82, 16.2574, -118.831), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.821, 9.70215, -98.2819), rotation=Vec3(0, -90.0023, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.822, 16.2584, -77.8362), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.823, 9.70315, -57.2874), rotation=Vec3(0, -90.0023, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.824, 16.2584, -36.3289), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.824, 9.70315, -15.7801), rotation=Vec3(0, -90.0023, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.825, 16.2594, 4.66555), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.826, 9.70415, 25.2144), rotation=Vec3(0, -90.0023, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.827, 16.2594, 45.7224), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.828, 9.70415, 66.2713), rotation=Vec3(0, -90.0023, 0), scale=Vec3(25.8135, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.828, 16.2604, 86.7169), rotation=Vec3(0, -90.0023, 0), scale=Vec3(15.3984, 32.6865, 15.3984), model='cube', color=Color(0.44999998807907104, 0.44999998807907104, 0.44999998807907104, 1.0),),
Entity(parent = environmentStatic, position=Vec3(-132.829, 9.70515, 109.46), rotation=Vec3(0, -90.0023, 0), scale=Vec3(30.1312, 19.5572, 15.3984), model='cube', color=Color(0.33000001311302185, 0.33000001311302185, 0.33000001311302185, 1.0),)

environmentStatic.combine()
environmentStatic.collider = 'mesh'

destructible = Entity(position=Vec3(-1.95785, 0.868581, 11.956), scale=Vec3(5.39646, 1.76104, 2.99344), model='cube', collider='box', )
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
            player.gun.on_cooldown = True
            player.gun.muzzle_flash.enabled=True
            player.gun.ammo -= 1
            ammoCount.text = str(player.gun.ammo)
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
        
def reload():
    if mouse.world_point != None:
        reloadRaycast = raycast(player.world_position, player.direction, distance = 4, ignore=[player, autocannon, ground, environmentStatic, destructible])
        print(reloadRaycast.entity)
        if reloadRaycast.entity != None and hasattr(reloadRaycast.entity, 'isStaggered'):
            if reloadRaycast.entity.isStaggered:
                player.ammoCounts[player.gun.name][0] = player.ammoCounts[player.gun.name][1]
                ammoCount.text = str(player.ammoCounts[player.gun.name][0])
                destroy(reloadRaycast.entity)

def damagePlayer():
    player.health -= 5
    health.text = str(player.health)

#enemy code below

class BasicEnemy(Entity):
    def __init__(self, **kwargs):
        super().__init__( model='cube', scale_y=2, origin_y=-0.5, color=color.green,x = 15, z = 15, collider = 'box')
        #self.health_bar = Entity(y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp
        self.onCooldown = False
        self.isStaggered = False
    def hp(self):
        return self.hp

    def hp(self, value):
        self.hp = value
        if value <= 0:
            destroy(self)
            return
    
    def update(self):
        dist = distance(player.position, self.position)
        if dist > 1000:
            return
        if not self.isStaggered:
            self.look_at_2d(player.position, 'y')
            hit_info = raycast(self.world_position + Vec3(0,0,0), self.forward, ignore=(self, environmentStatic, ground))
            if player in hit_info.entities:
                if dist > 2:
                    self.position += self.forward * time.dt * 5
                elif dist <= 2:
                    if not self.onCooldown:
                        self.onCooldown = True
                        damagePlayer()
                        invoke(setattr, self, 'onCooldown', False, delay = 1)
        else:
            if hasattr(mouse.hovered_entity, 'isStaggered'):
                self.blink(color.blue, duration = 0.3)

#creates our enemies

   

app.run()
