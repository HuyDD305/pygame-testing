import pygame

NEIGHBOR_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}


class Tilemap:
    """still don't know what this class for, prob the grid
    Oxford: a thin rectangular slab of baked clay, concrete, or other material,
    used in overlapping rows for covering roofs."""

    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        # ly do ko dung list la vi nhu vay o khoang nao minh cung phai co cai gi do, nhu the rat ton spaces
        self.offgrid_titles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
            # dua 10 stones va 10 grass vao trong cai dict() voi cac vi tri nhu sao
            # grass se co cac vi tri tu x = 3 -> x = 12 va y = 10
            # stone se co cac vi tri tu y = 5 -> y = 14 va x = 10

    def tiles_around(self, pos):
        """Function nay dung de tra ve tat ca cac cai tile xung quanh no"""
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSET:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        """Function nay tra ve mot cai list bao gom cac list cua cac vat xung quanh"""
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size,
                                self.tile_size))
        return rects

    def render(self, surf):
        for tile in self.offgrid_titles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']],
                      (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
            # vi cai self.game.assets[tile['type']] se tro thanh self.game.assets["grass"]]
            # sau do no nhin vao assets o trong file game, no se tra lai mot cai list
            # boi vi function load_images tra lai mot cai list nen cai variant chinh la cai index cua cai list nay
