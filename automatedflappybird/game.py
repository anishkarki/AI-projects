import pygame as pg
import sys
from ga import GeneticAlgorithm
from random import randint
from pipe import Pipe
from bird import Bird
import time
import constants as cs



def detect_colision(pipes, bird):
    if bird.rect.colliderect(pipes.pipe_down) == 1 or bird.rect.colliderect(pipes.pipe_up) == 1:
        return True
    elif bird.rect.y < 0 or bird.rect.y > cs.HEIGHT:
        return True
    return False


def get_closest_pipe(piepes,x):

    for pipe in piepes:
        if pipe.pipe_down.x - x + cs.P_WIDTH > 0:
            return pipe

firstStart = True
gen = GeneticAlgorithm()


def play(daemon, firstStart=False, generation=1):

    counter = 0
    if firstStart:
        population = gen.population
    else:
        population = gen.crossover()

    fitness = 0
    deadcounter = 0

    pipes = [Pipe(randint(120,400))]

    if not daemon:
        screen = pg.display.set_mode(cs.SCREEN)
        clock = pg.time.Clock()
        pg.init()
        pg.font.init()
        font = pg.font.SysFont('Arial', 25)

    while True:

        if not daemon:

            clock.tick(60)
            screen.blit(pg.image.load('assets/background.png').convert(),(0,0))

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    gen.grade()
                    pg.quit()
                    sys.exit()

        fitness += 1


        for i,p in enumerate(pipes):# what is this for???
            if not daemon:
                p.draw(screen)
            p.update()

            if p.pipe_down.x < int((cs.WIDTH) / 3) and len(pipes) < 2:
                pipes.append(Pipe(randint(120, 400)))

            if p.pipe_down.x <= -cs.P_WIDTH-10:
                del pipes[i]
                counter += 1


        pipe = get_closest_pipe(pipes, population[0].rect.x)
        for player in population:
            if not player.dead:#if player not dead

                if detect_colision(pipe, player):
                    player.dead = True
                    player.fitness += 1000 * counter
                    deadcounter += 1
                if deadcounter >= len(population):
                    print(generation)
                    play(False,generation=generation+1)


                player.update(pipe)
                player.fitness += 1
                if not daemon:
                   #draw bird
                   player.draw(screen)

        if generation >= 500:
            gen.grade()
            break



        if not daemon:
            screen.blit(font.render('Birds left:{}'.format(str(len(population)-deadcounter)), -1, (255, 0, 0)), (200, 150))
            screen.blit(font.render('Progress:{}'.format(str(counter)), -1, (255, 255, 0)), (200, 50))
            screen.blit(font.render('Fitness:{}'.format(fitness), -1, (0, 0, 255)), (200, 250))
            screen.blit(font.render('Generation:{}'.format(generation), -1, (0, 0, 0)), (200, 350))
            pg.display.flip()

if __name__ == '__main__':
    play(False, firstStart=True)
