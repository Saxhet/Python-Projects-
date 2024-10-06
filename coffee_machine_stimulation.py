
from main import coffee
print("☕ Welcome to SRS Coffee Station")
print(coffee)

# TODO 1. create a dictionary for MENU
coffee_menu={
    "espresso" : {
        "ingredients":{
           "water": 50,
            "coffee":18,
            'milk':00
        },
        "cost":1.50
    },
    "latte":{
        "ingredients" : {
            "water":200,
            "coffee":24,
            'milk':150
        },
        "cost":2.50
    },
    "cappuccino" :{
        "ingredients" :
        { "water":250,
           "coffee" :24,
           "milk":100
        },
        "cost":3
    }
}
# TODO 2. Make a dictionary of resources
machine_resources={
    "water":300,
    "milk":300,
    "coffee":100
}
machine_status="on"
def coffee_machine():
    global machine_status

    #TODO input from user
    user_order=(input("What would you like(espresso,latte,cappuccino)")).lower()

    #TODO create a report
    report1=(f"water:{machine_resources['water']}\n"
             f"coffee:{machine_resources['coffee']}\n"
             f"milk:{machine_resources['milk']}")

    #TODO calculate coins
    def process_coin():
        print("Please insert coins in the machine")
        penny=0.01*float(input(" No of Penny"))
        nickel=0.05*float(input("No of Nickel"))
        rime=0.10*float(input("No of Rime"))
        quarter=0.25*float(input("No of Rime"))
        total_money= penny+nickel+rime+quarter

        if total_money > coffee_menu[user_order]["cost"]:
            coin_change=round(total_money - coffee_menu[user_order]["cost"],2)
            print(f"Here is your change {coin_change}")
            # print("Here is your Coffee Enjoy!")
        else:
            print("sorry that's not enough money")
            coffee_machine()

    #TODO reduce the resources and update
    def update_resources():
        remaining_water = (machine_resources["water"]) - (coffee_menu[user_order]["ingredients"]["water"])
        machine_resources["water"] = remaining_water
        remaining_coffee = (machine_resources['coffee'] - coffee_menu[user_order]['ingredients']['coffee'])
        machine_resources['coffee'] = remaining_coffee
        remaining_milk = (machine_resources['milk'] - coffee_menu[user_order]['ingredients']['milk'])
        machine_resources['milk'] = remaining_milk
        # print(machine_resources)



    #TODO check for the resources
    if user_order=="report":
        print((f"water:{machine_resources['water']}\n"
             f"coffee:{machine_resources['coffee']}\n"
             f"milk:{machine_resources['milk']}"))
        coffee_machine()
    elif user_order=='off':
        machine_status="off"

    elif user_order=="refill":
        machine_resources['water']=300
        machine_resources['coffee']=100
        machine_resources['milk']=300
        coffee_machine()


    else:
        if machine_resources['water']>= coffee_menu[user_order]['ingredients']['water']:
            if machine_resources['coffee'] >= coffee_menu[user_order]['ingredients']['coffee']:
                if machine_resources['milk']>= coffee_menu[user_order]['ingredients']['milk']:
                    process_coin()
                    update_resources()
                    print("Here is your coffee,Enjoy!")
                    coffee_machine()

                else:
                    print("Sorry not sufficient milk")
            else:
                print("Sorry not sufficient coffee")
        else:
            print("sorry not  enough water")

while machine_status=="on":
    coffee_machine()

