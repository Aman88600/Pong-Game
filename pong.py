import time
from msilib.schema import Font
from re import S
import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen=pygame.display.set_mode((600,400))
gameDisplay=pygame.display.set_mode((600,400))
white=(255,255,255)
left_pong_y=200
right_pong_y=200
left_pong_up=0
left_pong_down=0
right_pong_up=0
right_pong_down=0
# ball
ball_x=300.0
ball_y=200.0
vx=0
vy=0
xbl=10
xbr=590
ybu=0
ybd=400
speed =1
scorel=0
scorer=0
running=True
while running:

	# RGB - Red, Green, Blue
	screen.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				left_pong_y-=10
			if event.key == pygame.K_s:
				left_pong_y+=10
			if event.key == pygame.K_UP:
				right_pong_y-=10
			if event.key == pygame.K_DOWN:
				right_pong_y+=10
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				left_pong_up=0
			if event.key == pygame.K_s:
				left_pong_down=0
			if event.key == pygame.K_UP:
				right_pong_up=0
			if event.key == pygame.K_DOWN:
				right_pong_down=0

	# pongs move up or down continiously
	if left_pong_up == 1:
		left_pong_y-=1#speed
	if left_pong_down == 1:
		left_pong_y+=1
	if right_pong_up == 1:
		right_pong_y-=1#speed
	if right_pong_down == 1:
		right_pong_y+=1
	

	right_pong_y=ball_y-30
	# left_pong_y=ball_y-30
	# ball moving logic
	
	if vx == 0 and vy == 0:#1
		if ball_x+10<xbr and ball_y>ybu:
			ball_x+=speed
			ball_y-=speed
			if(ball_x+10==xbr) and (ball_y==right_pong_y or ball_y==right_pong_y+1 or ball_y==right_pong_y+2 or ball_y==right_pong_y+3 or ball_y==right_pong_y+4 or ball_y==right_pong_y+5 or ball_y==right_pong_y+6 or ball_y==right_pong_y+7 or ball_y==right_pong_y+8 or ball_y==right_pong_y+9 or ball_y==right_pong_y+10 or ball_y==right_pong_y+11 or ball_y==right_pong_y+12 or ball_y==right_pong_y+13 or ball_y==right_pong_y+14 or ball_y==right_pong_y+15 or ball_y==right_pong_y+16 or ball_y==right_pong_y+17 or ball_y==right_pong_y+18 or ball_y==right_pong_y+19 or ball_y==right_pong_y+20 or ball_y==right_pong_y+21 or ball_y==right_pong_y+22 or ball_y==right_pong_y+23 or ball_y==right_pong_y+24 or ball_y==right_pong_y+25 or ball_y==right_pong_y+26 or ball_y==right_pong_y+27 or ball_y==right_pong_y+28 or ball_y==right_pong_y+29 or ball_y==right_pong_y+30 or ball_y==right_pong_y+31 or ball_y==right_pong_y+32 or ball_y==right_pong_y+33 or ball_y==right_pong_y+34 or ball_y==right_pong_y+35 or ball_y==right_pong_y+36 or ball_y==right_pong_y+37 or ball_y==right_pong_y+38 or ball_y==right_pong_y+39 or ball_y==right_pong_y+40 or ball_y==right_pong_y+41 or ball_y==right_pong_y+42 or ball_y==right_pong_y+43 or ball_y==right_pong_y+44 or ball_y==right_pong_y+45 or ball_y==right_pong_y+46 or ball_y==right_pong_y+47 or ball_y==right_pong_y+48 or ball_y==right_pong_y+49 or ball_y==right_pong_y+50 or ball_y==right_pong_y+51 or ball_y==right_pong_y+52 or ball_y==right_pong_y+53 or ball_y==right_pong_y+54 or ball_y==right_pong_y+55 or ball_y==right_pong_y+56 or ball_y==right_pong_y+57 or ball_y==right_pong_y+58 or ball_y==right_pong_y+59 or ball_y==right_pong_y+60 or ball_y==right_pong_y+61 or ball_y==right_pong_y+62 or ball_y==right_pong_y+63 or ball_y==right_pong_y+64 or ball_y==right_pong_y+65 or ball_y==right_pong_y+66 or ball_y==right_pong_y+67 or ball_y==right_pong_y+68 or ball_y==right_pong_y+69 or ball_y==right_pong_y+70 or ball_y==right_pong_y+71 or ball_y==right_pong_y+72 or ball_y==right_pong_y+73 or ball_y==right_pong_y+74 or ball_y==right_pong_y+75 or ball_y==right_pong_y+76 or ball_y==right_pong_y+77 or ball_y==right_pong_y+78 or ball_y==right_pong_y+79 or ball_y==right_pong_y+80 or ball_y==right_pong_y+81 or ball_y==right_pong_y+82 or ball_y==right_pong_y+83 or ball_y==right_pong_y+84 or ball_y==right_pong_y+85 or ball_y==right_pong_y+86 or ball_y==right_pong_y+87 or ball_y==right_pong_y+88 or ball_y==right_pong_y+89 or ball_y==right_pong_y+90):
				vx=1
				# ball_x=300
				# ball_y=200
				speed=1
			elif(ball_x+10==xbr) and (ball_y!=right_pong_y):
				ball_x=300
				ball_y=200
				scorel=scorel+1;
			if(ball_x+10==xbr) and (ball_y!=right_pong_y or ball_y!=right_pong_y+10):
				vx=1
				
			if ball_y==ybu:
				vy=1
	if vx == 1 and vy == 1:#2
		if ball_x>xbl and ball_y+10<ybd:
			ball_x-=speed
			ball_y+=speed
			if(ball_x==xbl) and (ball_y==left_pong_y or ball_y==left_pong_y+1 or ball_y==left_pong_y+2 or ball_y==left_pong_y+3 or ball_y==left_pong_y+4 or ball_y==left_pong_y+5 or ball_y==left_pong_y+6 or ball_y==left_pong_y+7 or ball_y==left_pong_y+8 or ball_y==left_pong_y+9 or ball_y==left_pong_y+10 or ball_y==left_pong_y+11 or ball_y==left_pong_y+12 or ball_y==left_pong_y+13 or ball_y==left_pong_y+14 or ball_y==left_pong_y+15 or ball_y==left_pong_y+16 or ball_y==left_pong_y+17 or ball_y==left_pong_y+18 or ball_y==left_pong_y+19 or ball_y==left_pong_y+20 or ball_y==left_pong_y+21 or ball_y==left_pong_y+22 or ball_y==left_pong_y+23 or ball_y==left_pong_y+24 or ball_y==left_pong_y+25 or ball_y==left_pong_y+26 or ball_y==left_pong_y+27 or ball_y==left_pong_y+28 or ball_y==left_pong_y+29 or ball_y==left_pong_y+30 or ball_y==left_pong_y+31 or ball_y==left_pong_y+32 or ball_y==left_pong_y+33 or ball_y==left_pong_y+34 or ball_y==left_pong_y+35 or ball_y==left_pong_y+36 or ball_y==left_pong_y+37 or ball_y==left_pong_y+38 or ball_y==left_pong_y+39 or ball_y==left_pong_y+40 or ball_y==left_pong_y+41 or ball_y==left_pong_y+42 or ball_y==left_pong_y+43 or ball_y==left_pong_y+44 or ball_y==left_pong_y+45 or ball_y==left_pong_y+46 or ball_y==left_pong_y+47 or ball_y==left_pong_y+48 or ball_y==left_pong_y+49 or ball_y==left_pong_y+50 or ball_y==left_pong_y+51 or ball_y==left_pong_y+52 or ball_y==left_pong_y+53 or ball_y==left_pong_y+54 or ball_y==left_pong_y+55 or ball_y==left_pong_y+56 or ball_y==left_pong_y+57 or ball_y==left_pong_y+58 or ball_y==left_pong_y+59 or ball_y==left_pong_y+60 or ball_y==left_pong_y+61 or ball_y==left_pong_y+62 or ball_y==left_pong_y+63 or ball_y==left_pong_y+64 or ball_y==left_pong_y+65 or ball_y==left_pong_y+66 or ball_y==left_pong_y+67 or ball_y==left_pong_y+68 or ball_y==left_pong_y+69 or ball_y==left_pong_y+70 or ball_y==left_pong_y+71 or ball_y==left_pong_y+72 or ball_y==left_pong_y+73 or ball_y==left_pong_y+74 or ball_y==left_pong_y+75 or ball_y==left_pong_y+76 or ball_y==left_pong_y+77 or ball_y==left_pong_y+78 or ball_y==left_pong_y+79 or ball_y==left_pong_y+80 or ball_y==left_pong_y+81 or ball_y==left_pong_y+82 or ball_y==left_pong_y+83 or ball_y==left_pong_y+84 or ball_y==left_pong_y+85 or ball_y==left_pong_y+86 or ball_y==left_pong_y+87 or ball_y==left_pong_y+88 or ball_y==left_pong_y+89 or ball_y==left_pong_y+90):
				vx=0
				speed=1
			elif(ball_x==xbl) and (ball_y!=left_pong_y):
				ball_x=300
				ball_y=200
				scorer+=1;
				
			
			# if(ball_x==xbl) and (ball_y!=left_pong_y or ball_y!=left_pong_y+10):
			# 	vx=0

			if ball_y+10==ybd:
				vy=0
	if vx == 0 and vy == 1:#3
		if ball_x+10<xbr and ball_y+10<ybd:
			ball_x+=speed
			ball_y+=speed
			if(ball_x+10==xbr) and (ball_y==right_pong_y or ball_y==right_pong_y+1 or ball_y==right_pong_y+2 or ball_y==right_pong_y+3 or ball_y==right_pong_y+4 or ball_y==right_pong_y+5 or ball_y==right_pong_y+6 or ball_y==right_pong_y+7 or ball_y==right_pong_y+8 or ball_y==right_pong_y+9 or ball_y==right_pong_y+10 or ball_y==right_pong_y+11 or ball_y==right_pong_y+12 or ball_y==right_pong_y+13 or ball_y==right_pong_y+14 or ball_y==right_pong_y+15 or ball_y==right_pong_y+16 or ball_y==right_pong_y+17 or ball_y==right_pong_y+18 or ball_y==right_pong_y+19 or ball_y==right_pong_y+20 or ball_y==right_pong_y+21 or ball_y==right_pong_y+22 or ball_y==right_pong_y+23 or ball_y==right_pong_y+24 or ball_y==right_pong_y+25 or ball_y==right_pong_y+26 or ball_y==right_pong_y+27 or ball_y==right_pong_y+28 or ball_y==right_pong_y+29 or ball_y==right_pong_y+30 or ball_y==right_pong_y+31 or ball_y==right_pong_y+32 or ball_y==right_pong_y+33 or ball_y==right_pong_y+34 or ball_y==right_pong_y+35 or ball_y==right_pong_y+36 or ball_y==right_pong_y+37 or ball_y==right_pong_y+38 or ball_y==right_pong_y+39 or ball_y==right_pong_y+40 or ball_y==right_pong_y+41 or ball_y==right_pong_y+42 or ball_y==right_pong_y+43 or ball_y==right_pong_y+44 or ball_y==right_pong_y+45 or ball_y==right_pong_y+46 or ball_y==right_pong_y+47 or ball_y==right_pong_y+48 or ball_y==right_pong_y+49 or ball_y==right_pong_y+50 or ball_y==right_pong_y+51 or ball_y==right_pong_y+52 or ball_y==right_pong_y+53 or ball_y==right_pong_y+54 or ball_y==right_pong_y+55 or ball_y==right_pong_y+56 or ball_y==right_pong_y+57 or ball_y==right_pong_y+58 or ball_y==right_pong_y+59 or ball_y==right_pong_y+60 or ball_y==right_pong_y+61 or ball_y==right_pong_y+62 or ball_y==right_pong_y+63 or ball_y==right_pong_y+64 or ball_y==right_pong_y+65 or ball_y==right_pong_y+66 or ball_y==right_pong_y+67 or ball_y==right_pong_y+68 or ball_y==right_pong_y+69 or ball_y==right_pong_y+70 or ball_y==right_pong_y+71 or ball_y==right_pong_y+72 or ball_y==right_pong_y+73 or ball_y==right_pong_y+74 or ball_y==right_pong_y+75 or ball_y==right_pong_y+76 or ball_y==right_pong_y+77 or ball_y==right_pong_y+78 or ball_y==right_pong_y+79 or ball_y==right_pong_y+80 or ball_y==right_pong_y+81 or ball_y==right_pong_y+82 or ball_y==right_pong_y+83 or ball_y==right_pong_y+84 or ball_y==right_pong_y+85 or ball_y==right_pong_y+86 or ball_y==right_pong_y+87 or ball_y==right_pong_y+88 or ball_y==right_pong_y+89 or ball_y==right_pong_y+90):
				vx=1
				# ball_x=300
				# ball_y=200
				speed=1
			elif(ball_x+10==xbr) and (ball_y!=right_pong_y):
				ball_x=300
				ball_y=200
				scorel+=1
			if(ball_x+10==xbr) and (ball_y!=right_pong_y or ball_y!=right_pong_y+10):
				vx=1

			if ball_y+10==ybd:
				vy=0
	if vx == 1 and vy == 0:#4 1 is -ve 0 is +ve
		if ball_x>xbl and ball_y>ybu:
			ball_x-=speed
			ball_y-=speed
			if(ball_x==xbl) and (ball_y==left_pong_y or ball_y==left_pong_y+1 or ball_y==left_pong_y+2 or ball_y==left_pong_y+3 or ball_y==left_pong_y+4 or ball_y==left_pong_y+5 or ball_y==left_pong_y+6 or ball_y==left_pong_y+7 or ball_y==left_pong_y+8 or ball_y==left_pong_y+9 or ball_y==left_pong_y+10 or ball_y==left_pong_y+11 or ball_y==left_pong_y+12 or ball_y==left_pong_y+13 or ball_y==left_pong_y+14 or ball_y==left_pong_y+15 or ball_y==left_pong_y+16 or ball_y==left_pong_y+17 or ball_y==left_pong_y+18 or ball_y==left_pong_y+19 or ball_y==left_pong_y+20 or ball_y==left_pong_y+21 or ball_y==left_pong_y+22 or ball_y==left_pong_y+23 or ball_y==left_pong_y+24 or ball_y==left_pong_y+25 or ball_y==left_pong_y+26 or ball_y==left_pong_y+27 or ball_y==left_pong_y+28 or ball_y==left_pong_y+29 or ball_y==left_pong_y+30 or ball_y==left_pong_y+31 or ball_y==left_pong_y+32 or ball_y==left_pong_y+33 or ball_y==left_pong_y+34 or ball_y==left_pong_y+35 or ball_y==left_pong_y+36 or ball_y==left_pong_y+37 or ball_y==left_pong_y+38 or ball_y==left_pong_y+39 or ball_y==left_pong_y+40 or ball_y==left_pong_y+41 or ball_y==left_pong_y+42 or ball_y==left_pong_y+43 or ball_y==left_pong_y+44 or ball_y==left_pong_y+45 or ball_y==left_pong_y+46 or ball_y==left_pong_y+47 or ball_y==left_pong_y+48 or ball_y==left_pong_y+49 or ball_y==left_pong_y+50 or ball_y==left_pong_y+51 or ball_y==left_pong_y+52 or ball_y==left_pong_y+53 or ball_y==left_pong_y+54 or ball_y==left_pong_y+55 or ball_y==left_pong_y+56 or ball_y==left_pong_y+57 or ball_y==left_pong_y+58 or ball_y==left_pong_y+59 or ball_y==left_pong_y+60 or ball_y==left_pong_y+61 or ball_y==left_pong_y+62 or ball_y==left_pong_y+63 or ball_y==left_pong_y+64 or ball_y==left_pong_y+65 or ball_y==left_pong_y+66 or ball_y==left_pong_y+67 or ball_y==left_pong_y+68 or ball_y==left_pong_y+69 or ball_y==left_pong_y+70 or ball_y==left_pong_y+71 or ball_y==left_pong_y+72 or ball_y==left_pong_y+73 or ball_y==left_pong_y+74 or ball_y==left_pong_y+75 or ball_y==left_pong_y+76 or ball_y==left_pong_y+77 or ball_y==left_pong_y+78 or ball_y==left_pong_y+79 or ball_y==left_pong_y+80 or ball_y==left_pong_y+81 or ball_y==left_pong_y+82 or ball_y==left_pong_y+83 or ball_y==left_pong_y+84 or ball_y==left_pong_y+85 or ball_y==left_pong_y+86 or ball_y==left_pong_y+87 or ball_y==left_pong_y+88 or ball_y==left_pong_y+89 or ball_y==left_pong_y+90):
				vx=0
				# ball_x=300
				# ball_y=200
				speed=1
			elif(ball_x==xbl) and (ball_y!=left_pong_y):
				ball_x=300
				ball_y=200
				scorer+=1
				
			if(ball_x==xbl) and (ball_y!=left_pong_y or ball_y!=left_pong_y+10):
				# ball_x=300
				# ball_y=200
				vx=0
				
			if ball_y==ybu:
				vy=1
	
	print("score_Left=",scorel,"score_Right",scorer)
	
	


	pygame.draw.rect(gameDisplay,white,(0,left_pong_y,10,100))# x,y of top left and width and height
	
	pygame.draw.rect(gameDisplay,white,(590,right_pong_y,10,100))# x,y of top left and width and height
	
	pygame.draw.rect(gameDisplay,white,(ball_x,ball_y,10,10))# x,y of top left and width and height
	time.sleep(0.008)
	pygame.display.update()