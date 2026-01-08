import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 48)
rect1_x = 400
rect2_x = 400
rect1_y = 20
rect2_y = 950
rectc_x = 500
rectc_y = 500
direction1 = 0
direction2 = 0
direction_x = 1
direction_y = 1
score1 = 0
score2 = 0 
SPEED = 3
class button:
    def __init__(self,x,y,w,h,text,color_text, alfa):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = (225,225,225,alfa)
        self.alfa = alfa
        self.text = font.render(text, False, color_text)
        self.text_rect = self.text.get_rect(center = self.rect.center)
    def draw(self,screen):
        surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.color, (0,0,self.rect.width,self.rect.height), border_radius=10)
        text_rect = self.text.get_rect(center=(self.rect.width//2, self.rect.height//2))
        surf.blit(self.text, text_rect)
        screen.blit(surf, self.rect.topleft)
    
menu_text = button(350, 50, 300, 100, "Pin-pong", (255,255,255),0)
btn_start = button(350, 450, 300, 100, "Start", (0,0,0),255)
btn_exit = button(450,850,100,50,"Quit", (255,0,0),255)
current_screen = "menu" 
while running:
    for event in pygame.event.get():
        #do hover btn
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if btn_exit.rect.collidepoint(mouse_x, mouse_y):
            btn_exit.color = (200,200,200)
        else: 
            btn_exit.color = (225,225,225)

        if btn_start.rect.collidepoint(mouse_x, mouse_y):
            btn_start.color = (200,200,200)
        else: 
            btn_start.color = (225,225,225)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if btn_start.rect.collidepoint(mouse_x, mouse_y):
                current_screen = "game"
            elif btn_exit.rect.collidepoint(mouse_x, mouse_y):
                running = False
        # logic move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                direction1 = -1
            if event.key == pygame.K_d:
                direction1 = 1
            if event.key == pygame.K_LEFT:
                direction2 = -1
            if event.key == pygame.K_RIGHT:
                direction2 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                direction1 = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                direction2 = 0

         
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    if current_screen == "menu":
        
        stars = []
        for nmb_str in range (0, 100):
            x = random.randint(0,1000)
            y = random.randint(0, 1000)
            size = random.randint(2,6)
            brightness = random.randint(50, 255)
            stars.append((x,y,size,brightness))
        for i, (x, y, size, brightness) in enumerate(stars):
            brightness = random.choice([-1,0,1])
            brightness = max(50, min(255,brightness))
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen,color,(x,y),size)
        menu_text.draw(screen)
        btn_start.draw(screen)
        btn_exit.draw(screen)
    elif current_screen == "game":
        score = button(800, 80,200,30, f"score {score1}: {score2}",(255,255,255),0)
        screen.fill("black")
        pygame.draw.circle(screen,(255,255,255),(rectc_x,rectc_y),12)
        pygame.draw.rect(screen,(255,255,255),(rect1_x,rect1_y,200,20))
        pygame.draw.rect(screen,(255,255,255),(rect2_x,rect2_y,200,20))
        rect1_x += direction1 * SPEED
        rect2_x += direction2 * SPEED
        rectc_x += direction_x * SPEED
        rectc_y += direction_y * SPEED
        if rect1_x < 0:
            rect1_x = 0
        if rect1_x >= 800:
            rect1_x = 800
        if rect2_x < 0:
            rect2_x = 0
        if rect2_x >= 800:
            rect2_x = 800
        if rectc_x >= 988:
            direction_x = -1
        if rectc_x <= 0:
            direction_x = 1
        if rect2_x <= rectc_x and rectc_x <= rect2_x + 200 and rectc_y >= rect2_y:
            direction_x *= 1 
            direction_y = -1  
        if rect1_x <= rectc_x and rectc_x <= rect1_x + 200 and rectc_y <=  rect1_y + 20:
            direction_x *= 1 
            direction_y = 1  
        if rectc_y >= 1012:
            score1 += 1
            rectc_x = 500
            rectc_y = 500
            direction_y = -1
            direction_x = 1
        if rectc_y <= -12:
            score2 += 1
            rectc_x = 500
            rectc_y = 500
            direction_y = 1
            direction_x = -1
        score.draw(screen)
            
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()