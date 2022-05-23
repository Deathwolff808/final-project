from ursina import *

app = Ursina()
class MenuButton(Button):
    def __init__(self, text='', **kwargs):
        super().__init__(text, scale=(.25, .075), highlight_color=color.azure, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key ,value)


# button_size = (.25, .075)
button_spacing = .075 * 1.25
menu_parent = Entity(parent=camera.ui, y=.15)
main_menu = Entity(parent=menu_parent)
load_menu = Entity(parent=menu_parent)
options_menu = Entity(parent=menu_parent)

state_handler = Animator({
    'main_menu' : main_menu,
    }
)

def start_game():
    menu_parent.enabled = False
    import finalprojectemanuelver
    finalprojectemanuelver.play_game()

# main menu content
main_menu.buttons = [
    MenuButton('start', on_click=start_game),
    MenuButton('quit', on_click=Sequence(Wait(.01), Func(sys.exit))),
]
for i, e in enumerate(main_menu.buttons):
    e.parent = main_menu
    e.y = (-i-2) * button_spacing






# animate the buttons in nicely when changing menu
for menu in (main_menu,):
    def animate_in_menu(menu=menu):
        for i, e in enumerate(menu.children):
            e.original_x = e.x
            e.x += .1
            e.animate_x(e.original_x, delay=i*.05, duration=.1, curve=curve.out_quad)

            e.alpha = 0
            e.animate('alpha', .7, delay=i*.05, duration=.1, curve=curve.out_quad)

            if hasattr(e, 'text_entity'):
                e.text_entity.alpha = 0
                e.text_entity.animate('alpha', 1, delay=i*.05, duration=.1)

    menu.on_enable = animate_in_menu


background = Entity(parent=menu_parent, model='quad', texture='shore', scale=(camera.aspect_ratio,1), color=color.white, z=1, world_y=0)

app.run()


