import unittest
from io import StringIO
from unittest.mock import patch
from game import HumanPlayer, ComputerPlayer, Game

class TestHumanPlayer(unittest.TestCase):
    def test_choose_move_valid_input(self):
        with patch('builtins.input', return_value='rock\n'):
            human_player = HumanPlayer()
            move = human_player.choose_move()
            self.assertEqual(move, 'rock')

    def test_choose_move_invalid_input(self):
        with patch('builtins.input', side_effect=['invalid\n', 'rock\n']):
            human_player = HumanPlayer()
            self.assertRaises(ValueError, human_player.choose_move)

class TestComputerPlayer(unittest.TestCase):
    def test_choose_move_returns_valid_move(self):
        computer_player = ComputerPlayer()
        move = computer_player.choose_move()
        self.assertIn(move, ['rock', 'paper', 'scissors'])

class TestGame(unittest.TestCase):
    def setUp(self):
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.game = Game(self.human_player, self.computer_player)

    def test_play_tie_increment_scores(self):
        with patch('builtins.input', return_value='rock\n'):
            self.game.play()
            self.assertEqual(self.game.human_score, 0)
            self.assertEqual(self.game.computer_score, 0)

    def test_play_human_wins_increment_human_score(self):
        with patch('builtins.input', return_value='rock\n'):
            self.game.play()
            self.assertEqual(self.game.human_score, 1)

    def test_play_computer_wins_increment_computer_score(self):
        with patch('builtins.input', return_value='paper\n'):
            self.game.play()
            self.assertEqual(self.game.computer_score, 1)

if __name__ == '__main__':
    unittest.main()
