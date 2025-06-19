menu = {
  'coffee' : 20,
  'pizza':250,
  'burger':99,
}

print("Welcome to our resturant")

print("coffee:Rs 20\npizza:Rs250\nburger:Rs99")

order_total = 0

item_1 = input("Enter your the name of dish you want to try : ")
if item_1 in menu:
  order_total += menu[item_1]
  print(f"your item {item_1} has added into oder list :")

  another_order = input("If you want to add another order (yes/no) :" )
  if another_order == "yes":

    item_2 = input("please enter second item : ")
    if item_2 in menu:
      order_total += menu[item_2] 
      print(f"Item {item_2} has been added in to your cart :")

    else:
      print(f"order item{item_2} is not available")
  print(f"total amount to pay is{order_total}")

else:
  print(f"order item {item_1} is not available :")
 