import pygame


class PhysicsEntity:
    """We use this class to define physic, movement of every object in our game"""
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]  # Moving 0 units per frame to the right and 0 units per frame upwards

    def update(self, movement=(0, 0)):
        """Changing the position of objects based on velocity or movement """
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surf):
        """Paste the object onto the surface """
        surf.blit(self.game.assets['player'], self.pos)
