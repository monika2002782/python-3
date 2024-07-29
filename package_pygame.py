# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
				random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object 
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)

# game over function
def game_over():

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text 
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text 
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()


# Main Function
while True:
	
	# handling key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	# If two keys pressed simultaneously
	# we don't want snake to move into two 
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10, 
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	# Game Over conditions
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()

	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score continuously
	show_score(1, white, 'times new roman', 20)

	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)










# SINGLE BALL RUNNING GAME
# import pygame
# import random

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# color=[0,0,0]
# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 500
# BALL_SIZE = 20

# # Define the starting color and the increment for each new ball
# START_COLOR = (0, 0, 0)


# class Ball:
#     """
#     Class to keep track of a ball's location, vector, and color.
#     """
#     def __init__(self,c):
#         self.x = 0
#         self.y = 0
#         self.change_x = 0
#         self.change_y = 0
#         self.color=c
        

            

# def make_ball(ball_list,c):
#     """
#     Function to make a new ball with a color.
#     """
#     # Calculate the color for the new ball based on the current number of balls
#     num_balls = len(ball_list)
#     """ color = tuple(min(255, START_COLOR[i] + num_balls * COLOR_INCREMENT[i]) for i in range(3))
#     print(color) """
#     ball = Ball(c)
#     # Starting position of the ball.
#     # Take into account the ball size so we don't spawn on the edge.
#     ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
#     ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

#     # Speed and direction of rectangle
#     ball.change_x = 5
#     ball.change_y = 5

#     return ball

# def main():
#     """
#     This is our main program.
#     """
#     pygame.init()

#     # Set the height and width of the screen
#     size = [SCREEN_WIDTH, SCREEN_HEIGHT]
#     screen = pygame.display.set_mode(size)

#     pygame.display.set_caption("Bouncing Balls")

#     # Loop until the user clicks the close button.
#     done = False

#     # Used to manage how fast the screen updates
#     clock = pygame.time.Clock()

#     ball_list = []

#     # Create the initial ball
#     ball = make_ball(ball_list,color)
#     ball_list.append(ball)

#     # -------- Main Program Loop -----------
#     while not done:
#         # --- Event Processing
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             elif event.type == pygame.KEYDOWN:
#                 if color[0]<245:
#                     color[0]+=10
#                 elif color[2]<245:
#                     color[2]+=10
#                 elif color[1]<245:
#                     color[1]+=10
#                 else:
#                     color[0]=0
#                     color[1]=0
#                     color[2]=0
#                 if event.key == pygame.K_SPACE:
#                     ball = make_ball(ball_list,color)
#                     ball_list.append(ball)

#         # --- Logic
#         for ball in ball_list:
#             # Move the ball's center
#             ball.x += ball.change_x
#             ball.y += ball.change_y

#             # Bounce the ball if needed
#             if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
#                 ball.change_y *= -1
#             if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
#                 ball.change_x *= -1

#         # --- Drawing
#         # Set the screen background
#         screen.fill(WHITE)

        



#         # Draw the balls with their respective colors
#         for ball in ball_list:
          
#             pygame.draw.circle(screen, color, [ball.x, ball.y], BALL_SIZE)

#         # --- Wrap-up
#         # Limit to 60 frames per second
#         clock.tick(200)

#         # Go ahead and update the screen with what we've drawn.
#         pygame.display.flip()

#     # Close everything down
#     pygame.quit()

# if __name__ == "__main__":
#     main()









# # MULTIPLE BALLS
# import pygame
# # initialize pygame
# pygame.init()

# # define width of screen
# width = 1000
# # define height of screen
# height = 600
# screen_res = (width, height)

# pygame.display.set_caption("GRS Bouncing game")
# screen = pygame.display.set_mode(screen_res)

# # define colors
# red = (255, 0, 0)
# green=(0,255,0)
# blue=(0,0,255)
# redgreen=(255,255,0)
# redblue=(255,0,255)
# black = (255,255,255)

