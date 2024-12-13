import pygame
class Order:
    def __init__(self,order_button_img):
        self.active = True
        self.drink_button=pygame.image.load(order_button_img).convert_alpha()
        order_button_img=order_button_img
        self.appetizer_button=pygame.image.load(order_button_img).convert_alpha()
        self.main_course_button=pygame.image.load(order_button_img).convert_alpha()
        self.first_side_button=pygame.image.load(order_button_img).convert_alpha()
        self.secound_side_button=pygame.image.load(order_button_img).convert_alpha()
        self.dessert_button=pygame.image.load(order_button_img).convert_alpha()

    def resize_img(self):
        self.drink_button = pygame.transform.scale(self.drink_button, (100, 34))
        self.appetizer_button = pygame.transform.scale(self.appetizer_button, (100, 34))
        self.main_course_button = pygame.transform.scale(self.main_course_button, (100, 34))
        self.first_side_button = pygame.transform.scale(self.first_side_button, (100, 34))
        self.secound_side_button = pygame.transform.scale(self.secound_side_button, (100, 34))
        self.dessert_button = pygame.transform.scale(self.dessert_button, (100, 34))

    def showing(self,screen):
        screen.blit(self.dessert_button, (75,50))
        screen.blit(self.main_course_button, (25,500))
        screen.blit(self.first_side_button, (3,1))
        screen.blit(self.drink_button, (100, 75))
        screen.blit(self.secound_side_button, (200,3))