
import pygame

from Button import Button
from game import *
from setting import *


# class Button:
#     def __init__(self, screen, x, y, width, height, color, border_color, border_width, text):
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color
#         self.border_color = border_color
#         self.border_width = border_width
#         self.text = text

#     def draw(self):
#         # vẽ viền cho nút
#         pygame.draw.rect(self.screen, self.border_color, (self.x,
#                          self.y, self.width, self.height), self.border_width)
#         # vẽ nút
#         pygame.draw.rect(self.screen, self.color, (self.x + self.border_width, self.y +
#                          self.border_width, self.width - self.border_width * 2, self.height - self.border_width * 2))
#         # canh chỉnh chữ trong nút
#         font = pygame.font.SysFont(None, 30)
#         text_surface = font.render(self.text, True, (0, 0, 0))
#         text_rect = text_surface.get_rect(
#             center=(self.x + self.width // 2, self.y + self.height // 2))
#         self.screen.blit(text_surface, text_rect)






class mainGUI:
    def __init__(self):
        pygame.init()
        self.icon = pygame.image.load(r'img\logo.png')
        self.background = pygame.image.load(r'img\background.png')
        self.background = pygame.transform.scale(
            self.background, (WIDTH, HEIGHT))
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.addControls()
        self.run()

    def addControls(self):
        x = 160
        self.zombie_Button = Button(self.screen, (self.screen.get_width(
        ) - 200) // 2, (self.screen.get_height() - 50) // 2 + x - 70, 200, 50, SILVER, BLACK, 3, "ZOMBIE WORLD")
        self.training_Button = Button(self.screen, (self.screen.get_width(
        ) - 200) // 2, (self.screen.get_height() - 50) // 2 + x, 200, 50, SILVER, BLACK, 3, "TRAINING")
        self.pvp_Button = Button(self.screen, (self.screen.get_width(
        ) - 200) // 2, (self.screen.get_height() - 50) // 2 + x + 70, 200, 50, SILVER, BLACK, 3, "2 PLAYERS")
        self.button_quit = Button(self.screen, (self.screen.get_width(
        ) - 200) // 2, (self.screen.get_height() - 50) // 2 + x + 140, 200, 50, SILVER, BLACK, 3, "QUIT")
    
    def quit(self):
        pygame.quit()
        quit()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.zombie_Button.draw()
        self.training_Button.draw()
        self.pvp_Button.draw()
        self.button_quit.draw()

    def addEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            # so sánh tọa độ x y của nút với của con trỏ chuột
                if check_btn_click(mouse_pos, self.button_quit):
                    self.quit()  # Thoát chương trình
                if check_btn_click(mouse_pos, self.zombie_Button):
                    self.current_display = mode_zombie(self.screen)
                if check_btn_click(mouse_pos, self.training_Button):
                    self.current_display = mode_training(self.screen)
                if check_btn_click(mouse_pos, self.pvp_Button):
                    self.current_display = mode_1v1(self.screen)
                self.screen.blit(self.background, (0, 0))
                    

    def run(self):
        self.run = True
        while self.run:
            self.addEvents()
            self.draw()
            pygame.display.flip()
        self.quit()
