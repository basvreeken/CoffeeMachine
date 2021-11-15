# Stage 1/6
# print('''Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!''')

# ingredients per cup in ml
water = 200
milk = 50
coffee_beans = 15  # grams

# Stage 2/6
# number_of_cups = int(input('Write how many cups of coffee you will need:\n'))
#
# print(f'For {number_of_cups} cups of coffee you will need:')
# print(str(number_of_cups * water) + ' ml of water')
# print(str(number_of_cups * milk) + ' ml of milk')
# print(str(number_of_cups * coffee_beans) + ' g of coffee beans')

water_available = int(input('Write how many ml of water the coffee machine '
                            'has:\n'))
milk_available = int(input('Write how many ml of milk the coffee machine '
                           'has:\n'))
coffee_beans_available = int(input('Write how many grams of coffee beans the '
                                   'coffee machine has:\n'))
cups_needed = int(input('Write how many cups of coffee you will need:\n'))
maximum_capacity = [int(water_available / water), int(milk_available / milk),
                    int(coffee_beans_available / coffee_beans)]
maximum_cups = min(maximum_capacity)

if cups_needed == maximum_cups:
    print('Yes, I can make that amount of coffee')
elif cups_needed > maximum_cups:
    print(f'No, I can make only {maximum_cups} cups of coffee')
elif cups_needed < maximum_cups:
    n = maximum_cups - cups_needed
    print(f'Yes, I can make that amount of coffee (and even {n} more than '
          f'that)')
