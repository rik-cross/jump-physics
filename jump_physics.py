# define screen size
WIDTH = 800
HEIGHT = 800
# define some colours
MAROON = 128,0,0
# vertical acceleration
GRAVITY = 0.2
# vertical velocity
JUMPSPEED = -7

# a list of platforms, each is a rectangle
# in the form ((x,y)(w,h))
platforms = [
    Rect((0,780),(800,20)),
    Rect((200,700),(100,100)),
    Rect((400,650),(100,20)),
    Rect((600,600),(100,20))
]

# create a player with initial speed
player = Actor('player',(50,450), anchor=('left','top'))
player.x_velocity = 2
player.y_velocity = 0
# player width and height
player.w = 20
player.h = 20

def update():

    #
    # horizontal movement
    #

    # calculate new horizontal position if
    # arrow keys are pressed
    if keyboard.left and player.x > 0:
        player.x -= player.x_velocity
    if keyboard.right and player.x < 780:
        player.x += player.x_velocity

    #
    # vertical movement
    #

    # temporary variable to store new y position
    newy = player.y

    # gravity is rate of change of velocity
    player.y_velocity += GRAVITY
    # velocity is rate of change of position
    newy += player.y_velocity

    # create a rectangle for the new y position
    newplayerpositiony = Rect((player.x,newy),(player.w,player.h))

    # check whether the new player position
    # collides with any playform
    collisiony = False
    # also check whether the player is on the ground
    playeronground = False
    # distance from colliding platform (used if on ground)
    ydist = 0
    for p in platforms:
        collisiony = newplayerpositiony.colliderect(p) or collisiony

    # player no longer has vertical velocity
    # if colliding with a platform
    if collisiony:
        player.y_velocity = 0
    # only allow the player to move if it
    # doesn't collide with any platforms
    else:
        player.y = newy

    # pressing space sets a negative vertical velocity
    # only if player is on the ground
    if keyboard.space and collisiony:
        player.y_velocity = JUMPSPEED

def draw():

    screen.clear()

    # draw platforms
    for p in platforms:
        screen.draw.filled_rect(p,MAROON)

    # draw player
    player.draw()
