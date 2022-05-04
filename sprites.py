import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def getSprite(self, x, y, width, height, scale):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        scaledSprite = pygame.transform.scale(sprite, (width*scale, height*scale))
        scaledSprite.set_colorkey(BLACK)
        return scaledSprite

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.allSprites, self.game.players
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        # self.width = VI_SIZE
        # self.height = VI_SIZE

        self.xChange = 0
        self.yChange = 0

        self.facing = 'down'
        self.animationLoop = 1

        # imageToLoad = pygame.image.load("img/smallVi.png")
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.set_colorkey(BLACK)
        # self.image.blit(imageToLoad, (0, 0))

        self.image = self.game.viSpritesheet.getSprite(3, 0, VI_WIDTH, TEMPLATE_HEIGHT, SCALE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.downAnimations = [self.game.viSpritesheet.getSprite(3, 0, VI_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.viSpritesheet.getSprite(35, 0, VI_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.viSpritesheet.getSprite(67, 0, VI_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.viSpritesheet.getSprite(99, 0, VI_WIDTH, TEMPLATE_HEIGHT, SCALE)]

    def update(self):

        self.movement()
        self.animate()
        self.collideEnemy()

        self.rect.x += self.xChange
        self.collideWalls('x')
        self.rect.y += self.yChange
        self.collideWalls('y')

        self.xChange = 0
        self.yChange = 0
        # print(self.rect.x, self.rect.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.game.camera:
                for sprite in self.game.allSprites:
                    sprite.rect.x += PLAYER_SPEED
            self.xChange -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.game.camera:
                for sprite in self.game.allSprites:
                    sprite.rect.x -= PLAYER_SPEED
            self.xChange += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.game.camera:
                for sprite in self.game.allSprites:
                    sprite.rect.y += PLAYER_SPEED
            self.yChange -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.game.camera:
                for sprite in self.game.allSprites:
                    sprite.rect.y -= PLAYER_SPEED
            self.yChange += PLAYER_SPEED
            self.facing = 'down'

    def collideEnemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False
            self.game.malding = True

    def collideWalls(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.xChange > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    if self.game.camera:
                        for sprite in self.game.allSprites:
                            sprite.rect.x += PLAYER_SPEED
                if self.xChange < 0:
                    self.rect.x = hits[0].rect.right
                    if self.game.camera:
                        for sprite in self.game.allSprites:
                            sprite.rect.x -= PLAYER_SPEED

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.yChange > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    if self.game.camera:
                        for sprite in self.game.allSprites:
                            sprite.rect.y += PLAYER_SPEED
                if self.yChange < 0:
                    self.rect.y = hits[0].rect.bottom
                    if self.game.camera:
                        for sprite in self.game.allSprites:
                            sprite.rect.y -= PLAYER_SPEED

    def animate(self):
        if  self.yChange == 0 and self.xChange == 0:
            self.image = self.game.viSpritesheet.getSprite(3, 0, VI_WIDTH, self.height, SCALE)
        else:
            self.image = self.downAnimations[math.floor(self.animationLoop)]
            self.animationLoop += 0.1
            if self.animationLoop >= 4:
                self.animationLoop = 0

class Npc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, image):
        self.game = game
        self._layer = NPC_LAYER
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.collidePlayer()

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            return True
        else:
            return False

class Brimstone(Npc):
    def __init__(self, game, x , y):
        self.image = game.brimSpritesheet.getSprite(5, 0, BRIM_WIDTH, BRIM_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (BRIM_HEIGHT - TILE_SIZE), BRIM_WIDTH, BRIM_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atBrim = True
        else:
            self.game.atBrim = False

class Fanfic(Npc):
    def __init__(self, game, x, y):
        self.image = game.fanficSpritesheet.getSprite(0, 0, FANFIC_WIDTH, FANFIC_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (FANFIC_HEIGHT - TILE_SIZE), FANFIC_WIDTH, FANFIC_HEIGHT, self.image)  

class F0(Fanfic):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def update(self):
        self.collidePlayer()
        if self.game.killF0:
            self.kill()    
            self.game.atF0 = False

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atF0 = True
        else:
            self.game.atF0 = False

class F1(Fanfic):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def update(self):
        self.collidePlayer()
        if self.game.killF1:
            self.kill()    
            self.game.atF1 = False

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atF1 = True
        else:
            self.game.atF1 = False   

class F2(Fanfic):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def update(self):
        self.collidePlayer()
        if self.game.killF2:
            self.kill()    
            self.game.atF2 = False

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atF2 = True
        else:
            self.game.atF2 = False   

class F3(Fanfic):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def update(self):
        self.collidePlayer()
        if self.game.killF3:
            self.kill()    
            self.game.atF3 = False

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atF3 = True
        else:
            self.game.atF3 = False                                       

class Cait(Npc):
    def __init__(self, game, x, y):
        self.image = game.caitSpritesheet.getSprite(3, 0, CAIT_WIDTH, CAIT_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (CAIT_HEIGHT - TILE_SIZE), CAIT_WIDTH, CAIT_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atCait = True
        else:
            self.game.atCait = False

class Anya(Npc):
    def __init__(self, game, x, y):
        self.image = game.anyaSpritesheet.getSprite(6, 0, ANYA_WIDTH, ANYA_HEIGHT, 1)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (ANYA_HEIGHT - TILE_SIZE), ANYA_WIDTH, ANYA_HEIGHT, self.image)
    
    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atAnya = True
        else:
            self.game.atAnya = False

class Charles(Npc):
    def __init__(self, game, x, y):
        # TODO: Change the numbers
        self.image = game.charlesSpritesheet.getSprite(5, 0, CHARLES_WIDTH, CHARLES_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (CHARLES_HEIGHT - TILE_SIZE), CHARLES_WIDTH, CHARLES_HEIGHT, self.image)
    
    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atCharles = True
        else:
            self.game.atCharles = False            

class Fenroar(Npc):
    def __init__(self, game, x, y):
        self.image = game.fenroarSpritesheet.getSprite(0, 1, FENROAR_WIDTH, FENROAR_HEIGHT, 1)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (FENROAR_HEIGHT - TILE_SIZE), FENROAR_WIDTH, FENROAR_HEIGHT, self.image)
    
    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atFenroar = True
        else:
            self.game.atFenroar = False       

class Dog(Npc):
    def __init__(self, game, x, y):
        self.image = game.dogSpritesheet.getSprite(0, 0, DOG_WIDTH, DOG_HEIGHT, 1)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (DOG_HEIGHT - TILE_SIZE), DOG_WIDTH, DOG_HEIGHT, self.image)

        self.animations = [game.dogSpritesheet.getSprite(0, 0, DOG_WIDTH, DOG_HEIGHT, 1),
                           game.dogSpritesheet.getSprite(32, 0, DOG_WIDTH, DOG_HEIGHT, 1),
                           game.dogSpritesheet.getSprite(64, 0, DOG_WIDTH, DOG_HEIGHT, 1),
                           game.dogSpritesheet.getSprite(96, 0, DOG_WIDTH, DOG_HEIGHT, 1)]

        self.animationLoop = 0
    
    def update(self):
        super().update()
        self.animate()

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atDog = True
        else:
            self.game.atDog = False 

    def animate(self):
        self.image = self.animations[math.floor(self.animationLoop)]
        self.animationLoop += 0.1
        if self.animationLoop >= 4:
            self.animationLoop = 0        

class Isak(Npc):
    def __init__(self, game, x, y):
        self.image = game.isakSpritesheet.getSprite(4, 0, ISAK_WIDTH, ISAK_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (ISAK_HEIGHT - TILE_SIZE), ISAK_WIDTH, ISAK_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atIsak = True
        else:
            self.game.atIsak = False

class Witch(Npc):
    def __init__(self, game, x, y):
        self.image = game.witchSpritesheet.getSprite(5, 0, WITCH_WIDTH, WITCH_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (WITCH_HEIGHT - TILE_SIZE), WITCH_WIDTH, WITCH_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atWitch = True
        else:
            self.game.atWitch = False

class Witch2(Npc):
    def __init__(self, game, x, y):
        self.image = game.witchSpritesheet.getSprite(5, 0, WITCH_WIDTH, WITCH_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (WITCH_HEIGHT - TILE_SIZE), WITCH_WIDTH, WITCH_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atWitch2 = True
        else:
            self.game.atWitch2 = False

class Ekko(Npc):
    def __init__(self, game, x, y, ):
        self.image = game.ekkoSpritesheet.getSprite(8, 0, EKKO_WIDTH, EKKO_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE - (EKKO_HEIGHT - TILE_SIZE), EKKO_WIDTH, EKKO_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atEkko = True
        else:
            self.game.atEkko = False

class Ezreal(Npc):
    def __init__(self, game, x, y):
        self.image = game.ezrealSpritesheet.getSprite(4, 0, EZREAL_WIDTH, EZREAL_HEIGHT, SCALE)
        super().__init__(game, x * TILE_SIZE, y * TILE_SIZE, EZREAL_WIDTH, EZREAL_HEIGHT, self.image)

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atEzreal = True
        else:
            self.game.atEzreal = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = NPC_LAYER
        self.groups = self.game.allSprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.xChange = 0
        self.yChange = 0

        self.facing = random.choice(['left', 'right', 'up', 'down'])
        self.animationLoop = 1
        self.movementLoop = 0
        self.maxTravel = random.randint(7, 30)

        self.image = self.game.enemySpritesheet.getSprite(3, 2, self.width, self.height, SCALE)

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.downAnimations = [self.game.enemySpritesheet.getSprite(5, 0, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(37, 0, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(69, 0, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(101, 0, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE)]

        self.upAnimations = [self.game.enemySpritesheet.getSprite(5, 32, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                         self.game.enemySpritesheet.getSprite(37, 32, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                         self.game.enemySpritesheet.getSprite(69, 32, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                         self.game.enemySpritesheet.getSprite(101, 32, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE)]

        self.rightAnimations = [self.game.enemySpritesheet.getSprite(37, 64, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(69, 64, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(101, 64, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                           self.game.enemySpritesheet.getSprite(5, 64, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE)]

        self.leftAnimations = [self.game.enemySpritesheet.getSprite(37, 96, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                            self.game.enemySpritesheet.getSprite(69, 96, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                            self.game.enemySpritesheet.getSprite(101, 96, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE),
                            self.game.enemySpritesheet.getSprite(5, 96, TEMPLATE_WIDTH, TEMPLATE_HEIGHT, SCALE)]

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.xChange
        self.rect.y += self.yChange

        self.xChange = 0
        self.yChange = 0

    def movement(self):
        if self.facing == 'left':
            self.xChange -= ENEMY_SPEED
            self.movementLoop -= 1
            if self.movementLoop <= -self.maxTravel:
                self.facing = 'right'
        if self.facing == 'right':
            self.xChange += ENEMY_SPEED
            self.movementLoop += 1
            if self.movementLoop >= self.maxTravel:
                self.facing = 'left'
        if self.facing == 'up':
            self.yChange -= ENEMY_SPEED
            self.movementLoop -= 1
            if self.movementLoop <= -self.maxTravel:
                self.facing = 'down'
        if self.facing == 'down':
            self.yChange += ENEMY_SPEED
            self.movementLoop += 1
            if self.movementLoop >= self.maxTravel:
                self.facing = 'up'

    def animate(self):

        if self.facing== 'down':
            if  self.yChange == 0:
                self.image = self.game.enemySpritesheet.getSprite(5, 0, TEMPLATE_WIDTH, self.height, SCALE)
            else:
                self.image = self.downAnimations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 4:
                    self.animationLoop = 0

        if self.facing== 'up':
            if  self.yChange == 0:
                self.image = self.game.enemySpritesheet.getSprite(5, 32, TEMPLATE_WIDTH, self.height, SCALE)
            else:
                self.image = self.upAnimations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 4:
                    self.animationLoop = 0

        if self.facing== 'right':
            if  self.xChange == 0:
                self.image = self.game.enemySpritesheet.getSprite(37, 64, TEMPLATE_WIDTH, self.height, SCALE)
            else:
                self.image = self.rightAnimations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 4:
                    self.animationLoop = 0
        
        if self.facing== 'left':
            if  self.xChange == 0:
                self.image = self.game.enemySpritesheet.getSprite(37, 96, TEMPLATE_WIDTH, self.height, SCALE)
            else:
                self.image = self.leftAnimations[math.floor(self.animationLoop)]
                self.animationLoop += 0.1
                if self.animationLoop >= 4:
                    self.animationLoop = 0

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.allSprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE


        # self.image = pygame.Surface([self.width, self.height])
        # self.image.fill(BLUE)
            
        if type == 'home':
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.image = self.game.terrainSpritesheet.getSprite(384, 576, self.width, self.height, 1)
        else:
            self.width = ROCK_WIDTH
            self.height = ROCK_HEIGHT
            self.image = self.game.terrainSpritesheet.getSprite(962, 450, ROCK_WIDTH, ROCK_HEIGHT, 1)

        # rect is the hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Breakable(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.allSprites, self.game.walls, self.game.breakables
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = ROCK_WIDTH
        self.height = ROCK_HEIGHT

        self.image = self.game.terrainSpritesheet.getSprite(962, 450, ROCK_WIDTH, ROCK_HEIGHT, 1)

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        if type == 'flower':
            self.image = self.game.terrainSpritesheet.getSprite(96, 352, self.width, self.height, 1)
        elif type == 'wood':
            self.image = self.game.terrainSpritesheet2.getSprite(258, 768, self.width, self.height, 1)
        elif type == 'chair':
            self.image = self.game.terrainSpritesheet2.getSprite(288, 448, self.width, self.height, 1)
        else:
            self.image = self.game.terrainSpritesheet.getSprite(64, 352, self.width, self.height, 1)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Flower(Ground):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.game.terrainSpritesheet.getSprite(96, 352, self.width, self.height, 1)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # def collidePlayer(self):
    #     hits = pygame.sprite.spritecollide(self, self.game.players, False)
    #     if hits:
    #         return True
    #     else:
    #         return False

    def update(self):
        self.collidePlayer()

    def collidePlayer(self):
        hits = pygame.sprite.spritecollide(self, self.game.players, False)
        if hits:
            self.game.atFlower = True
        else:
            self.game.atFlower = False

class Decor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.game = game
        self._layer = DECOR_LAYER
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE*2
        self.height = TILE_SIZE*2
    
        self.image = self.game.terrainSpritesheet2.getSprite(256, 672, self.width, self.height, 1)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    
    def __init__(self, x, y, width, height, fg, bg, content, size):
        self.font = pygame.font.Font('Arcane.ttf', size)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def isPressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

    def isHover(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

class Attack(pygame.sprite.Sprite):
    pygame.mixer.init()
    killedEnemyVoiceLines = [pygame.mixer.Sound('sounds/scaryterry.wav'),
                            pygame.mixer.Sound('sounds/Leo/Mald.wav'),
                            pygame.mixer.Sound('sounds/Alan/Mad.wav'),
                            pygame.mixer.Sound('sounds/Alan/IHaveAQuestion.wav'),
                            pygame.mixer.Sound('sounds/Willi/Tooki1.wav'),
                            pygame.mixer.Sound('sounds/Willi/Tooki2.wav')]

    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.allSprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups )
        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animationLoop = 0
        self.image = self.game.attackSpritesheet.getSprite(0, 0, self.width, self.height, 1)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.rightAnimations = [self.game.attackSpritesheet.getSprite(0, 64, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(32, 64, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(64, 64, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(96, 64, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(128, 64, self.width, self.height, SCALE)]

        self.downAnimations = [self.game.attackSpritesheet.getSprite(0, 32, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(32, 32, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(64, 32, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(96, 32, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(128, 32, self.width, self.height, SCALE)]

        self.leftAnimations = [self.game.attackSpritesheet.getSprite(0, 96, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(32, 96, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(64, 96, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(96, 96, self.width, self.height, SCALE),
                           self.game.attackSpritesheet.getSprite(128, 96, self.width, self.height, SCALE)]

        self.upAnimations = [self.game.attackSpritesheet.getSprite(0, 0, self.width, self.height, SCALE),
                         self.game.attackSpritesheet.getSprite(32, 0, self.width, self.height, SCALE),
                         self.game.attackSpritesheet.getSprite(64, 0, self.width, self.height, SCALE),
                         self.game.attackSpritesheet.getSprite(96, 0, self.width, self.height, SCALE),
                         self.game.attackSpritesheet.getSprite(128, 0, self.width, self.height, SCALE)]

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.breakables, True)
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        if hits:
            voiceLine = random.randint(0, len(self.killedEnemyVoiceLines)-1)
            self.killedEnemyVoiceLines[voiceLine].play()    
    
    def animate(self):
        direction = self.game.player.facing

        if direction == 'up':
            self.image = self.upAnimations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 5:
                self.kill()
        if direction == 'down':
            self.image = self.downAnimations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 5:
                self.kill()

        if direction == 'right':
            self.image = self.rightAnimations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 5:
                self.kill()
        
        if direction == 'left':
            self.image = self.leftAnimations[math.floor(self.animationLoop)]
            self.animationLoop += 0.5
            if self.animationLoop >= 5:
                self.kill()