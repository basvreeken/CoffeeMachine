# contents ((water, milk, coffee beans, money, disposable cups)
coffee_machine = [400, 540, 120, 550, 9]

# products (water, milk, coffee beans, price)
espresso = (250, 0, 16, 4)
latte = (350, 75, 20, 7)
cappuccino = (200, 100, 12, 6)
products = [espresso, latte, cappuccino]


def print_state():
    print('\nThe coffee machine has:')
    print(coffee_machine[0], 'of water')
    print(coffee_machine[1], 'of milk')
    print(coffee_machine[2], 'of coffee beans')
    print(coffee_machine[4], 'of disposable cups')
    print(coffee_machine[3], 'of money')
    print()


def buy(product):
    for i in range(0, 3):
        coffee_machine[i] -= product[i]
    coffee_machine[3] += product[3]
    coffee_machine[4] -= 1
    print_state()


def fill(water, milk, beans, cups):
    coffee_machine[0] += water
    coffee_machine[1] += milk
    coffee_machine[2] += beans
    coffee_machine[4] += cups
    print_state()


def take():
    print(f'I gave you ${coffee_machine[3]}')
    coffee_machine[3] = 0
    print_state()


print_state()
action = input('Write action (buy, fill, take):\n')

if action == 'buy':
    choice = int(input('What do you want to buy? 1 - espresso, 2 - latte, '
                       '3 - cappuccino: \n'))
    buy(products[choice - 1])
elif action == 'fill':
    water = int(input('Write how many ml of water you want to add:\n'))
    milk = int(input('Write how many ml of milk you want to add:\n'))
    beans = int(input('Write how many grams of coffee beans you want to '
                      'add:\n'))
    cups = int(input('Write how many ml of coffee cups you want to add:\n'))
    fill(water, milk, beans, cups)
elif action == 'take':
    take()
