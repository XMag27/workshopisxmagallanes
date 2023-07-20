#create a function that shows a restaurant menu
mealsdictionary = {}
mealsdictionary["Hamburger"] = 5.00
mealsdictionary["Hot Dog"] = 3.00
mealsdictionary["Pizza"] = 7.00
mealsdictionary["Salad"] = 4.00
mealsdictionary["Soup"] = 3.50
mealsdictionary["Chicken"] = 5.50
mealsdictionary["Fries"] = 2.50
mealsdictionary["Ice Cream"] = 2.00
specials = {}
specials["Double Hamburger"] = 10.00
specials["Double Hot Dog"] = 6.00
specials["Double Pizza"] = 14.00
specials["Double Salad"] = 8.00




def showMenu():
    print("Menu")
    for key in mealsdictionary:
        print(key, mealsdictionary[key])
    print("Specials")
    for key in specials:
        print(key, specials[key])

def getOrder():
    isOrdering = True
    order = {}
    totalofmeals = 0
    while isOrdering:
        meal = input("What would you like to order? ")
        if meal in mealsdictionary:
            quantity = int(input("How many? "))
            if quantity > 0 and quantity < 100:
                order[meal] = quantity
            else:
                print("Please enter a valid quantity")
        else:
            print("Sorry, we don't have that")
        another = input("Would you like to order another meal? ")
        if another == "no":
            isOrdering = False
    return order
def getCost(order):
    total = 0
    for key in order:
        try:
            total = total + (mealsdictionary[key] * order[key])
        except KeyError:
            total = total + (specials[key] * order[key])
    if len(order) > 5:
        total = total * 0.9
    if len(order) > 10:
        total = total * 0.8
    return total

def applyDiscount(total):
    if total > 50:
        total = total - 10
    if total > 100:
        total = total - 25
    return total

def askConfirmation(total):
    confirmation = input("Are you sure you want to order? Your total is: " + str(total) + " ")
    if confirmation == "yes":
        return True      
    elif confirmation == "no":
        #order again
        return False

showMenu()
order = getOrder()
total = getCost(order)
total = applyDiscount(total)
isOrdering = askConfirmation(total)
if isOrdering:
    print("Your order has been placed. Thank you!")
    print("Your total is: " + str(total) + " You can pay at the counter")
else:
    print("Your order has been cancelled. Thank you!")

#define test cases


