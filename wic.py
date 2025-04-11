import pygame
pygame.init()

# global constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# if you want your game to go full-screen, use this:
# dim = pygame.display.Info()
# SCREEN_WIDTH = dim.current_w
# SCREEN_HEIGHT = dim.current_h
 
CELL_SIZE = 60
WIDTH = SCREEN_WIDTH // CELL_SIZE
HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# color constants -- RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (192, 192, 192)

'''
these are my special colors i color picked online.
for ease, i suggest just using standard red and green
'''
PINK = (255, 179, 230)
GREEN = (195, 250, 167)

# Create Maze function
def initMaze():
    # You can randomly add obstacles here using a for-loop
    # but for our purposes (and ease) using a set array is preferred
    maze = [
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
    ]
    # 0 = empty space
    # 1 = wall
    # 2 = goal/exit

    return maze

# Draw maze
def drawMaze(screen, maze):
    # traverse maze array
    for col in range(WIDTH):
        for row in range(HEIGHT):
            if maze[col][row] == 1:     # visualize the 1s as walls
                # syntax: surface, color, (left coordinate, top coordinate, width, height)
                pygame.draw.rect(screen, BLACK, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif maze[col][row] == 2:   # visualize the endpoint as a distinct color (red)
                pygame.draw.rect(screen, GREEN, (row * CELL_SIZE, col * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Create the player
class Player:
    def __init__(self):     # initialize player at 0, 0
        self.x = 0
        self.y = 0
    
    # move player
    def move(self, dx, dy, maze): 
        newX = self.x + dx
        newY = self.y + dy

        # check that new coords are valid
        if 0 <= newX < WIDTH and 0 <= newY < HEIGHT and maze[newY][newX] != 1:
            self.x = newX
            self.y = newY
    
    # draw player
    def draw(self, screen):
        pygame.draw.rect(screen, PINK, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main
def main():
    # set screen, text, and display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nidhi's Maze <3")      # title displayed on window! make this whatever you want
    screen.fill(WHITE)

    # create maze and player
    maze = initMaze()
    player = Player()
    drawMaze(screen, maze)
    player.draw(screen)

    # bool to track if the player has won
    run = True

    while run:
        # get events from arrow keys
        for event in pygame.event.get():        # event = input (keyboard, mouse, etc.)
            if event.type == pygame.QUIT:       # quit if user exits window
                run = False
            # otherwise, check for a key input using the arrow keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(0, -1, maze)
                elif event.key == pygame.K_DOWN:
                    player.move(0, 1, maze)
                elif event.key == pygame.K_LEFT:
                    player.move(-1, 0, maze)
                elif event.key == pygame.K_RIGHT:
                    player.move(1, 0, maze)
        
        # refill the background + redraw maze/player every iteration
        screen.fill(WHITE)      # if you don't do this, your "player" will just keep duplicating
        drawMaze(screen, maze)
        player.draw(screen)

        # if player wins, end game
        if maze[player.y][player.x] == 2:
            run = False
        pygame.display.flip()       # update contents of the entire display

    # change screen color after win
    screen.fill(GREEN)

    # winning text display -- show off some funky text options
    font = pygame.font.SysFont("Lucida Console", 48)        # Try "Lucida Console"
    text = font.render('You won!', True, BLACK)
    text_center = (
        (SCREEN_WIDTH // 2 - text.get_width() // 2), 
        (SCREEN_HEIGHT // 2 - text.get_height() // 2)
    )

    screen.blit(text, text_center)
    pygame.display.flip()
    pygame.time.wait(2000)      # lag, then close
    pygame.quit()       # close window

if __name__ == "__main__":      # call main
    main()