# # define ball
# ball_obj = pygame.draw.circle(surface=screen, color=red, center=[100, 100], radius=20) 
# ball_obj1= pygame.draw.circle(surface=screen, color=blue, center=[100,100],radius=20)
# ball_obj2= pygame.draw.circle(surface=screen, color=green, center=[100,100],radius=20)
# ball_obj3= pygame.draw.circle(surface=screen, color=redgreen, center=[100,100],radius=20)
# ball_obj4= pygame.draw.circle(surface=screen, color=redblue, center=[100,100],radius=20)
# # define speed of ball
# # speed = [X direction speed, Y direction speed]
# speed = [1, 1] 
# speed1 = [2, 2]
# speed2= [3,3]
# speed3=[4,4]
# speed4=[5,5]

# # game loop
# while True:
# 	# event loop
# 	for event in pygame.event.get():
# 		# check if a user wants to exit the game or not
# 		if event.type == pygame.QUIT:
# 			exit()

# 	# fill black color on screen
# 	screen.fill(black)

# 	# move the ball
# 	# Let center of the ball is (100,100) and the speed is (1,1)
# 	ball_obj = ball_obj.move(speed) 
# 	ball_obj1=ball_obj1.move(speed1)
# 	ball_obj2=ball_obj2.move(speed2)
# 	ball_obj3=ball_obj3.move(speed3)
# 	ball_obj4=ball_obj4.move(speed4)
# 	# Now center of the ball is (101,101)
# 	# In this way our wall will move

# 	# if ball goes out of screen then change direction of movement
# 	if ball_obj.left <= 0 or ball_obj.right >= width:
# 		speed[0] = -speed[0]
# 	if ball_obj.top <= 0 or ball_obj.bottom >= height:
# 		speed[1] = -speed[1]
		
# 	if ball_obj1.left <= 0 or ball_obj1.right >= width:
# 		speed1[0] =- speed1[0]
# 	if ball_obj1.top <= 0 or ball_obj1.bottom >= height:
# 		speed1[1] =- speed1[1] 
		

# 	if ball_obj2.left <= 0 or ball_obj2.right >= width:
# 		speed2[0] =- speed2[0]
# 	if ball_obj2.top <= 0 or ball_obj2.bottom >= height:
# 		speed2[1] =- speed2[1] 
	
# 	if ball_obj3.left <= 0 or ball_obj3.right >= width:
# 		speed3[0] =- speed3[0]
# 	if ball_obj3.top <= 0 or ball_obj3.bottom >= height:
# 		speed3[1] =- speed3[1] 
		
# 	if ball_obj4.left <= 0 or ball_obj4.right >= width:
# 		speed4[0] =- speed4[0]
# 	if ball_obj4.top <= 0 or ball_obj4.bottom >= height:
# 		speed4[1] =- speed4[1] 
		
    


# 	# draw ball at new centers that are obtained after moving ball_obj
# 	pygame.draw.circle(surface=screen, color=red,center=ball_obj.center, radius=30)
# 	pygame.draw.circle(surface=screen,color=blue,center=ball_obj1.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=green,center=ball_obj2.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=redgreen,center=ball_obj3.center,radius=30)
# 	pygame.draw.circle(surface=screen,color=redblue,center=ball_obj4.center,radius=30)
	
	



# 	# update screen
# 	pygame.display.flip()


'''JUMPING BALL'''
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jumping Ball")

# Set up colors  
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the ball
ball_radius = 20
ball_x = window_width // 2
ball_y = window_height - ball_radius
ball_dy = 0
gravity = 0.5
jump_strength = -10
on_ground = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                ball_dy = jump_strength
                on_ground = False

    # Update ball position
    ball_y += ball_dy
    ball_dy += gravity

    # Check for collision with ground
    if ball_y >= window_height - ball_radius:
        ball_y = window_height - ball_radius
        ball_dy = 0
        on_ground = True

    # Fill the window with white color
    window.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(window, BLUE, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()  
