import pygame, random, time

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400

FRAME_REFRESH_RATE = 30

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUND = (0, 0, 0)

MAX_NUMBER_OF_CYCLES = 1000
NEW_METEOR_CYCLE_INTERVAL = 40
INITIAL_METEOR_Y_LOCATION = 10
INITIAL_NUMBER_OF_METEORS = 8

# Initialize PyGame before loading images
pygame.init()
# Set up the display
DISPLAY_SURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Set up the STARSHIP
STARSHIP_SPEED = 10
STARSHIP_IMAGE = pygame.image.load('starship.png').convert()
STARSHIP_WIDTH = STARSHIP_IMAGE.get_width()
STARSHIP_HEIGHT = STARSHIP_IMAGE.get_height()
STARSHIP = {'x': DISPLAY_WIDTH / 2, 'y': DISPLAY_HEIGHT - 40}

# Set up METEOR constants
MAX_METEOR_SPEED = 5
METEOR_IMAGE = pygame.image.load('meteor.png').convert()
METEOR_WIDTH = METEOR_IMAGE.get_width()
METEOR_HEIGHT = METEOR_IMAGE.get_height()


def create_a_meteor():
    """ Creates a new meteor structure"""
    new_meteor = {'x': random.randint(0, DISPLAY_WIDTH),
                  'y': INITIAL_METEOR_Y_LOCATION,
                  'speed': random.randint(1, MAX_METEOR_SPEED)}
    return new_meteor


def move_meteor_down(meteor):
    """ Move a meteor down the screen """
    meteor['y'] = meteor['y'] + meteor['speed']
    if meteor['y'] > DISPLAY_HEIGHT:
        meteor['y'] = 5


def move_starship_right():
    """ moves the starship right across the screen """
    STARSHIP['x'] = STARSHIP['x'] + STARSHIP_SPEED
    if STARSHIP['x'] + STARSHIP_WIDTH > DISPLAY_WIDTH:
        STARSHIP['x'] = DISPLAY_WIDTH - STARSHIP_WIDTH


def move_starship_left():
    """ Move the starship left across the screen """
    STARSHIP['x'] = STARSHIP['x'] - STARSHIP_SPEED
    if STARSHIP['x'] < 0:
        STARSHIP['x'] = 0


def move_starship_up():
    """ Move the starship up the screen """
    STARSHIP['y'] = STARSHIP['y'] - STARSHIP_SPEED
    if STARSHIP['y'] < 0:
        STARSHIP['y'] = 0


def move_starship_down():
    """ Move the starship down the screen """
    STARSHIP['y'] = STARSHIP['y'] + STARSHIP_SPEED
    if STARSHIP['y'] + STARSHIP_HEIGHT > DISPLAY_HEIGHT:
        STARSHIP['y'] = DISPLAY_HEIGHT - STARSHIP_HEIGHT


def get_rect(obj, width, hieght):
    """ Return a rectangle representing the area on the screen
    the contains the game object """
    return pygame.Rect(obj['x'], obj['y'], width, hieght)


def get_meteor_rect(obj):
    """ return a rectangle representing a meteor on the screen
     in its current location """
    return get_rect(obj, METEOR_WIDTH, METEOR_HEIGHT)


def get_starship_rect(obj):
    """ Return a rectangle representin the starship on the screen """
    return get_rect(obj, STARSHIP_WIDTH, STARSHIP_HEIGHT)


def check_for_collision(meteors):
    """ Checks to see if any of the meteors have collided with the starship """
    result = False
    for meteor in meteors:
        if get_starship_rect(STARSHIP).colliderect(get_meteor_rect(meteor)):
            result = True
            break
    return result


def display_message(message):
    """ Displays a message to the user on the screen """
    text_font = pygame.font.Font('freesansbold.ttf', 48)
    text_surface = text_font.render(message, True, BLUE, WHITE)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    DISPLAY_SURFACE.fill(WHITE)
    DISPLAY_SURFACE.blit(text_surface, text_rectangle)


def main():
    """ Main processing loop of the game """
    print('Starting Game')
    # Set up the title fo the game
    pygame.display.set_caption('Starship Meteors')
    # Used for timing within the program
    clock = pygame.time.Clock()
    # Set up meteors
    meteors = [create_a_meteor() for _ in range(0, INITIAL_NUMBER_OF_METEORS)]

    is_running = True
    starship_collided = False
    cycle_count = 0

    # Main game playing Loop
    while is_running and not starship_collided:
        # Indicates how many times the main game loop has been run
        cycle_count += 1

        # See if the player has won
        if cycle_count == MAX_NUMBER_OF_CYCLES:
            display_message('WINNER!')
            break

        # Work out what the user wants to do
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                # Check to see which key is pressed
                if event.key == pygame.K_RIGHT:
                    # Right arrow key has been pressed
                    # move the player right
                    move_starship_right()
                elif event.key == pygame.K_LEFT:
                    # Left arrow has been pressed
                    # move the player left
                    move_starship_left()
                elif event.key == pygame.K_UP:
                    move_starship_up()
                elif event.key == pygame.K_DOWN:
                    move_starship_down()
                elif event.key == pygame.K_q:
                    is_running = False

        # Move the Meteors
        for meteor in meteors:
            move_meteor_down(meteor)

        # Clear the screen of current contents
        DISPLAY_SURFACE.fill(BACKGROUND)

        # Draw the meteors and the starship
        DISPLAY_SURFACE.blit(STARSHIP_IMAGE, (STARSHIP['x'], STARSHIP['y']))
        for meteor in meteors:
            DISPLAY_SURFACE.blit(METEOR_IMAGE, (meteor['x'], meteor['y']))

        # Check to see if a meteor has hit the ship
        if check_for_collision(meteors):
            starship_collided = True
            display_message('Collision: Game Over')

        # Determine if new mateors should be added
        if cycle_count % NEW_METEOR_CYCLE_INTERVAL == 0:
            meteors.append(create_a_meteor())

        # Update the display
        pygame.display.update()

        # Defines the frame rate. The number is number of frames per second
        # Should be called once per frame (but only once)
        clock.tick(FRAME_REFRESH_RATE)

    time.sleep(1)

    # Let pygame shutdown gracefully
    pygame.quit()

    print('Game Over')


if __name__ == '__main__':
    main()
