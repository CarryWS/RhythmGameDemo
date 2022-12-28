import pygame
import time
import configparser
import easygui
import sys


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Rhythm Game Demo')

try:
    mapfile = sys.argv[1]
except:
    mapfile = easygui.fileopenbox('Map file path:','Set map file path','*.ini')

conf = configparser.ConfigParser()
conf.read(mapfile)
Mainfps = float(conf.get('mainconfig','fps'))

block_sum = 0
while True:
    try:
        conf.get('note'+str(block_sum+1),'pos_x')
    except:
        break
    else:
        block_sum += 1

print(block_sum)

for block_num in range(1,block_sum+1):
    exec('block'+str(block_num)+'_position_x = int(conf.get(\'note'+str(block_num)+'\',\'pos_x\'))')
    exec('block'+str(block_num)+'_position_y = int(conf.get(\'note'+str(block_num)+'\',\'pos_y\'))')
    exec('print(\'block'+str(block_num)+'_position_x\',block'+str(block_num)+'_position_x)')
    exec('print(\'block'+str(block_num)+'_position_y\',block'+str(block_num)+'_position_y)')

    exec('block'+str(block_num)+'_size_x = int(conf.get(\'note'+str(block_num)+'\',\'size_x\'))')
    exec('block'+str(block_num)+'_size_y = int(conf.get(\'note'+str(block_num)+'\',\'size_y\'))')
    exec('print(\'block'+str(block_num)+'_size_x\',block'+str(block_num)+'_size_x)')
    exec('print(\'block'+str(block_num)+'_size_y\',block'+str(block_num)+'_size_y)')

    exec('block'+str(block_num)+' = pygame.Surface((block'+str(block_num)+'_size_x,block'+str(block_num)+'_size_y))')
    exec('block'+str(block_num)+'.fill(\'white\')')

#block1_position_x = int(conf.get('block1','position_x'))
#block1_position_y = int(conf.get('block1','position_y'))
#block1_size_x = int(conf.get('block1','size_x'))
#block1_size_y = int(conf.get('block1','size_y'))

#block2_position_x = int(conf.get('block2','position_x'))
#block2_position_y = int(conf.get('block2','position_y'))
#block2_size_x = int(conf.get('block2','size_x'))
#block2_size_y = int(conf.get('block2','size_y'))

#block1 = pygame.Surface((block1_size_x,block1_size_y))
#block2 = pygame.Surface((block2_size_x,block2_size_y))
#block1.fill('white')
#block2.fill('white')


line = pygame.Surface((1200,1))
line.fill('red')

perfect_sum = 0
good_sum = 0
bad_sum = 0
miss_sum =0

#block1_clicked = False

font = pygame.font.Font('C:\\Windows\\Fonts\\simhei.ttf',20)
perfect_text = font.render('Perfect: '+str(perfect_sum),True,'white','black')
good_text = font.render('Good: '+str(good_sum),True,'white','black')
bad_text = font.render('Bad: '+str(bad_sum),True,'white','black')
miss_text = font.render('Miss: '+str(miss_sum),True,'white','black')

clock = pygame.time.Clock()


bgm_file = conf.get('mainconfig','bgm')
pygame.mixer.music.load(bgm_file)
pygame.mixer.music.play()
while True:
    screen.fill('black')
    screen.blit(line,(0,700))

    for block_num in range(1,block_sum+1):
        exec('block'+str(block_num)+'_position_y += 1')
        exec('screen.blit(block'+str(block_num)+',(block'+str(block_num)+'_position_x,block'+str(block_num)+'_position_y))')

    '''
    block1_position_y += 1
    block1_distance = abs(block1_position_y+block1_size_y - 700)
    block1_distance_unabs = block1_position_y+block1_size_y - 700

    block2_position_y += 1
    block2_distance = abs(block2_position_y+block2_size_y - 700)
    block2_distance_unabs = block2_position_y+block2_size_y-700
    
    screen.blit(block1,(block1_position_x,block1_position_y))
    screen.blit(block2,(block2_position_x,block2_position_y))
    '''
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
            '''
        if events.type == pygame.MOUSEBUTTONDOWN and block1_clicked == False:
            block1_clicked = True
            mx , my = events.pos
            if mx >= block1_position_x and mx <= block1_position_x + block1_size_x:
                if my >= 650 and my <= 750:
                    print('distance: ',block1_distance)
                    if block1_distance <= 10:
                        perfect_sum += 1
                    if block1_distance >= 11 and block1_distance <= 20:
                        good_sum += 1
                    if block1_distance >= 21 and block1_distance <= 30:
                        bad_sum += 1
                    else:
                        miss_sum += 1
    if block1_distance_unabs >= 31 and block1_clicked == False:
        miss_sum += 1
        block1_clicked = True
    '''
    perfect_text = font.render('Perfect: '+str(perfect_sum),True,'white','black')
    good_text = font.render('Good: '+str(good_sum),True,'white','black')
    bad_text = font.render('Bad: '+str(bad_sum),True,'white','black')
    miss_text = font.render('Miss: '+str(miss_sum),True,'white','black')
    
    screen.blit(perfect_text,(0,0))
    screen.blit(good_text,(0,50))
    screen.blit(bad_text,(0,100))
    screen.blit(miss_text,(0,150))

    pygame.display.flip()
    clock.tick(Mainfps)
    #time.sleep(main_delay)
