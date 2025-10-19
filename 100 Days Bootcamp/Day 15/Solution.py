class CoffeeMachine:
    def __init__(
        self, water: int = 100, milk: int = 50, coffee: int = 76, money: float = 2.5
    ):
        """Initialize the CoffeeMachine with the given resources.

        Args:
            water (int, optional): The amount of water in ml. Defaults to 100.
            milk (int, optional): The amount of milk in ml. Defaults to 50.
            coffee (int, optional): The amount of coffee in grams. Defaults to 76.
            money (float, optional): The amount of money in dollars. Defaults to 2.5.
        """
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "money": money,
        }
        self.options = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
        }

    def report(self) -> None:
        """Print a report of the current resource levels."""
        print(
            f"Water: {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}g\n"
            f"Money: ${self.resources['money']}"
        )

    def ask(self):
        """Prompt the user for their coffee choice and process the order."""
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            self.report()
            return None
        elif choice in self.options:
            money = float(input("Please insert coins: $"))
            if money >= self.options[choice]["cost"]:
                self.resources["money"] += self.options[choice]["cost"]
                for item in self.options[choice]:
                    if item != "cost":
                        self.resources[item] -= self.options[choice][item]
                print(
                    f"Here is your change: ${money - self.options[choice]['cost']:.2f}"
                )
            else:
                print("Sorry, that's not enough money.")
            return choice
        else:
            print("Invalid choice.")
            return None

    def run(self):
        """Run the coffee machine until a valid order is processed."""
        while True:
            result = self.ask()
            if result is None:
                continue
            else:
                print(f"Here is your {result}. Enjoy!")
                break
