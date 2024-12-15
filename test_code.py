import pygame
import sys

# initializing the constructor
pygame.init()


# screen resolution
res = (1500, 1000)

# opens up a window
screen = pygame.display.set_mode(res)
thai_ice_tea=pygame.image.load('thaitea.jpg').convert_alpha()
thai_ice_tea = pygame.transform.scale(thai_ice_tea, (150, 200))
soda_img=pygame.image.load('soda.jpeg').convert_alpha()
soda_img = pygame.transform.scale(soda_img, (150, 200))
water_img=pygame.image.load('watter.jpg').convert_alpha()
water_img = pygame.transform.scale(water_img, (150, 200))
shrimp_img = pygame.image.load('Tempura-Shrimp.jpg').convert_alpha()
lettus_rap_img=pygame.image.load('lettuce-wraps.jpg').convert_alpha()
edamame_img=pygame.image.load('Edname.jpg').convert_alpha()
shrimp_img=pygame.transform.scale(shrimp_img, (200, 200))
lettus_rap_img=pygame.transform.scale(lettus_rap_img, (200, 200))
edamame_img=pygame.transform.scale(edamame_img, (200, 200))
beef_img=pygame.image.load('beef.jpg').convert_alpha()
fungus_img=pygame.image.load('fungus.jpg').convert_alpha()
nodels_img=pygame.image.load('nodels.jpg').convert_alpha()
rice_img=pygame.image.load('rice.jpg').convert_alpha()
pickeled_veg_img=pygame.image.load('pickeld_veg.jpg').convert_alpha()
ice_cream_img=pygame.image.load('ice_cream.jpeg').convert_alpha()
pudding_img=pygame.image.load('pudding.jpg').convert_alpha()
cake_img=pygame.image.load('spounge_cake.jpg').convert_alpha()
nodel_plate_img=pygame.image.load('nodel_plate.jpg').convert_alpha()
curry_img=pygame.image.load('cury.jpg').convert_alpha()
salad_img=pygame.image.load('salad.jpg').convert_alpha()
beef_img=pygame.transform.scale(beef_img, (200, 200))
fungus_img=pygame.transform.scale(fungus_img, (200, 200))
nodels_img=pygame.transform.scale(nodels_img, (200, 200))
rice_img=pygame.transform.scale(rice_img, (200, 200))
pickeled_veg_img=pygame.transform.scale(pickeled_veg_img, (200, 200))
ice_cream_img=pygame.transform.scale(ice_cream_img, (200, 200))
pudding_img=pygame.transform.scale(pudding_img, (200, 200))
cake_img=pygame.transform.scale(cake_img, (200, 200))
nodel_plate_img=pygame.transform.scale(nodel_plate_img, (200, 200))
curry_img=pygame.transform.scale(curry_img, (200, 200))
salad_img=pygame.transform.scale(salad_img, (200, 200))
shopping_cart=salad_img=pygame.image.load('shopping_cart.jpg').convert_alpha()
shopping_cart=pygame.transform.scale(shopping_cart, (200, 200))


# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the screen into a variable
width = screen.get_width()

