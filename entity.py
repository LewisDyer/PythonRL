class Entity:
    """
    A generic object to represents players, enemies, objects, items, etc...
    """

    def __init__(self, x, y, char, colour):
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour

    def move(self, dx, dy):
        # Move entity by the given amount
        self.x += dx
        self.y += dy
