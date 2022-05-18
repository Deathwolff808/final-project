from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#wip
class Player(FirstPersonController):
    def __init__(self, **kwargs):
        player = FirstPersonController(height = 2, speed = 15)
        player.collider = BoxCollider(player)
        #player.gun = starter
        #player.gun.muzzle_flash = Entity(parent=player.gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)
        '''
    #makes the starter weapon for the player
        starter = Entity(model='cube',
                         parent=camera,
                         position=(.5,-.25,.25),
                         scale=(.3,.2,1),
                         origin_z=-.5,
                         color=color.red,
                         on_cooldown=False,
                         name = 'starter',
                         ammo = 15,
                         maxAmmo = 15
                         )
        self.gun = starter
        self.gun.muzzle_flash = Entity(parent=player.gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)
        #list of the players weapons so when more are added we can do some stuff more easily
        self.weaponList = [starter]

        def input(self, key):
            if key == 'escape':
                quit()
            if key == 'r':
                Func(reload(), delay = 0.5)
        '''

    def shoot(self):
        if self.gun == self.weaponList[0]:
            if not self.gun.on_cooldown and self.gun.ammo > 0:
                from ursina.prefabs.ursfx import ursfx
                self.gun.on_cooldown = True
                self.gun.muzzle_flash.enabled=True
                self.gun.ammo -= 1
                ammoCount.text = str(self.gun.ammo)
                ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
                invoke(self.gun.muzzle_flash.disable, delay=.05)
                invoke(setattr, self.gun, 'on_cooldown', False, delay=.2)
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
    #this will be removed soon
    def reload():
        self.gun.ammo = self.gun.maxAmmo

