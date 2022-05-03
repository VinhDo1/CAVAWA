WIN_WIDTH = 1280
WIN_HEIGHT = 736
TILE_SIZE = 32
VI_SIZE = 53
FPS = 60
SCALE = 1

ROCK_WIDTH = 28
ROCK_HEIGHT = 29

TEMPLATE_WIDTH = 22
TEMPLATE_HEIGHT = 31

VI_WIDTH = 24
BRIM_WIDTH = 24
BRIM_HEIGHT = 31
FANFIC_WIDTH = 22
FANFIC_HEIGHT = 15
WITCH_WIDTH = 34
WITCH_HEIGHT = 43
CAIT_WIDTH = 24
CAIT_HEIGHT = 36
ANYA_WIDTH = 22
ANYA_HEIGHT = 31
CHARLES_WIDTH = 22
CHARLES_HEIGHT = 31
FENROAR_WIDTH = 32
FENROAR_HEIGHT = 29
DOG_WIDTH = 32
DOG_HEIGHT = 31
ISAK_WIDTH = 24
ISAK_HEIGHT = 31
EKKO_WIDTH = 22
EKKO_HEIGHT = 38
EZREAL_WIDTH = 24
EZREAL_HEIGHT = 31

PLAYER_SPEED = 10
ENEMY_SPEED = 2

PLAYER_LAYER = 5
NPC_LAYER = 4
DECOR_LAYER = 3
WALL_LAYER = 2
GROUND_LAYER = 1


RED = (255, 0, 0)
GREEN = (47, 129, 56)
BLUE = (0, 0, 255)
TITLE_COLOR = (167, 129, 92)
GIRAFFE_GREEN = (223, 247, 187)
GIRAFFE_GREEN_DARK = (190, 212, 159)
GRAY = (40, 40, 40)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TITLE_TEXT = 'Cait and Vi\'s Wedding Adventure'

# Each tile is 32 pixels so you make it however big you want
tilemap = [
        'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
        'W.......................................W',
        'W.......................................W',
        'W.......................................W',
        'W.......................................W',
        'W.......................................WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
        'W.......................................W0............W..................E............E.....WW...............W',
        'W............HHHHHHHHHHHH...............W.............W............E........................WW..E............W',
        'W............HwwwwwwwwwwH...............W......E....WWW....E...........W.........E..........WW........W......W',
        'W............HwwwwwwwwwwH...........................W................E.W.................E..WW........W......W',
        'W............HwwwwwPwwwwH............K..............W.......E..........W.........W....E..........E....W......W',
        'W............HwwwwwwwwwwH......................................W.......W.........W...........E........WE.....W',
        'W............HwwwwwwwwwwH...........................E..........E................WW.................E..W..E...W',
        'W............HwwwwwwwwwwH.......................W......................E.........W....E......E........W......W',
        'W............HHHHH..HHHHH..............................WWWW.....WW......E........W....WWW..........WWWW......W',
        'W................B......................................E......W.................W....WWW.E........W.........W',
        'W...............................................E..............W............E....W1...WWW..........W.........W',
        'W.......................................WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW...E.....W',
        'W.......................................W++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.rr.rrr..W',
        'W.......................................W++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r...r...W',
        'W.......................................W++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.....r...W',
        'W.......................................W++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.....r.rrW',
        'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW..WWWWWWWW++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Wrrrr.r...W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.....r...W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.....rrr.W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++....rrrrr.W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++..........W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.........W',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r.r.rrrrW',
        '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r.r.....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++WWWWWW.r.rrrrr.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...rr.r.r.....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Wrr....r.r.rrrrW',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...rrrr.r.....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r....r.rrrrr.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r..r.r.r...r.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r.rr.r.r.r...W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r.r..r.r.rrrrW',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Wrrrr.rr.r.....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W......rrrrrrr.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r.rr.r....2r.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r....r.rrrrr.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.rr.rrr.r...r.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Wrr......r.r.r.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...rrrr.r.r.r.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.rr...r.r.r...W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.r..r...r.rrrrW',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.rrrr.rrr.....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W......r.rrrrr.W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++WWWrrrrrrr.......WWWWWWWW',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W................C......W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...............A.......W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....................Y..W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc..rrW',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.....................r3W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc..rrW',       
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...........L...........W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.........F...D.........W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++........................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',                
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...I...................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W....ccccc.....ccccc....W',                
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W...........f...........W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W..........O.Z..........W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++W.......................W',
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++WWWWWWWWWWWWWWWWWWWWWWWWW',

]