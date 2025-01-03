import pygame, sys


class Game:
    def __init__(self):
        pygame.init()  # Initiates pygame
        pygame.display.set_caption("Ninja game")
        self.screen = pygame.display.set_mode((640, 480))  # build the screen
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")  # Cai nay de load anh
        self.img.set_colorkey((0, 0, 0))  # Bat cu cai mau nao duoc dung trong cai function nay se deu transparent
        self.img_pos = [160, 260]
        self.movement = [False, False]
        self.up_down = [False, False]
        self.collision_area = pygame.Rect(50, 50, 300, 50)  # tao mot cai hinh chu nhat phuc vu cho collision

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            # self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            # self.img_pos[0] += (self.up_down[1] - self.up_down[0]) * 5
            # self.screen.blit(self.img, self.img_pos)  # day la toa do(x = 100, y = 200)(top left la (0, 0)),blit dung de paste cai surface nay len surface khac

            # tao mot cai rect nhung cai rect nay co the hieu nhu la logic de phat hien collision'
            # cai rect nay se they doi vi tri theo cai img
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                # ve truc tiep len cai screen surface chu ko phai la tao them mot cai surface rieng biet nhu blit, co nghia la ko di chuyen duoc
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.img_pos[0] += (self.up_down[1] - self.up_down[0]) * 5
            self.screen.blit(self.img,
                             self.img_pos)  # day la toa do(x = 100, y = 200)(top left la (0, 0)),blit dung de paste cai surface nay len surface khac

            for event in pygame.event.get():  # Cai nay se tra lo mot cai list gom cac event
                if event.type == pygame.QUIT:  # Moi cai event thi se co mot cai type, day la code de dung dau X thoat chuong trinh
                    pygame.quit()  # Tat pygame
                    sys.exit()  # Tat system

                if event.type == pygame.KEYDOWN:  # day la de biet la co key dang duoc nhan
                    if event.key == pygame.K_UP:  # day la de check xem dang nhan key gi
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT:
                        self.up_down[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.up_down[1] = True

                if event.type == pygame.KEYUP:  # day la de biet la co key dang duoc lift
                    if event.key == pygame.K_UP:  # day la de check xem dang nhan key gi
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT:
                        self.up_down[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.up_down[1] = False

            pygame.display.update()
            # den buoc nay se hien len mot cai window nhung vi neu mot cai app ma ko co input
            # thi no se dung lai
            self.clock.tick(60)


if __name__ == "__main__":  # co the hieu khi mot cai program chay no se co mot cai bien la __name__
    start_game = Game()
    start_game.run()
