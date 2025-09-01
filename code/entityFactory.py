#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.player import Player
from code.enemy import Enemy


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_Bg = []
                for i in range(9):
                    list_Bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_Bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_Bg
            case 'Player1':
                return Player('Player1', (10, (WIN_HEIGHT/2) - 60))
            case 'Player2':
                return Player('Player2', (10, (WIN_HEIGHT / 2) + 60))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(15, WIN_HEIGHT - 15)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(15, WIN_HEIGHT - 15)))
