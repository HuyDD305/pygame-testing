class Tilemap:
    """still don't know what this class for, prob the grid
    Oxford: a thin rectangular slab of baked clay, concrete, or other material,
    used in overlapping rows for covering roofs."""

    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        #ly do ko dung list la vi nhu vay o khoang nao minh cung phai co cai gi do, nhu the rat ton spaces
        self.offgrid_titles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
