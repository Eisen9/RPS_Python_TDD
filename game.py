import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.move = None

    def choose_move(self):
        pass

class Human(Player):
    def choose_move(self):
        print("Enter your move (rock/paper/scissors): ")
        self.move = input().lower()
        while self.move not in ['rock', 'paper', 'scissors']:
            print("Invalid move. Please try again.")
            self.move = input().lower()

class Computer(Player):
    def choose_move(self):
        self.move = random.choice(['rock', 'paper', 'scissors'])

class Game:
    def __init__(self):
        self.human = Human('You')
        self.computer = Computer('Computer')

    def play_round(self):
        print(f"{self.human.name}'s move: {self.human.move}")
        print(f"{self.computer.name}'s move: {self.computer.move}")

        if self.human.move == self.computer.move:
            print("It's a tie!")
        elif (self.human.move == 'rock' and self.computer.move == 'scissors') or \
             (self.human.move == 'paper' and self.computer.move == 'rock') or \
             (self.human.move == 'scissors' and self.computer.move == 'paper'):
            print(f"{self.human.name} wins!")
            self.human.score += 1
        else:
            print(f"{self.computer.name} wins!")
            self.computer.score += 1

        print(f"Score: {self.human.name}: {self.human.score}  {self.computer.name}: {self.computer.score}")

    def play_game(self):
        print("Let's play Rock Paper Scissors!")
        while True:
            self.human.choose_move()
            self.computer.choose_move()
            self.play_round()
            print("Play again? (y/n)")
            play_again = input().lower()
            while play_again not in ['y', 'n']:
                print("Invalid input. Please enter 'y' or 'n'.")
                play_again = input().lower()
            if play_again == 'n':
                break

if __name__ == '__main__':
    game = Game()
    game.play_game()
