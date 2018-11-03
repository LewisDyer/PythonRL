class Entity:
    """
    A generic object to represents players, enemies, objects, items, etc...
    """

    def __init__(self, x, y, char, colour, name, blocks = False):
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour
        self.name = name
        self.blocks = blocks

    def move(self, dx, dy):
        # Move entity by the given amount
        self.x += dx
        self.y += dy


def get_blocking_entities_at_location(entities, dest_x, dest_y):
    for entity in entities:
        if entity.blocks and entity.x == dest_x and entity.y == dest_y:
            return entity

    return None
