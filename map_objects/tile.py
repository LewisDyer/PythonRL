class Tile:
    """
    A tile on a map. It may or may not be blocked, and it may or may not block sight.
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        # unless given otherwise, we assume a blocked tile also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight