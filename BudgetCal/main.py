drinks = float(input('Enter quantity of drinks: '))
drinks_price = float(input('Enter drinks price: '))
pastries = float(input('Enter quantity of pastries: '))
pastries_price = float(input('Enter pastries price: '))
food_facilitators = float(input('Enter quantity of food for facilitators: '))
food_facilitators_price = float(input('Enter price of food: '))
bottle_water_for_facilitators = float(input('Enter quantity of bottle water: '))
bottle_water_price = float(input('Enter quantity of bottle water: '))
bag_of_water = float(input("Enter quantity of bags of water: "))
price_of_bag_of_water = float(input("Price of bags of water: "))
honorarium = float(input('Enter quantity of honorarium: '))
price_of_honorarium = float(input("Enter price for honorarium: "))


total = (drinks * drinks_price)+ (pastries * pastries_price) + (food_facilitators_price * food_facilitators) + (bottle_water_for_facilitators * bottle_water_price) + (bag_of_water * price_of_bag_of_water) + (honorarium * price_of_honorarium)
print("\n\n#####################################################\n")
print("\nTotal : " + str(total))

print("\n6% of the total \n")
six_percent = total * 0.06
print(six_percent)


print("\n Sub total \n")
sub_total = total + six_percent
print(sub_total)


print("\n15% of the sub total \n")
fifteen_percent = sub_total * 0.15
print(fifteen_percent)

print("\n**** GRAND TOTAL **** \n")
grand_total = sub_total + fifteen_percent
print(grand_total)
