import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('foster_the_people.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Agora vc escuta?')