# stores the height of the screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in this font
total_order_cost=0
total_order_tax=total_order_cost*0.0725+total_order_cost
total_order_tax=round(total_order_tax,2)
erm1=0
umm1=0
amm1=0
erm2=0
umm2=0
amm2=0
erm3=0
umm3=0
amm3=0
dum=0
fun=0
erm4=0
umm4=0
amm4=0
erm5=0
umm5=0
amm5=0
intro_text=smallfont.render('Hello welcome to my restrant. Press one of the menus. Then chose the item you like by pressing the number above it.\n Every time you click that button it will add one of those items to your order. When your done finding all of your item press the cart button and you can complete the ordering process there.',True,color)
soda_text= smallfont.render('Soda', True, color)
thai_ice_tea_text= smallfont.render('Thai Ice Tea', True, color)
water_text = smallfont.render('Water', True, color)
edamame_text=smallfont.render('Edname', True, color)
shrimp_text=smallfont.render('Shrimp', True, color)
letus_raps_text=smallfont.render('Letus Raps', True, color)
beef_text=smallfont.render('Extra Protien', True, color)
fungs_text=smallfont.render('Fungus', True, color)
pickeled_veg_text=smallfont.render('Vegtabels', True, color)
nodels_text=smallfont.render('Nodels', True, color)
rice_text=smallfont.render('Rice', True, color)
curry_text=smallfont.render('Curry', True, color)
salad_text=smallfont.render('Salad', True, color)
nodel_plate_text=smallfont.render('Nodel Plate', True, color)
cake_text=smallfont.render('Spounge Cake', True, color)
pudding_text=smallfont.render('Pudding', True, color)
ice_cream_text=smallfont.render('Ice Cream', True, color)
text1 = smallfont.render(str(erm1), True, color)
text2 = smallfont.render(str(umm1), True, color)
text3 = smallfont.render(str(amm1), True, color)
text21 = smallfont.render(str(erm2), True, color)
text22 = smallfont.render(str(umm2), True, color)
text23 = smallfont.render(str(amm2), True, color)
text31 = smallfont.render(str(erm3), True, color)
text32 = smallfont.render(str(umm3), True, color)
text33 = smallfont.render(str(amm3), True, color)
text34 = smallfont.render(str(dum), True, color)
text35 = smallfont.render(str(fun), True, color)
text41 = smallfont.render(str(erm4), True, color)
text42 = smallfont.render(str(umm4), True, color)
text43 = smallfont.render(str(amm4), True, color)
text51 = smallfont.render(str(erm5), True, color)
text52 = smallfont.render(str(umm5), True, color)
text53 = smallfont.render(str(amm5), True, color)
dessert_button = smallfont.render("Dessert menu", True, color)
appatizer_button = smallfont.render("appatizer menu", True, color)
drink_button = smallfont.render("Drink menu", True, color)
entre_button = smallfont.render("Entre menu", True, color)
side_button = smallfont.render("side menu", True, color)
back_button= smallfont.render("Back", True, color)
shopping_cart_button=smallfont.render("Cart",True,color)
# Set the initial position of the button here:
button_1width = 140
button_1height = 40

# Set the button's initial position at the start (e.g., top-left corner)
thai_ice_tea_lx=0
thai_ice_tea_ly=300
soda_img_lx=200
soda_img_ly=300
water_img_lx=400
water_img_ly=300
beef_img_lx=600
fungus_img_lx=800
back_button_lx=350
back_button_ly=700
button_1x = 0  # You can change this value to adjust the horizontal position
button_1y = 200  # You can change this value to adjust the vertical position
button_2x = 200
button_3x = 400
button_4x = 600
button_5x = 800
current_screen = 'menu menu'
def show_drink_menu():
    screen.fill((60, 25, 60))
    screen.blit(soda_text, (soda_img_lx, 100))
    screen.blit(water_text, (water_img_lx, 100))
    screen.blit(thai_ice_tea_text, (thai_ice_tea_lx, 100))
    screen.blit(text1, (button_1x + 50, button_1y))
    screen.blit(text2, (button_2x + 50, button_1y))
    screen.blit(text3, (button_3x + 50, button_1y))
    screen.blit(thai_ice_tea, (thai_ice_tea_lx, thai_ice_tea_ly))
    screen.blit(water_img, (water_img_lx, water_img_ly))
    screen.blit(soda_img, (soda_img_lx, soda_img_ly))
    screen.blit(back_button, (350,700))

def show_appatizer_menu():
    screen.fill((60, 25, 60))
    screen.blit(edamame_text, (soda_img_lx, 100))
    screen.blit(shrimp_text, (water_img_lx, 100))
    screen.blit(letus_raps_text, (thai_ice_tea_lx, 100))
    screen.blit(text21, (button_1x + 50, button_1y))
    screen.blit(text22, (button_2x + 50, button_1y))
    screen.blit(text23, (button_3x + 50, button_1y))
    screen.blit(lettus_rap_img, (thai_ice_tea_lx, thai_ice_tea_ly))
    screen.blit(shrimp_img, (water_img_lx, water_img_ly))
    screen.blit(edamame_img, (soda_img_lx, soda_img_ly))
    screen.blit(back_button, (350,700))

