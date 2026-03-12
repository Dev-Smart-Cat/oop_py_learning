# Importing module die
import random

class Die:
    """A class to show the result after rolling the die.
    
    Attributes:
        value (int): the value containing the number after rolling the die.

    Methods:
        roll (self):
            Return the current value after rolling the die.
    """

    def __init__(self, value=None):
        """Initialize an instance of die.

        Defines the value variable as non-public, meaning it cannot be modified.
        """
        self._value = value

    @property
    def value(self):
        """Returns the value of the die."""
        return self._value
    
    def roll(self):
        """Return the value of the die.

        This method represents the die rolling thanks to the method randint() that choose random 
        numbers from 1 - 6. Then the new value is assigned as non-public variable, 
        meaning it cannot modified. 
        
        """
        new_value = random.randint(1 ,6)
        self._value = new_value
        return new_value
    
class Player:

    def __init__(self, die, is_computer=False):
        # Arguments passed when the instance is created.
        self._die = die                 
        self._is_computer = is_computer
        # This argument is not passed because it is initilized when the instance is created.
        self._counter = 10

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def die(self):
        return self._die

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()
                
class DiceGame:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def play(self):
        print("============================")
        print("🎲 Welcome to Roll he Dice!")
        print("============================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the player to the round.
        self.print_welcome()

        # Roll the dice (player and computer).
        player_value = self.player.roll_die()
        computer_value = self.computer.roll_die()

        # Show the values of the dice.
        self.show_dice(player_value, computer_value)

        # Determine winner and loser
        if player_value > computer_value:
            print("You won this round! 🎉")
            self.update_counters(winner=self.player, loser=self.computer)
        elif computer_value > player_value:
            print("The computer wont this round. Try again.")
            self.update_counters(winner=self.computer, loser=self.player)
        else:
            print("It's a tie!")

        # Show the counter of the player
        self.show_counters()
    
    def print_welcome(self):
        print("\n--------- New Round ---------")
        input("🎲 Press ay key to roll the dice. 🎲")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}\n")

    def show_counters(self):
        print(f"Your counter: {self.player.counter}")
        print(f"Computer counter: {self.computer.counter}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def check_game_over(self):
        if self.player.counter == 0:
            self.show_game_over(winner=self.player)
            return True
        elif self.computer.counter == 0:
            self.show_game_over(winner=self.computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n====================")
            print("GAME OVER")
            print("=====================")
            print("The computer won the game. Sorry...")
            print("=====================")
        else:
            print("\n====================")
            print("GAME OVER")
            print("=====================")
            print("You won the game. Congrats!")
            print("=====================")


my_die = Die()
computer_die = Die()

my_player = Player(my_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

print(my_player.die)