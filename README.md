# RPS_Python_TDD

## `game.py` summary and explanation.
> We define two classes, `Human` and `Computer`, which inherit from the base class `Player`. Each player has a name, `score`, and `move` attributes. The `choose_move` method is overridden in the subclasses to prompt the human player for input or randomly choose a move for the computer player.

> We define a `Game` class which contains two player objects, `human` and `computer`. The `play_round` method compares the moves chosen by each player and updates the score accordingly. 

> The `play_game` method prompts the player to play another round or exit the game, and loops until the player chooses to exit.

> The `if __name__ == '__main__':` block at the bottom of the file creates a new `Game` object and starts the game.

## `game_test.py` summary and explanation.
* We use the built-in `unittest` module to write the unit tests.
* We create a `StringIO` object to simulate user input for the `HumanPlayer` tests.
* We use the `@patch` decorator to replace the `input()` function with our `StringIO` object.
* We use `self.assertRaises()` to test that the `HumanPlayer` class raises a `ValueError` when the user inputs an invalid move.
* We test the `ComputerPlayer` class by asserting that the move returned is one of the three valid moves.
* We test the `Game` class by simulating user input and asserting that the scores are incremented correctly based on the game outcome.
* To run these tests, we save them in a file named `test_game.py` (or any other valid identifier ending in `.py`) in the same directory as the `game.py` file. Then, run the command `python -m unittest test_game.py` from the command line to execute the tests.