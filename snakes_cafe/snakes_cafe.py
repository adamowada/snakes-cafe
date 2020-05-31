menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""

print(menu)

meal = {}

order = input()

while order != "quit":
  if order in meal:
    meal.update({order: meal[order] + 1})
    print("\n**" + str(meal[order]) + " orders of " + order + " have been added to your meal**\n")
  else:
    meal.update({order: 1})
    print("\n**" + str(meal[order]) + " order of " + order + " have been added to your meal**\n")
  order = input()

quit()