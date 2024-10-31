import pygame
import random

pygame.init()

# Set up the display
screen_width = 1200
screen_height = 800

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake")

# Define colors
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
food_color = (200, 50, 50)
blue = (0, 0, 255)
red = (255, 0, 0)

# Define game variables
cell_size = 10
direction = 1 # 1 is up, 2 is right, 3 is down, 4 is left
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]
score = 0
game_over = False
clicked = False

again_rect = pygame.Rect(screen_width/2 - 100, screen_height/2 - 50, 200, 100)

def draw_screen():
  screen.fill(bg)

def draw_score():
  score_txt = ('Score: ' + str(score))
  score_img = font.render(score_txt, True, blue)
  screen.blit(score_img, (10, 10))

def check_game_over(game_over):
  head_count = 0
  for segement in snake_pos:
    if snake_pos[0] == segement and head_count > 0:
      game_over = True
    head_count += 1

  if snake_pos[0][0] < 0 or snake_pos[0][0] > screen_width or snake_pos[0][1] < 0 or snake_pos[0][1] > screen_height:
    game_over = True
  
  return game_over

def draw_game_over():
  over_txt = ('Game Over')
  over_img = font.render(over_txt, True, blue)
  pygame.draw.rect(screen, red, (screen_width // 2-80, screen_height // 2 - 60, 160, 50))
  screen.blit(over_img, (screen_width // 2-80, screen_height // 2-50))
  
  again_txt = ('Play Again')
  again_img = font.render(again_txt, True, blue)
  pygame.draw.rect(screen, red, again_rect)
  screen.blit(again_img, (screen_width // 2-80, screen_height // 2 + 10))
  


# Create Snake
snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
snake_pos.append([int(screen_width / 2), int(screen_height / 2)  + cell_size * 3])

run = True
while run:
  # Draw snake
  for x in snake_pos:
    pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
    pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size -2, cell_size -2))

  draw_screen()
  draw_score()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        direction = 1
      if event.key == pygame.K_RIGHT:
        direction = 2
      if event.key == pygame.K_DOWN:
        direction = 3
      if event.key == pygame.K_LEFT:
        direction = 4

  if new_food == True:
    new_food = False
    food[0] = cell_size * random.randint(0, (screen_width / cell_size) - 1)
    food[1] = cell_size * random.randint(0, (screen_height / cell_size) - 1)

  #Draw food
  pygame.draw.rect(screen, food_color, (food[0], food[1], cell_size, cell_size))

  if game_over == False:
    # Move snake
    if update_snake > 99:
      update_snake = 0
      snake_pos = snake_pos[-1:] + snake_pos[:-1]
      if direction == 1:
        snake_pos[0][0] = snake_pos[1][0]
        snake_pos[0][1] = snake_pos[1][1] - cell_size
      if direction == 3:
        snake_pos[0][0] = snake_pos[1][0]
        snake_pos[0][1] = snake_pos[1][1] + cell_size
      if direction == 2:
        snake_pos[0][1] = snake_pos[1][1]
        snake_pos[0][0] = snake_pos[1][0] + cell_size
      if direction == 4:
        snake_pos[0][0] = snake_pos[1][0]
        snake_pos[0][0] = snake_pos[1][0] - cell_size
    game_over = check_game_over(game_over)  

    if game_over == True:
      draw_game_over()
      if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
      if event.type == pygame.MOUSEBUTTONUP and clicked == True:
        clicked = False
        pos = pygame.mouse.get_pos()
        if again_rect.collidepoint(pos):
          game_over = False
          snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]
          snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
          snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
          snake_pos.append([int(screen_width / 2), int(screen_height / 2)  + cell_size * 3])
          direction = 1
          update_snake = 0
          food = [0,0]
          new_food = True
          new_piece = [0,0]
          score = 0
    
  
  # Update the display
  pygame.display.update()

  update_snake += 1
pygame.quit()
