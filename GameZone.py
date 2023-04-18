class Enemy(Entity):
    def __init__(self, position=(0, 0, 0), life=100):
        super().__init__(
            model='sphere',
            color=color.red,
            position=position,
            scale=2
        )
        self.life = life

        # Create a Text object to display enemy's life at the top of the object
        self.text = Text(
            text=f'Life: {self.life}',
            origin=(0, 0),
            position=(0, self.scale_y/2+0.5, 0),
            scale=0.5,
            background=True
        )

    def take_damage(self, damage):
        self.life -= damage
        self.text.text = f'Life: {self.life}'
        if self.life <= 0:
            destroy(self)


app = Ursina()

enemy = Enemy(life=50)


def update():
    # Check if left mouse button is clicked
    if held_keys['left mouse'] and mouse.hovered_entity == enemy:
        enemy.take_damage(10)


app.run()


ceiling.add_script(SmoothFollow(
    target=player, offset=[0, 1, 0], speed=0.3))


# Create a function that destroys an object when it's clicked
def destroy_object():
    if mouse.hovered_entity:
        mouse.hovered_entity.disable()

# Create a mouse click event to destroy the object


def input(key):
    if key == 'left mouse down':
        destroy_object()
