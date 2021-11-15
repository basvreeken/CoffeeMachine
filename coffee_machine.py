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

number_of_cups = int(input('Write how many cups of coffee you will need:\n'))

print(f'For {number_of_cups} cups of coffee you will need:')
print(str(number_of_cups * water) + ' ml of water')
print(str(number_of_cups * milk) + ' ml of milk')
print(str(number_of_cups * coffee_beans) + ' g of coffee beans')
