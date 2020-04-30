import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("snake game")

black = (0,0,0)
blue = (0,0,255)
snake_block = 10
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
snake_list = []
length_of_snake = 1
foodx = round(random.randrange(0,800-10)/10)*10
foody = round(random.randrange(0,800-10)/10)*10

clock = pygame.time.Clock()

def our_snake(snake_block,snake_list):
	for x in snake_list:
		pygame.draw.rect(x[0],x[1],10,10)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x1_change = -10
				y1_change = 0
				
			if event.key == pygame.K_RIGHT:
				x1_change = 10
				y1_change = 0
			if event.key == pygame.K_UP:
				y1_change = -10
				x1_change = 0
			if event.key == pygame.K_DOWN:
				y1_change = 10
				x1_change = 0 

	if x1>=800 or x1<0 or y1>=800 or y1<0:
		running  = False
	x1 += x1_change
	y1 += y1_change
	screen.fill((255,255,255))
	pygame.draw.rect(screen,black,[x1,y1,10,10])
	pygame.draw.rect(screen,blue,[foodx,foody,10,10])
	snake_head = []
	snake_head.append(x1)
	snake_head.append(y1)
	snake_list.append(snake_head)
	if len(snake_list) > length_of_snake:
		del snake_list[0]

	our_snake(10,[])
	pygame.display.update()
	if x1 == foodx and y1 == foody:
		foodx = round(random.randrange(0,800-10)/10)*10
		foody = round(random.randrange(0,800-10)/10)*10
		length_of_snake +=1
	clock.tick(30)

pygame.quit()
quit()



