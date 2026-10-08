# U1 Coding with Python Lesson 1 - Project

fruit_prices = {
    "apple": 0.75,
    "banans": 0.40,
    "orange": 0.60
}
# above is a dictionary storing fruits and their prices


#order variables
selected_fruit = "apple"
quantity = 5
is_member = True

# check if item exsits in inventory
if selected_fruit in fruit_prices:
    price_per_item = fruit_prices[selected_fruit]
    subtotal = price_per_item * quantity

    # apply discount if quantity is 5 or more and user is a member
    if quantity >= 5 and is_member:
        discount = 0.50
        total_cost = subtotal - discount
        print("discount applied")
    else:
        total_cost = subtotal # if the user is not a member than they pay full price

    print("item: " + selected_fruit) # this selects the item (apple) and prints
    print("total price: £" + str(total_cost)) # this prints the total price
    