def show_side_menu():
    screen.fill((60, 25, 60))
    screen.blit(nodels_text, (soda_img_lx, 100))
    screen.blit(rice_text, (water_img_lx, 100))
    screen.blit(beef_text, (thai_ice_tea_lx, 100))
    screen.blit(pickeled_veg_text, (beef_img_lx, 100))
    screen.blit(fungs_text, (fungus_img_lx, 100))
    screen.blit(text31, (button_1x + 50, button_1y))
    screen.blit(text32, (button_2x + 50, button_1y))
    screen.blit(text33, (button_3x + 50, button_1y))
    screen.blit(text34, (button_4x + 50, button_1y))
    screen.blit(text35, (button_5x + 50, button_1y))
    screen.blit(beef_img, (thai_ice_tea_lx, thai_ice_tea_ly))
    screen.blit(rice_img, (water_img_lx, water_img_ly))
    screen.blit(nodels_img, (soda_img_lx, soda_img_ly))
    screen.blit(pickeled_veg_img, (beef_img_lx, soda_img_ly))
    screen.blit(fungus_img, (fungus_img_lx, soda_img_ly))
    screen.blit(back_button, (350,700))

def show_entre_menu():
    screen.fill((60, 25, 60))
    screen.blit(curry_text, (soda_img_lx, 100))
    screen.blit(salad_text, (water_img_lx, 100))
    screen.blit(nodel_plate_text, (thai_ice_tea_lx, 100))
    screen.blit(text41, (button_1x + 50, button_1y))
    screen.blit(text42, (button_2x + 50, button_1y))
    screen.blit(text43, (button_3x + 50, button_1y))
    screen.blit(nodel_plate_img, (thai_ice_tea_lx, thai_ice_tea_ly))
    screen.blit(salad_img, (water_img_lx, water_img_ly))
    screen.blit(curry_img, (soda_img_lx, soda_img_ly))
    screen.blit(back_button, (350,700))

def show_dessert_menu():
    screen.fill((60, 25, 60))
    screen.blit(cake_text, (soda_img_lx, 100))
    screen.blit(pudding_text, (water_img_lx, 100))
    screen.blit(ice_cream_text, (thai_ice_tea_lx, 100))
    screen.blit(text51, (button_1x + 50, button_1y))
    screen.blit(text52, (button_2x + 50, button_1y))
    screen.blit(text53, (button_3x + 50, button_1y))
    screen.blit(ice_cream_img, (thai_ice_tea_lx, thai_ice_tea_ly))
    screen.blit(pudding_img, (water_img_lx, water_img_ly))
    screen.blit(cake_img, (soda_img_lx, soda_img_ly))
    screen.blit(back_button, (350,700))

def show_menu_menu():
    screen.fill((60,25,60))
    screen.blit(dessert_button,(0,300))
    screen.blit(ice_cream_img,(0,400))
    screen.blit(drink_button,(200,300))
    screen.blit(water_img,(200,400))
    screen.blit(appatizer_button,(400,300))
    screen.blit(shrimp_img,(400,400))
    screen.blit(side_button,(700,300))
    screen.blit(rice_img,(700,400))
    screen.blit(entre_button,(900,300))
    screen.blit(curry_img,(900,400))
    screen.blit(shopping_cart_button,(350,800))
    screen.blit(shopping_cart,(350,900))

    # if mouse is hovered on a button, it changes to a lighter shade

