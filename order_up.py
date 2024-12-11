class Order:
    def __init__(self, drink=None, appetizer=None, main_course=None, first_side=None, secound_side=None, dessert=None ):
        self.drink=drink
        self.appetizer=appetizer
        self.main_course=main_course
        self.first_side=first_side
        self.secound_side=secound_side
        self.dessert=dessert
        self.Order_list=[]
        self.Full_menu_value=[]
        self.Full_menu={'Soda':3.15, 'Water':0.00, 'Cury':10, 'Rice':1.20, 'Thai Ice Tea':5.35, 'Nodels':1.20, 'Nodel Plate': 12.00, 'Pickiled Veg':.50, 'Extra Protien':.50, 'Salad':7.00, 'Wood Ear Mushroom':4.00, 'Spounge Cake':3.00, 'Pudding':2.50, 'Icecream':5.00, 'Edamame':2.00, 'Shrimp':10.50, 'Letus Raps':5.00}   
        self.drink_menu=['Soda', 'Water', 'Thai Ice Tea']
        self.appetizer_menu=['Edamame', 'Shrimp', 'Letus Raps']
        self.side_menu=['Rice', 'Nodels', 'Pickled Veg', 'Extra Protien', 'Wood Ear Mushroom']
        self.main_course_menu=['Cury', 'Salad', 'Nodel Plate']
        self.dessert_menu=['Spounge Cake', 'Pudding', 'Icecream']
        self.Full_menu_value=list(self.Full_menu.values())
        self.Order_cost=[]
    
    def add_order(self):
        total=0
        for i in range(len(self.Order_cost)):
            total+=(self.Order_cost[i])
        grand_total=total*0.047+total
        x=round(grand_total,2)
        print('Your subtotal is',str(total)+'.')
        print('Your grand total is',str(x)+'.')

    def drink_check(self,item):
        while True:
            if item in self.Full_menu:
                self.Order_list.append(item)
                res = list(self.Full_menu.keys()).index(item)
                self.Order_cost.append(self.Full_menu_value[res])
                break

            elif item=='0':
                break

            else:
                item =input("That drink is not on the menu. The choices are Soda, Water, Thai Ice Tea.: ") 
    
    def appetizer_check(self,item):
        while True:
            if item in self.Full_menu:
                self.Order_list.append(item)
                res = list(self.Full_menu.keys()).index(item)
                self.Order_cost.append(self.Full_menu_value[res])
                break
            
            elif item=='0':
                break

            else:
                item =input("That appetizer is not on the menu. The choices are Edamame, Shrimp, Letus Raps.: ")

    def side_check(self,item):
        while True:
            if item in self.Full_menu:
                self.Order_list.append(item)
                res = list(self.Full_menu.keys()).index(item)
                self.Order_cost.append(self.Full_menu_value[res])
                break

            elif item=='0':
                break

            else:
                item =input("That side is not on the menu. The choices are Rice, Nodels, Pickled Veg, Extra Protien, Wood Ear Mushroom.: ")

    def main_course_check(self,item):
        while True:
            if item in self.Full_menu:
                self.Order_list.append(item)
                res = list(self.Full_menu.keys()).index(item)
                self.Order_cost.append(self.Full_menu_value[res])
                break

            elif item=='0':
                break

            else:
                item =input("That main course is not on the menu. The choices are Cury, Salad, Nodel Plate.: ") 

    def dessert_check(self,item):
        while True:
            if item in self.Full_menu:
                self.Order_list.append(item)
                res = list(self.Full_menu.keys()).index(item)
                self.Order_cost.append(self.Full_menu_value[res])
                break

            elif item=='0':
                break

            else:
                item =input("That dessert is not on the menu. The choices are Spounge Cake, Pudding, Icecream.: ") 

    def lst_check(self):
        if self.Order_list != []:
            print("Your order is",str(self.Order_list)+".")
            return True
        
        else:
            print("That's not an acseptable order. Try again.")
            return False




order1=Order()

x = False
while x == False:
    drink_item=input("For a drink would you want Soda, Water, Thai Ice Tea, or nothing(for nothing press 0 then enter)?: ")
    order1.drink_check(drink_item)
    appetizer_item=input("For an appetizer would you want Edamame, Shrimp, Letus Raps, or nothing(for nothing press 0 then enter)?: ")
    order1.appetizer_check(appetizer_item)
    main_course_item=input("For a main course would you want Cury, Salad, Nodel Plate, or nothing(for nothing press 0 then enter)?: ")
    order1.main_course_check(main_course_item)
    first_side_item=input("For a first side would you want Rice, Nodels, Pickled Veg, Extra Protien, Wood Ear Mushroom, or nothing(for nothing press 0 then enter)?: ")
    order1.side_check(first_side_item)
    secound_side_item=input("For a secound side would you want Rice, Nodels, Pickled Veg, Extra Protien, Wood Ear Mushroom, or nothing(for nothing press 0 then enter)?: ")
    order1.side_check(secound_side_item)
    dessert_item=input("For a dessert would you want Spounge Cake, Pudding, Icecream, or nothing(for nothing press 0 then enter)?: ")
    order1.dessert_check(dessert_item)
    x=order1.lst_check()

order1.add_order()