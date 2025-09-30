class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def budget_check(self, budget):
        if not isinstance(budget, (int, float)):  # Check if budget is a number
            print("Invalid entry. Please enter a number: ")
            exit()

    def change(self, budget):  # Calculate change after purchase
        return budget - self.price
    
    def purchase(self, budget):
        self.budget_check(budget)  # Validate budget input

        if budget >= self.price:  # Check if budget is sufficient
            print(f"Thank you for purchasing {self.name}!")

        if budget == self.price:  # Exact budget case
            print("You have the exact amount of money to buy shoes, therefore, no change.")  

        else:  # Budget exceeds price case
            print(f"Lucky you!!!You can buy shoes and still have change left.")

            exit("Than you for shopping with us!")  # Exit after purchase
            