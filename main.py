from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money = MoneyMachine()
machine_on = True
while machine_on:
    items = Menu()
    # takes the input of the drink name
    drink_name = input(f"what would you like? {items.get_items()}")
    if drink_name  == 'report':
        money.report()
    elif drink_name == 'off':
        machine_on = False
    #return a menu item if the name exits
    else:
        drink = items.find_drink(drink_name)
        coffee__maker = CoffeeMaker()
        if money.make_payment(drink.cost):
            if coffee__maker.is_resource_sufficient(drink):
                coffee__maker.make_coffee(drink)












