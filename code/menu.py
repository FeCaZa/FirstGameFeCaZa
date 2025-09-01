#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import *


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            # Desenhando as imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'StarDate', COLOR_MENU, ((WIN_WIDTH / 2), 60))
            self.menu_text(50, '-4821184-', COLOR_MENU, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], COLOR_MENU_SELECT, ((WIN_WIDTH / 2), 300 + 40 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], COLOR_MENU_OP, ((WIN_WIDTH / 2), 300 + 40 * i))

            pygame.display.flip()

            # Checagem de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar janela
                    quit()  # Encerrar pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # Tecla Baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # Tecla Cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Tecla Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
