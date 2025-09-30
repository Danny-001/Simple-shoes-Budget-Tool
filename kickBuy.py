from kicks import Shoes

cheap = Shoes("Crock Shoes", 20)
average = Shoes("Nike Air Force 1", 100)
expensive = Shoes("Yeezy Boost 350", 250)

try:
    user_budget = float(input("Enter your budget: "))  # Prompt user for budget
except ValueError:
    exit("Invalid entry. Please enter a number.")

for shoe in (expensive, average, cheap):
    shoe.purchase(user_budget)  # Attempt to purchase each shoe with the user's budget
    