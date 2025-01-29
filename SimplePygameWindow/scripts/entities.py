import pygame


class PhysicsEntity:
    """We use this class to define physic, movement of every object in our game"""

    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)  # change a tuple to a list
        self.size = size
        self.velocity = [0, 0]  # Moving 0 units per frame to the right and 0 units per frame upwards
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        """Vi chung ta thay doi vi tri thuong xuyen va moi lan thay doi day ta muon co mot cai rect"""
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        """Changing the position of objects based on velocity or movement """
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # Horizontal movement
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                aTest = tilemap.tilemap['10;9']['pos']
                pos1 = aTest[0] * tilemap.tile_size
                pos2 = aTest[1] * tilemap.tile_size
                if rect.x == pos1 and rect.y == pos2:
                    print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                print(f"before x: {self.pos[0]}")
                print(entity_rect.x)
                self.pos[0] = entity_rect.x
                print(f"after x: {self.pos[0]}")
                print(entity_rect.x)

        # Vertical movement
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                print(f"before y: {self.pos[1]}")
                print(entity_rect.y)
                self.pos[1] = entity_rect.y
                print(f"after y: {self.pos[1]}")
                print(entity_rect.y)

        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        # #Cai nay la de van toc roi xuong khong the qua 5

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, surf):
        """Paste the object onto the surface """
        surf.blit(self.game.assets['player'], self.pos)
