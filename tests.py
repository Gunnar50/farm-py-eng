import sys

import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('In-Game Console Debugger')
font = pygame.font.Font(None, 32)

# Variables to monitor
game_variables = {
    'player_health': 100,
    'player_position': (50, 100),
    'enemy_count': 5,
}

# Input-related variables
input_active = False
input_text = ''
console_output = []


def evaluate_input(user_input, variables):
  try:
    # If the input is a variable name, return its value
    if user_input in variables:
      return f"{user_input} = {variables[user_input]}"
    # Otherwise, attempt to evaluate it as a Python expression
    else:
      result = eval(user_input, {}, variables)
      return str(result)
  except Exception as e:
    return f"Error: {str(e)}"


def draw_console():
  screen.fill((0, 0, 0))  # Clear screen with black color

  # Draw previous console output
  y_offset = 0
  for line in console_output[-10:]:  # Display last 10 lines of output
    text_surface = font.render(line, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10 + y_offset))
    y_offset += 30

  # Draw input text
  input_surface = font.render('> ' + input_text, True, (0, 255, 0))
  screen.blit(input_surface, (10, 570))

  pygame.display.flip()


# Main loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_BACKQUOTE:  # Toggle console with backquote key (`)
        input_active = not input_active
        input_text = ''

      elif input_active:
        if event.key == pygame.K_RETURN:
          # Evaluate input and append the result to the console output
          result = evaluate_input(input_text.strip(), game_variables)
          console_output.append(f"> {input_text}")
          console_output.append(result)
          input_text = ''

        elif event.key == pygame.K_BACKSPACE:
          # Remove last character from input text
          input_text = input_text[:-1]

        else:
          # Append typed character to input text
          input_text += event.unicode

  if input_active:
    draw_console()
  else:
    screen.fill((0, 0, 0))  # Clear screen when console is not active
    pygame.display.flip()

  pygame.time.Clock().tick(60)
