import pygame

# Initialize Pygame
pygame.init()

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 40
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)

# Create the Pygame window
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption('Eraser Tool')

# Function to draw grid
def draw_grid():
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            pygame.draw.rect(screen, BLUE, pygame.Rect(col, row, CELL_SIZE, CELL_SIZE))

# Function to erase objects in contact with the eraser
def erase_objects(eraser_rect):
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            cell_rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
            if cell_rect.colliderect(eraser_rect):  # Check if the cell and eraser overlap
                pygame.draw.rect(screen, WHITE, cell_rect)

def main():
    # Set up clock for smooth movement
    clock = pygame.time.Clock()
    
    # Create an initial grid
    screen.fill(WHITE)
    draw_grid()
    
    eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
    dragging = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse clicks on the eraser
                if eraser_rect.collidepoint(event.pos):
                    dragging = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
        
        # Get mouse position and move the eraser
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if dragging:
            # Adjust the position of the eraser to center it on the mouse cursor
            eraser_rect.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)
        
        # Erase the cells in contact with the eraser
        erase_objects(eraser_rect)
        
        # Draw the eraser
        pygame.draw.rect(screen, PINK, eraser_rect)
        
        pygame.display.update()
        clock.tick(30)  # 30 FPS for smooth movement

if __name__ == '__main__':
    main()
