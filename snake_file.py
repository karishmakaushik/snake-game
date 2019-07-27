import pygame, sys, random

#initialization or set of pygame
pygame.init()

#colors
black=(0, 0, 0)
white=(255, 255, 255) 
red=(200,0,0)
Green = (0,199,0)
Blue = (0,0,255)
BG = (255,255,200)

#set up of screen
width=900
height=600
screen=pygame.display.set_mode((width,height),pygame.RESIZABLE )

#set up background image
background_img = pygame.image.load("snake.png")
background_img = pygame.transform.scale(background_img, (width,height)).convert_alpha()

#variables
fps=10

#Game name
pygame.display.set_caption('Snake Game')

#Game icon
icon_var= pygame.image.load('icon.png')
pygame.display.set_icon(icon_var)
pygame.mixer.music.load('snake_music.mp3')

#time
clock = pygame.time.Clock()

#set up front display
front_img=pygame.image.load('front.png')
front_img=pygame.transform.scale(front_img,(int(width/2),int(height/2)))
pygame.display.flip()

def plot_snake(screen, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])
    pygame.display.update()



def display_text(text,size,color,x,y):
    text1=pygame.font.SysFont(None,size)
    text2=text1.render(text,True,color)
    text3= text2.get_rect()
    text3.center= (x,y)
    screen.blit(text2,text3)
    pygame.display.update()

def frontend():
    while True:
        display_text("Welcome to Snake Game!!!Press Space To Play....",40, black, 400, 250)
        screen.fill(Green)
        screen.blit(front_img, (900,600))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.play()
                    game_loop()

    click=pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(fps)

def game_loop():
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(10, width / 2)
    food_y = random.randint(10, height / 2)
    score = 0
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            screen.fill(Green)
            display_text("Your score is:  "+str(score)+".  Game Over!  Press Enter To Continue...",40,red, 500, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        frontend()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - 5
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 5
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 5
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <30 and abs(snake_y - food_y) <30:
                score += 10
                food_x = random.randint(20, width / 2)
                food_y = random.randint(20, height / 2)
                snk_length += 5

            screen.fill(Green)
            screen.blit(background_img, (0, 0))
            display_text("Score: " + str(score), 30,red, 40, 15)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                #pygame.mixer.music.load('gameover.mp3')
                #pygame.mixer.music.play()

            if snake_x < 0 or snake_x > 890 or snake_y < 0 or snake_y > 590:
                game_over = True
                #pygame.mixer.music.load('gameover.mp3')
                #pygame.mixer.music.play()
            plot_snake(screen, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
frontend()
