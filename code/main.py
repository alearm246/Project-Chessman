import pygame
import sys
import time
from pygame.locals import *
from app import App

def start_game():
  pygame.init()
  pygame.key.set_repeat(1, 40)
  App()

if __name__ == "__main__":
  start_game()
