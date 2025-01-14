import pygame


class PhysicsEntity:
    """We use this class to define physic, movement of every object in our game"""
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]  # Moving 0 units per frame to the right and 0 units per frame upwards

    def rect(self):
        """Vi chung ta thay doi vi tri thuong xuyen va moi lan thay doi day ta muon co mot cai rect"""
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap,  movement=(0, 0)):
        """Changing the position of objects based on velocity or movement """

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        #Cai nay la de van toc roi xuong khong the qua 5

        self.pos[0] += frame_movement[0]
        enitity_rect = self.rect()
        self.pos[1] += frame_movement[1]

        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        # #Cai nay la de van toc roi xuong khong the qua 5

    def render(self, surf):
        """Paste the object onto the surface """
        surf.blit(self.game.assets['player'], self.pos)