while True:
    # stores the (x, y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if current_screen == 'menu menu':
            show_menu_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if 0<= mouse[0] <= 0+ button_1width and 300 <= mouse[1] <= 300 + button_1height:
                    current_screen='dessert menu'
                
                if 200<= mouse[0] <= 200+ button_1width and 300<= mouse[1] <= 300+ button_1height:
                    current_screen='drink menu'
                
                if 400 <= mouse[0] <= 400 + button_1width and 300 <= mouse[1] <= 300 + button_1height:
                    current_screen='appatizer menu'
                
                if 700 <= mouse[0] <= 700 + button_1width and 300 <= mouse[1] <= 300 + button_1height:
                    current_screen='side menu'
                
                if 900 <= mouse[0] <= 900 + button_1width and 300 <= mouse[1] <= 300 + button_1height:
                    current_screen='entre menu'

                if 900 <= mouse[0] <= 900 + button_1width and 300 <= mouse[1] <= 300 + button_1height:
                    current_screen='checkout'

                if 0 <= mouse[0] <= 0 + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [0, button_1y, button_1width, button_1height])

                if 200 <= mouse[0] <= 200 + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [200, button_1y, button_1width, button_1height])
                
                if 400 <= mouse[0] <= 400 + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [400, button_1y, button_1width, button_1height])

                if 700 <= mouse[0] <= 700 + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [700, back_button_ly, button_1width, button_1height])
                
                if 900 <= mouse[0] <= 900 + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [900, back_button_ly, button_1width, button_1height])                                                                                                                                                              
        if current_screen == 'drink menu':
            show_drink_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    erm1+=1
                    total_order_cost+=5.35
                    text1 = smallfont.render(str(erm1), True, color)
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    umm1+=1
                    total_order_cost+=3.15
                    text2 = smallfont.render(str(umm1), True, color)
                
                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    amm1+=1
                    total_order_cost+=0.00
                    text3 = smallfont.render(str(amm1), True, color)
                
                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    current_screen='menu menu'
                                
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_1x, button_1y, button_1width, button_1height])

                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_3x, button_1y, button_1width, button_1height])
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_2x, button_1y, button_1width, button_1height])

                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [back_button_lx, back_button_ly, button_1width, button_1height])

        if current_screen == 'appatizer menu':
            show_appatizer_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    erm2+=1
                    total_order_cost+=5.00
                    text21 = smallfont.render(str(erm2), True, color)
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    umm2+=1
                    total_order_cost+=2.00
                    text22 = smallfont.render(str(umm2), True, color)
                
                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    amm2+=10.50
                    text23 = smallfont.render(str(amm2), True, color)

                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    current_screen='menu menu'                    
            
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_1x, button_1y, button_1width, button_1height])

                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_3x, button_1y, button_1width, button_1height])
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_2x, button_1y, button_1width, button_1height])

                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [back_button_lx, back_button_ly, button_1width, button_1height])

        if current_screen == 'side menu':
            show_side_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    erm3+=1
                    total_order_cost+=0.50
                    text31 = smallfont.render(str(erm3), True, color)
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    umm3+=1
                    total_order_cost+=1.20
                    text32 = smallfont.render(str(umm3), True, color)
                
                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    amm3+=1
                    total_order_cost+=1.20
                    text33 = smallfont.render(str(amm3), True, color)
                
                if button_4x <= mouse[0] <= button_4x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    dum+=1
                    total_order_cost+=0.50
                    text34 = smallfont.render(str(dum), True, color)
                
                if button_5x <= mouse[0] <= button_5x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    fun+=1
                    total_order_cost+=4.00
                    text35 = smallfont.render(str(fun), True, color)
                
                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    current_screen='menu menu'                    
            
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_1x, button_1y, button_1width, button_1height])

                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_3x, button_1y, button_1width, button_1height])
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_2x, button_1y, button_1width, button_1height])
                
                if button_4x <= mouse[0] <= button_4x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_4x, button_1y, button_1width, button_1height])
                
                if button_5x <= mouse[0] <= button_5x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_5x, button_1y, button_1width, button_1height])

                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [back_button_lx, back_button_ly, button_1width, button_1height])

        if current_screen == 'entre menu':
            show_entre_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    erm4+=1
                    text41 = smallfont.render(str(erm4), True, color)
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    umm4+=1
                    text42 = smallfont.render(str(umm4), True, color)
                
                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    amm4+=1
                    text43 = smallfont.render(str(amm4), True, color)
                    
                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    current_screen='menu menu'

                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_1x, button_1y, button_1width, button_1height])

                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_3x, button_1y, button_1width, button_1height])
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_2x, button_1y, button_1width, button_1height])
                
                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [back_button_lx, back_button_ly, button_1width, button_1height])

        if current_screen == 'dessert menu':
            show_dessert_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    erm5+=1
                    total_order_cost+=5.00
                    text51 = smallfont.render(str(erm5), True, color)
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    umm5+=1
                    total_order_cost+=3.00
                    text52 = smallfont.render(str(umm5), True, color)
                
                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    amm5+=1
                    total_order_cost+=2.50
                    text53 = smallfont.render(str(amm5), True, color)
                
                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    current_screen='menu menu'                    
            
                if button_1x <= mouse[0] <= button_1x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_1x, button_1y, button_1width, button_1height])

                if button_3x <= mouse[0] <= button_3x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_3x, button_1y, button_1width, button_1height])
                
                if button_2x <= mouse[0] <= button_2x + button_1width and button_1y <= mouse[1] <= button_1y + button_1height:
                    pygame.draw.rect(screen, color_light, [button_2x, button_1y, button_1width, button_1height])

                if back_button_lx <= mouse[0] <= back_button_lx + button_1width and back_button_ly <= mouse[1] <= back_button_ly + button_1height:
                    pygame.draw.rect(screen, color_light, [back_button_lx, back_button_ly, button_1width, button_1height])               

    # superimposing the text onto our button


    # updates the frames of the game
    pygame.display.update()