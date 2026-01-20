import pygame
import random

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_LEVEL = SCREEN_HEIGHT * 0.8
FPS = 60

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255)) #Белый прямоугольник для динозавра
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = GROUND_LEVEL - self.rect.height
        self.is_jumping = False
        self.jump_vel = 0
    
    def update(self):
        if self.is_jumping:
            self.jump_vel -= 1
            self.rect.y += self.jump_vel
            
            if self.rect.bottom >= GROUND_LEVEL:
                self.rect.bottom = GROUND_LEVEL
                self.is_jumping = False
                self.jump_vel = 0

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill((0, 255, 0)) #Зелёный прямоугольник для кактуса
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 300)
        self.rect.y = GROUND_LEVEL - self.rect.height
        
    def update(self):
        self.rect.x -= 5
        if self.rect.right <= 0:
            self.kill()  #Удаляем кактус, вышедший за пределы экрана

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dino = Dino()
    all_sprites = pygame.sprite.Group(dino)
    obstacles = pygame.sprite.Group()
    
    score = 0
    game_over = False
    font = pygame.font.SysFont(None, 36)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dino.is_jumping:
                    dino.is_jumping = True
                    dino.jump_vel = 15
                    
        all_sprites.update()
        
        # Добавляем новые препятствия случайным образом
        if len(obstacles) < 3 and random.random() < 0.01:
            obstacle = Cactus()
            obstacles.add(obstacle)
            all_sprites.add(obstacle)
        
        # Проверка столкновений
        hits = pygame.sprite.spritecollide(dino, obstacles, False)
        if hits:
            game_over = True
        
        # Отображение очков
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Очистка экрана
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0, 0, 0), (0, GROUND_LEVEL), (SCREEN_WIDTH, GROUND_LEVEL), 2)
        
        # Рисование всех объектов
        all_sprites.draw(screen)
        
        # Увеличение счёта
        score += 1
        
        pygame.display.flip()
        clock.tick(FPS)
    
    print("Game Over!")
    pygame.quit()

if __name__ == "__main__":
    main()
