# https://www.techbeamers.com/python-multiline-string/ helped me with multiline strings
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

# https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf helped me with while loops
while order != "quit":
  #  https://www.geeksforgeeks.org/python-check-whether-given-key-already-exists-in-a-dictionary/ helped me with if ... in ... logic
  if order in meal: 
    #  https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf helped me with dictionaries
    meal.update({order: meal[order] + 1})
    print("\n**" + str(meal[order]) + " orders of " + order + " have been added to your meal**\n")
  #  https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf helped me with if else statements
  else:
    meal.update({order: 1})
    print("\n**" + str(meal[order]) + " order of " + order + " have been added to your meal**\n")
  order = input()

# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/ helped me with exit command
quit()