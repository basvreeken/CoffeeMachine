class Coffee:
    def __init__(self, water, milk, beans, price):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price


espresso = Coffee(250, 0, 16, 4)
latte = Coffee(350, 75, 20, 7)
cappuccino = Coffee(200, 100, 12, 6)


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = 'off'
        self.products = [espresso, latte, cappuccino]
        self.messages = ['Write action (buy, fill, take, remaining, exit):',
                         'What do you want to buy? 1 - espresso, 2 - latte, '
                         '3 - cappuccino:',
                         'Write how many ml of water you want to add:',
                         'Write how many ml of milk do you want to add:',
                         'Write how many grams of coffee beans do you want '
                         'to add:',
                         'Write how many disposable cups of coffee do you '
                         'want to '
                         'add:']

    def __str__(self):
        return f'''\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money'''

    def buy(self, product):
        if self.enough_resources(product):
            print('I have enough resources, making you a coffee!')
            self.water -= product.water
            self.milk -= product.milk
            self.beans -= product.beans
            self.cups -= 1
            self.money += product.price

    def enough_resources(self, product):
        if self.water < product.water:
            print('Sorry, not enough water!')
            return False
        if self.milk < product.milk:
            print('Sorry, not enough milk!')
            return False
        if self.beans < product.beans:
            print('Sorry, not enough coffee beans!')
            return False
        if self.cups < 1:
            print('Sorry, not enough disposable cups!')
            return False
        else:
            return True

    def take(self):
        print(f'\nI gave you ${self.money}')
        self.money = 0

    def do_task(self, state, msg_index):
        self.state = state
        print('\n' + self.messages[msg_index])

    def do(self, job):
        if job == 'start':
            self.do_task('on', 0)
        elif job == 'buy':
            self.do_task('buy', 1)
        elif job in ['1', '2', '3'] and self.state == 'buy':
            self.buy(self.products[int(job) - 1])
            self.do_task('on', 0)
        elif job == 'back':
            self.do_task('on', 0)
        elif job == 'fill':
            self.do_task('fill_water', 2)
        elif job and self.state == 'fill_water':
            self.water += int(job)
            self.do_task('fill_milk', 3)
        elif job and self.state == 'fill_milk':
            self.milk += int(job)
            self.do_task('fill_beans', 4)
        elif job and self.state == 'fill_beans':
            self.beans += int(job)
            self.do_task('fill_cups', 5)
        elif job and self.state == 'fill_cups':
            self.cups += int(job)
            self.do_task('on', 0)
        elif job == 'take':
            self.take()
            self.do_task('on', 0)
        elif job == 'remaining':
            print(self.__str__())
            self.do_task('on', 0)
        elif job == 'exit':
            self.state = 'off'
            exit()
        else:
            print('Unknown command...')
            self.do_task('on', 0)


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    if coffee_machine.state == 'off':
        coffee_machine.do('start')
    else:
        coffee_machine.do(input())
