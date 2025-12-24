import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 48)

class button:
    def __init__(self,x,y,w,h,text):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = (255,255,255)
        self.text = font.render(text, False, (255,100,55))
        self.text_rect = self.text.get_rect(center = self.rect.center)
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius= 10)
        screen.blit(self.text, self.text_rect)
btn_start = button(350, 650, 300, 100, "Start")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    btn_start.draw(screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()