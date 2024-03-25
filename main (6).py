import valid as v
#******************************************************************************
# Author:           Kimberly Rodriguez
# Title:            Discount Calculator Program
# Date:             03/24/2024
# Description:      This program will calculate the discounted price of an
#                   item and the amount saved. You are given a choice to
#                   enter as many items as you like and the program will
#                   output the total price and the total amount saved.
#******************************************************************************
ADD_ITEM = 1
QUIT = 2

def main():
  item = ''
  price = 0.0
  discount = 0.0
  savings = 0
  choice = 0
  count = 0
  total_payment = 0.0
  total_savings = 0.0
  
  print_intro()

  while (choice != QUIT):
    print_menu()
    choice = get_choice()

    if choice == ADD_ITEM:
      item = get_item()
      price = get_price()
      discount = get_discount()
    
      total_discount = calc_total_discount(discount, price)
      savings = calc_savings(price, total_discount)
      print_results(item, total_discount, savings)

      total_payment += total_discount
      total_savings += savings
      count +=1
      
  print_totals(total_payment, total_savings, count)
  print_goodbye()


def print_intro():
  """
  Prints the information about the program to the user
  :param: none
  :return: none
  """
  print("Welcome to my discount shopping program!")
  print("\nThis program will calculate the discount"
        + "and savings for your purchase.\n")
  print("\nLet's get started!\n")


def print_menu():
  """
  Prints the menu to the user
  :param: none
  :return: none
  """
  print("1. Add item")
  print("2. Quit")
  

def get_choice():
  """
  Prompts the user for a choice and returns it
  :param: none
  :return: choice as an integer
  """
  choice = 0
  choice = v.get_integer("\nEnter menu choice: ")
  while choice < 1 or choice > 2:
    print("Only 1 or 2 is allowed,")
    choice = v.get_integer("\nEnter menu choice: ")
  print(" ")
  return choice  
  

def get_item():
  """
  Prompts the user for the name of the item
  :param: none
  :return: item as a string
  """
  item = ''
  item = input("Please enter your item of purchase: ")
  while item == "":
    print("Item cannot be blank.\n")
    item = input("Please enter your item of purchase: ")
  return item


def get_price():
  """
  Prompts the user for the price of the item
  :param: none
  :return: price as a float
  """
  price = 0.0
  price = v.get_float("Please enter the price of your item: ")
  while price < 0:
    print("Price cannot be negative.\n")
    price = v.get_float("Please enter the price of your item: ")
  return price


def get_discount():
  """
  Prompts the user for the discount of the item
  :param: none
  :return: discount as a float
  """
  discount = 0.0
  discount = v.get_float("Please enter the discount as an integer: ")
  while discount < 0 or discount > 100:
    print("Discount must be between 0 and 100.\n")
    discount = v.get_float("Please enter the discount as an integer: ")
  return discount


def calc_total_discount(discount, price):
  """
  Calculates the total discount
  :param discount: float with the discount
  :param price: float with the price
  """
  total_discount = 0.0
  decimal = discount / 100
  total_discount = price * (1 - decimal)
  return total_discount


def calc_savings(price, total_discount):
  """
  Calculates the savings
  :param price: float with the price
  :param total_discount: float with the total discount
  """
  savings = 0.0
  savings = price - total_discount
  return savings


def print_results(item, total_discount, savings):
  """
  Prints the results to the user
  :param item: string with the item
  :param total_discount: float with the total discount
  :param savings: float with the savings
  """
  print(f'\nYour total for {item} is:'
        + f' ${total_discount:.2f}, Great! You saved: ${savings:.2f}\n')


def print_totals(total_payment, total_savings, count):
  """
  Prints the totals to the user
  :param total_payment: float with the total payment
  :param total_savings: float with the total savings
  :param count: integer with the number of items
  """
  print(f'\nTotal number of items: {count}')
  print(f'You payed: ${total_payment:.2f} after the discounts')
  print(f'You saved: ${total_savings:.2f} in total')


def print_goodbye():
  """
  Prints a goodbye message to the user
  :param: none
  :return: none
  """
  print("\nThank you for using my discount shopping program!")


main()
