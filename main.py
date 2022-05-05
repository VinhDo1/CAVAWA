import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(TITLE_TEXT)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arcane.ttf', 48)
        self.running = True
        self.camera = True
        self.finished = False

        self.malding = False

        self.killF0 = False
        self.killF1 = False
        self.killF2 = False
        self.killF3 = False

        self.atBrim = False
        self.atF0 = False
        self.atF1 = False
        self.atF2 = False
        self.atF3 = False
        self.atWitch = False
        self.atWitch2 = False
        self.atCait = False
        self.atAnya = False
        self.atCharles = False
        self.atFenroar = False
        self.atDog = False
        self.atIsak = False
        self.atEkko = False
        self.atEzreal = False
        self.atFlower = False

        self.viSpritesheet = Spritesheet('img/viTemplate.png')
        self.brimSpritesheet = Spritesheet('img/brim.png')
        self.fanficSpritesheet = Spritesheet('img/fanfic.png')
        self.witchSpritesheet = Spritesheet('img/witch.png')
        self.caitSpritesheet = Spritesheet('img/cait.png')
        self.anyaSpritesheet = Spritesheet('img/anya.png')
        self.charlesSpritesheet = Spritesheet('img/charles.png')
        self.fenroarSpritesheet = Spritesheet('img/fenroar.png')
        self.dogSpritesheet = Spritesheet('img/dog.png')
        self.isakSpritesheet = Spritesheet('img/isak.png')
        self.ekkoSpritesheet = Spritesheet('img/ekko.png')
        self.ezrealSpritesheet = Spritesheet('img/ezreal.png')

        self.enemySpritesheet = Spritesheet('img/template.png')
        self.attackSpritesheet = Spritesheet('img/attack.png')
        self.terrainSpritesheet = Spritesheet('img/terrain.png')
        self.terrainSpritesheet1 = Spritesheet('img/tiles1.png')
        self.terrainSpritesheet2 = Spritesheet('img/tiles2.png')
        self.introBackground = pygame.image.load('img/intro.png')
        self.goBackground = pygame.image.load('img/smallbadending.jpg')
        self.ceremonyBackground = pygame.image.load('img/ceremony2.png')
        self.creditsBackground = pygame.image.load('img/credits.png')

        self.channel = pygame.mixer.Channel(0)
        self.channel1 = pygame.mixer.Channel(1)

        self.goSound = pygame.mixer.Sound('sounds/PaperMarioGO.wav') 
        self.ceremonySound = pygame.mixer.Sound('sounds/Ceremony.wav')   

        self.brimVoiceLines = [pygame.mixer.Sound('sounds/Doovid/ArentYouLate.wav'),
                            pygame.mixer.Sound('sounds/Doovid/WhatDoesFarmerMean.wav'),
                            pygame.mixer.Sound('sounds/Doovid/AwMan.wav'),
                            pygame.mixer.Sound('sounds/Doovid/Toasted.wav'),
                            pygame.mixer.Sound('sounds/Doovid/Optional.wav')]
        self.fanficVoiceLines = [pygame.mixer.Sound('sounds/Dchen/Fanfic0.wav'),
                            pygame.mixer.Sound('sounds/Willi/Fanfic1.wav'),
                            pygame.mixer.Sound('sounds/Shenward/Fanfic2.wav'),
                            pygame.mixer.Sound('sounds/Richard/Fanfic3.wav'),]
        self.witchVoiceLines = [pygame.mixer.Sound('sounds/Andrew/GetPast.wav'),
                            pygame.mixer.Sound('sounds/Andrew/YeaHateFarmers.wav'),
                            pygame.mixer.Sound('sounds/Andrew/IfYoureBad.wav'),
                            pygame.mixer.Sound('sounds/Andrew/ImWarningYou.wav'),
                            pygame.mixer.Sound('sounds/Andrew/TryUsingSpacebar.wav')]
        self.witch2VoiceLines = [pygame.mixer.Sound('sounds/Andrew/DangIfOnly.wav')]
        self.caitVoiceLines = [pygame.mixer.Sound('sounds/Upi/YoureSoLate.wav'),
                            pygame.mixer.Sound('sounds/Upi/IJustLickedLux.wav'),
                            pygame.mixer.Sound('sounds/Upi/OkBoomer.wav'),
                            pygame.mixer.Sound('sounds/Upi/DoYouWanna.wav'),
                            pygame.mixer.Sound('sounds/Upi/YoureHotCupcake.wav')]                                                                                                                                                                        
        self.anyaVoiceLines = [pygame.mixer.Sound('sounds/Sherry/Greeting.wav'),
                            pygame.mixer.Sound('sounds/Sherry/MomLovesKnives.wav'),
                            pygame.mixer.Sound('sounds/Sherry/SpySpySpy.wav')]     
        self.charlesVoiceLines = [pygame.mixer.Sound('sounds/Nikolaj/DannyShenwardWilli.wav'),
                            pygame.mixer.Sound('sounds/Nikolaj/DoovidVinh.wav'),
                            pygame.mixer.Sound('sounds/Nikolaj/LeoUpi.wav')]  
        self.fenroarVoiceLines = [pygame.mixer.Sound('sounds/Pew/AlanAndrewDanny.wav'),
                            pygame.mixer.Sound('sounds/Pew/DchenDoovidLeo.wav'),
                            pygame.mixer.Sound('sounds/Pew/RichardShenwardSherry.wav'),
                            pygame.mixer.Sound('sounds/Pew/UpiWilliVinh.wav')]            
        self.dogVoiceLines = [pygame.mixer.Sound('sounds/Dog/LeoUpi.wav'),
                            pygame.mixer.Sound('sounds/Dog/ShenwardVinh.wav'),
                            pygame.mixer.Sound('sounds/Dog/DchenDoovidDanny.wav')]                
        self.isakVoiceLines = [pygame.mixer.Sound('sounds/Vinh/Greeting.wav'),
                            pygame.mixer.Sound('sounds/Vinh/GodTongue.wav'),
                            pygame.mixer.Sound('sounds/Vinh/YouLovePizza.wav'),
                            pygame.mixer.Sound('sounds/Vinh/EzrealBrokeUp.wav'),
                            pygame.mixer.Sound('sounds/Vinh/SuddenlyHot.wav')]
        self.ekkoVoiceLines = [pygame.mixer.Sound('sounds/Danny/HiVi.wav'),
                            pygame.mixer.Sound('sounds/Danny/ThankYouVi.wav'),
                            pygame.mixer.Sound('sounds/Danny/ICantBelieve.wav'),
                            pygame.mixer.Sound('sounds/Danny/PressF5.wav')]
        self.ezrealVoiceLines = [pygame.mixer.Sound('sounds/Leo/Greeting.wav'),
                            pygame.mixer.Sound('sounds/Leo/WideSnakes.wav'),
                            pygame.mixer.Sound('sounds/Leo/PressF5.wav')]


        self.brimVoiceCount = 0
        self.fanficVoiceCount = 0
        self.witchVoiceCount = 0
        self.witch2VoiceCount = 0
        self.previousEnemyLine = 0
        self.caitVoiceCount = 0
        self.anyaVoiceCount = 0
        self.previousChar = 0
        self.previousFenroar = 0
        self.previousDog = 0
        self.isakVoiceCount = 0
        self.ekkoVoiceCount = 0
        self.ezrealVoiceCount = 0

        self.music = pygame.mixer.music.load('sounds/GiraffeBackgroundMusic.wav')
        pygame.mixer.music.set_volume(0.3)

    def createTilemap(self, map):
        for y, row in enumerate(map):
            for x, col in enumerate(row):
                if col == "f":
                    Flower(self, x, y)
                elif col == "w":
                    Ground(self, x, y, 'wood')
                elif col == "c":
                    Ground(self, x, y, 'chair')

                    
                elif col == "W":
                    Wall(self, x, y, 'rock')
                elif col == "H":
                    Wall(self, x, y, 'home')
                elif col == "r":
                    Breakable(self, x, y)
                elif col == "P":
                    self.player = Player(self, x, y)
                elif col == "B":
                    Brimstone(self, x, y)
                elif col == "0":
                    F0(self, x, y)
                elif col == "1":
                    F1(self, x, y)
                elif col == "2":
                    F2(self, x, y)
                elif col == "3":
                    F3(self, x, y)
                elif col == "K":
                    Witch(self, x, y)
                elif col == "Y":
                    Witch2(self, x, y)
                elif col == "C":
                    Cait(self, x, y)
                elif col == "A":
                    Anya(self, x, y)
                elif col == "L":
                    Charles(self, x, y)    
                elif col == "F":
                    Fenroar(self, x, y)
                elif col == "D":
                    Dog(self, x, y)
                elif col == "I":
                    Isak(self, x, y)
                elif col == "E":
                    Enemy(self, x, y)
                elif col == "O":
                    Ekko(self, x, y)                    
                elif col == "Z":
                    Ezreal(self, x, y)
                else:
                    Ground(self, x, y, 'grass')

    def new(self):
        # a new game starts
        self.playing = True

        self.allSprites = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.breakables = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.players = pygame.sprite.LayeredUpdates()

        self.createTilemap(tilemap)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.malding = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILE_SIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILE_SIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILE_SIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILE_SIZE, self.player.rect.y)

                if event.key == pygame.K_c:
                    self.camera = not self.camera
                if event.key == pygame.K_g:
                    if self.atBrim:
                        self.channel.play(self.brimVoiceLines[self.brimVoiceCount])
                        self.atBrim = False
                        self.brimVoiceCount += 1
                        if self.brimVoiceCount > len(self.brimVoiceLines) - 1:
                            self.brimVoiceCount = 0 
                    elif self.atF0:
                        self.channel.play(self.fanficVoiceLines[self.fanficVoiceCount])
                        self.killF0 = True    
                        self.atF0 = False
                        self.fanficVoiceCount += 1
                        if self.fanficVoiceCount > len(self.fanficVoiceLines) - 1:
                            self.fanficVoiceCount = 0     
                    elif self.atF1:
                        self.channel.play(self.fanficVoiceLines[self.fanficVoiceCount])
                        self.killF1 = True    
                        self.atF1 = False
                        self.fanficVoiceCount += 1
                        if self.fanficVoiceCount > len(self.fanficVoiceLines) - 1:
                            self.fanficVoiceCount = 0  
                    elif self.atF2:
                        self.channel.play(self.fanficVoiceLines[self.fanficVoiceCount])
                        self.killF2 = True    
                        self.atF2 = False
                        self.fanficVoiceCount += 1
                        if self.fanficVoiceCount > len(self.fanficVoiceLines) - 1:
                            self.fanficVoiceCount = 0  
                    elif self.atF3:
                        self.channel.play(self.fanficVoiceLines[self.fanficVoiceCount])
                        self.killF3 = True    
                        self.atF3 = False
                        self.fanficVoiceCount += 1
                        if self.fanficVoiceCount > len(self.fanficVoiceLines) - 1:
                            self.fanficVoiceCount = 0                                
                    elif self.atWitch:
                        self.channel.play(self.witchVoiceLines[self.witchVoiceCount])
                        self.atWitch = False
                        self.witchVoiceCount += 1
                        if self.witchVoiceCount > len(self.witchVoiceLines) - 1:
                            self.witchVoiceCount = 0
                    elif self.atWitch2:
                        self.channel.play(self.witch2VoiceLines[self.witch2VoiceCount])
                        self.atWitch2 = False
                        self.witch2VoiceCount += 1
                        if self.witch2VoiceCount > len(self.witch2VoiceLines) - 1:
                            self.witch2VoiceCount = 0                    
                    elif self.atCait:
                        self.channel.play(self.caitVoiceLines[self.caitVoiceCount])
                        self.atCait = False
                        self.caitVoiceCount += 1
                        if self.caitVoiceCount > len(self.caitVoiceLines) - 1:
                            self.caitVoiceCount = 0  
                    elif self.atAnya:
                        self.channel.play(self.anyaVoiceLines[self.anyaVoiceCount])
                        self.atAnya = False
                        self.anyaVoiceCount += 1
                        if self.anyaVoiceCount > len(self.anyaVoiceLines) - 1:
                            self.anyaVoiceCount = 0  
                    elif self.atCharles:
                        randVoiceLine = random.randint(0, len(self.charlesVoiceLines)-1)
                        while randVoiceLine == self.previousChar:
                            randVoiceLine = random.randint(0, len(self.charlesVoiceLines)-1)
                        self.channel.play(self.charlesVoiceLines[randVoiceLine])
                        self.previousChar = randVoiceLine
                        self.atCharles = False
                    elif self.atFenroar:
                        randVoiceLine = random.randint(0, len(self.fenroarVoiceLines)-1)
                        while randVoiceLine == self.previousFenroar:
                            randVoiceLine = random.randint(0, len(self.fenroarVoiceLines)-1)
                        self.channel.play(self.fenroarVoiceLines[randVoiceLine])
                        self.previousFenroar = randVoiceLine  
                        self.atFenroar = False
                    elif self.atDog:
                        randVoiceLine = random.randint(0, len(self.dogVoiceLines)-1)
                        while randVoiceLine == self.previousDog:
                            randVoiceLine = random.randint(0, len(self.dogVoiceLines)-1)
                        self.channel.play(self.dogVoiceLines[randVoiceLine])
                        self.previousDog = randVoiceLine
                        self.atDog = False
                    elif self.atIsak:
                        self.channel.play(self.isakVoiceLines[self.isakVoiceCount])
                        self.atIsak = False
                        self.isakVoiceCount += 1
                        if self.isakVoiceCount > len(self.isakVoiceLines) - 1:
                            self.isakVoiceCount = 0 
                    elif self.atEkko:                        
                        self.channel.play(self.ekkoVoiceLines[self.ekkoVoiceCount])
                        self.atEkko = False
                        self.ekkoVoiceCount += 1
                        if self.ekkoVoiceCount > len(self.ekkoVoiceLines) - 1:
                            self.ekkoVoiceCount = 0 
                    elif self.atEzreal:
                        self.channel.play(self.ezrealVoiceLines[self.ezrealVoiceCount])
                        self.atEzreal = False
                        self.ezrealVoiceCount += 1
                        if self.ezrealVoiceCount > len(self.ezrealVoiceLines) - 1:
                            self.ezrealVoiceCount = 0 
                if self.atFlower and event.key == pygame.K_F5:
                    self.channel.play(self.ceremonySound)
                    self.finished = True
                    self.playing = False
                    self.atFlower = False                

    def update(self):
        # game loop updates
        self.allSprites.update()
        
    def draw(self):
        self.screen.fill(GREEN)
        self.allSprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()            

    def introScreen(self):
        pygame.mixer.music.play(-1)
        intro = True

        counter = 0

        title = self.font.render(TITLE_TEXT, True, TITLE_COLOR)
        titleRect = title.get_rect(x=10, y=0)

        playButton = Button(900, 70, 120, 50, WHITE, GIRAFFE_GREEN, 'Play', 48)
        exitButton = Button(900, 135, 120, 50, WHITE, GIRAFFE_GREEN, 'Exit', 48)

        morleButton = Button(880, 400, 150, 120, WHITE, GIRAFFE_GREEN, 'CAVAWA', 48)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()

            if playButton.isPressed(mousePos, mousePressed) or keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or counter > 45:
                # If counter is over 45 then play a special voice line
                intro = False
            elif playButton.isHover(mousePos):
                playButton = Button(900, 70, 120, 50, WHITE, GIRAFFE_GREEN_DARK, 'Play', 48)
            else:
                playButton = Button(900, 70, 120, 50, WHITE, GIRAFFE_GREEN, 'Play', 48)

            if exitButton.isPressed(mousePos, mousePressed):
                intro = False
                self.running = False
            elif exitButton.isHover(mousePos):
                exitButton = Button(900, 135, 120, 50, WHITE, GIRAFFE_GREEN_DARK, 'Exit', 48)
            else:
                exitButton = Button(900, 135, 120, 50, WHITE, GIRAFFE_GREEN, 'Exit', 48)

            if morleButton.isHover(mousePos):
                counter += 1
                randX = random.randint(60, 1160)
                randY = random.randint(60, 600)
                morleButton = Button(randX, randY, 120, 100, WHITE, GIRAFFE_GREEN, 'Morle', 42)
                

            self.screen.blit(self.introBackground, (0,0))
            self.screen.blit(title, titleRect)
            self.screen.blit(playButton.image, playButton.rect)
            self.screen.blit(exitButton.image, exitButton.rect)
            self.screen.blit(morleButton.image, morleButton.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def gameOver(self):
        pygame.mixer.music.stop()
        self.goSound.play()
        text = self.font.render('You Died', True, WHITE)
        textRect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restartButton = Button(WIN_WIDTH/2 - 60, WIN_HEIGHT / 2 + 30, 120, 50, WHITE, GIRAFFE_GREEN, 'Restart', 32)

        for sprite in self.allSprites:
            sprite.kill()

        while self.malding:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.malding = False
                    self.running = False
            
            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            # keys = pygame.key.get_pressed()

            if restartButton.isPressed(mousePos, mousePressed):
                pygame.mixer.music.play()
                self.new()
                self.malding = False
                # self.main()
            elif restartButton.isHover(mousePos):
                restartButton = Button(WIN_WIDTH/2 - 60, WIN_HEIGHT / 2 + 30, 120, 50, WHITE, GIRAFFE_GREEN_DARK, 'Restart', 32)
            else:
                restartButton = Button(WIN_WIDTH/2 - 60, WIN_HEIGHT / 2 + 30, 120, 50, WHITE, GIRAFFE_GREEN, 'Restart', 32)
            
            self.screen.blit(self.goBackground, (0,0))
            self.screen.blit(text, textRect)
            self.screen.blit(restartButton.image, restartButton.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def ceremony(self):
        pygame.mixer.music.stop()
        ceremony = True
        button = False

        timerEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(timerEvent, 62000)
        # pygame.time.set_timer(timerEvent, 1)

        continueButton = Button(WIN_WIDTH/2 - 70, WIN_HEIGHT / 2 - 60, 140, 50, WHITE, GIRAFFE_GREEN, 'Continue', 32)

        while ceremony and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                elif event.type == timerEvent:
                    button = True

                mousePos = pygame.mouse.get_pos()
                mousePressed = pygame.mouse.get_pressed()
                keys = pygame.key.get_pressed()

                if button:
                    if continueButton.isPressed(mousePos, mousePressed):
                        ceremony = False
                    elif continueButton.isHover(mousePos):
                        continueButton = Button(WIN_WIDTH/2 - 70, WIN_HEIGHT / 2 - 60, 140, 50, WHITE, GIRAFFE_GREEN_DARK, 'Continue', 32)
                    else:
                        continueButton = Button(WIN_WIDTH/2 - 70, WIN_HEIGHT / 2 - 60, 140, 50, WHITE, GIRAFFE_GREEN, 'Continue', 32)                  
            
            self.screen.blit(self.ceremonyBackground, (0,0))
            if button:
                self.screen.blit(continueButton.image, continueButton.rect)
            self.clock.tick(FPS)
            pygame.display.update()

            if not ceremony:
                self.credits()

    def credits(self):
        text = self.font.render('You did it!', True, WHITE)
        textRect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/(4*3)))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False

            mousePos = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            
            self.screen.blit(self.creditsBackground, (0,0))
            self.screen.blit(text, textRect)
            self.clock.tick(FPS)
            pygame.display.update()        

g = Game()
g.introScreen()
g.new()
while g.running:
    g.main()
    if g.finished:
        g.ceremony()
    else:
        g.gameOver()

pygame.quit()
sys.exit()