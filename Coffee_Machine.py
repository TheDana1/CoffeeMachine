class Coffee_Machine():
    def __init__(self, amount_water, amount_milk, amount_beans, amount_cups, amount_money):
        self._water = amount_water
        self._milk = amount_milk
        self._beans = amount_beans
        self._cups = amount_cups
        self._money = amount_money

    def status(self):
        print("The coffee machine has:")
        print(str(self._water) + " of water")
        print(str(self._milk) + " of milk")
        print(str(self._beans) + " of coffee beans")
        print(str(self._cups) + " of disposable cups")
        print("$" + str(self._money) + " of money")

    def options(self):
        print("Write action (buy, fill, take, remaining, exit):")
        answer = input()
        if (answer == "buy"):
            self.buy()
        elif (answer == "fill"):
            self.fill()
        elif (answer == "take"):
            self.take()
        elif (answer == "remaining"):
            self.status()
            self.loop(1)
        elif (answer == "exit"):
            print("bye")
        else:
            print("not applicable")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        reply = input()
        if reply == "back":
            self.options()
        elif (int(reply) == 1):
            if (self._beans > 16 and self._water > 250 and self._cups > 1):
                print("I have enough resources, making you a coffee!")
                self._money += 4
                self._beans -= 16
                self._water -= 250
                self._cups -= 1
                self.loop(1)
            else:
                if (self._beans < 16):
                    print("Sorry, not enough coffee beans!")
                elif self._water < 250:
                    print("Sorry, not enough water!")
                else:
                    print("Sorry, not enough disposable cups!")
                self.loop(1)
        elif (int(reply) == 2):
            if (self._beans > 20 and self._water > 350 and self._cups > 1 and self._milk > 75):
                print("I have enough resources, making you a coffee!")
                self._milk -= 75
                self._money += 7
                self._beans -= 20
                self._water -= 350
                self._cups -= 1
                self.loop(1)
            else:
                if (self._beans < 20):
                    print("Sorry, not enough coffee beans!")
                elif self._water < 350:
                    print("Sorry, not enough water!")
                elif self._cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough milk!")
                self.loop(1)
        else:
            if (self._beans > 12 and self._water > 200 and self._cups > 1 and self._milk > 100):
                print("I have enough resources, making you a coffee!")
                self._milk -= 100
                self._money += 6
                self._beans -= 12
                self._water -= 200
                self._cups -= 1
                self.loop(1)
            else:
                if (self._beans < 12):
                    print("Sorry, not enough coffee beans!")
                elif self._water < 200:
                    print("Sorry, not enough water!")
                elif self._cups < 1:
                    print("Sorry, not enough disposable cups!")
                else:
                    print("Sorry, not enough milk!")
                self.loop(1)

    def fill(self):
        print("Write how many ml of water you want to add:")
        water_ml = int(input())
        self._water += water_ml
        print("Write how many ml of milk you want to add:")
        milk_ml = int(input())
        self._milk += milk_ml
        print("Write how many grams of coffee beans you want to add:")
        g_beans = int(input())
        self._beans += g_beans
        print("Write how many disposable coffee cups you want to add:")
        cup_num = int(input())
        self._cups += cup_num
        self.loop(1)

    def take(self):
        total_money = self._money
        self._money -= total_money
        print("I gave you $" + str(total_money))
        self.loop(1)

    def loop(self, option):
        if option == 1:
            order = Coffee_Machine(
                self._water, self._milk, self._beans, self._cups, self._money)
            order.options()


order1 = Coffee_Machine(400, 540, 120, 9, 550)
order1.options()
