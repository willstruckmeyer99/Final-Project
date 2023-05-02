import pandas as pd
import random
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import unittest

class MonteCarloTestSuite(unittest.TestCase):
    
    def test_1_change_weight(self):
        obj = Die([1,2,3])
        obj.change_weight(2, 3.0)
        test_list = [1.0, 3.0, 1.0]
        expected = True
        self.assertEqual(obj.W .equals(test_list), expected)
        
    def test_2_change_weight(self):
        obj = Die([1,2,3])
        obj.change_weight(2, 3)
        test_list = [1.0, 1.0, 1.0]
        expected = True
        self.assertEqual(obj.W.equals(test_list), expected)
        
    def test_3_change_weight(self):
        obj = Die([1,2,3])
        obj.change_weight(4, 3.0)
        test_list = [1.0, 1.0, 1.0]
        expected = True
        self.assertEqual(obj.W.equals(test_list), expected)
        
    def test_4_roll(self):
        obj = Die([1,2,3,4,5,6])
        output = obj.roll(3)
        expected = 3
        self.assertEqual(len(output), expected)
        
    def test_5_roll(self):
        obj = Die([1,2,3,4,5,6])
        output = obj.roll()[0]
        expected = True
        self.assertEqual(output in obj.faces)
        
    def test_6_show_die(self):
        obj = Die([1,2,3])
        test_df = pd.DataFrame({
            'face' : [1,2,3],
            'weight' : [1.0,1.0,1.0]
        })
        expected = True
        self.assertEqual(obj.show_die().equals(test_df), expected)
        
    def test_7_play(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        obj = Game(dice)
        obj.play(4)
        test_tuple = (3, 4)
        expected = True
        self.assertEqual(obj.playdf.shape.equals(test_tuple), expected)
        
    def test_8_show_game(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        obj = Game(dice)
        obj.play(4)
        test_tuple(3, 4)
        expected = True
        self.assertEqual(obj.show_game().shape.equals(test_tuple), expected)
        
    def test_9_show_game(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        obj = Game(dice)
        obj.play(4)
        test_tuple(12, 2)
        expected = True
        self.assertEqual(obj.show_game('narrow').shape.equals(test_tuple), expected)
        
    def test_10_jackpot(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        game = Game(dice)
        game.play(4)
        game.playdf = pd.DataFrame({
            1 : [1,1,2],
            2 : [2,2,3],
            3 : [1,3,1],
            4 : [3,2,2]
        })
        game.playdf.index += 1
        obj = Analyzer(game)
        espected = 0
        self.assertEqual(obj.jackpot(), expected)
        
    def test_11_jackpot(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        game = Game(dice)
        game.play(4)
        game.playdf = pd.DataFrame({
            1 : [1,1,2],
            2 : [2,2,3],
            3 : [1,1,1],
            4 : [3,2,2]
        })
        game.playdf.index += 1
        obj = Analyzer(game)
        espected = 1
        self.assertEqual(obj.jackpot(), expected)
        
    def test_12_combo(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        game = Game(dice)
        game.play(4)
        game.playdf = pd.DataFrame({
            1 : [1,1,2],
            2 : [2,2,3],
            3 : [1,3,1],
            4 : [3,2,2]
        })
        game.playdf.index += 1
        obj = Analyzer(game)
        test_tuple = (4, 2)
        espected = True
        self.assertEqual(obj.combo().shape.equals(test_tuple), expected)
    
    def test_13_combo(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        game = Game(dice)
        game.play(4)
        game.playdf = pd.DataFrame({
            1 : [1,1,2],
            2 : [1,1,2],
            3 : [1,3,1],
            4 : [1,3,1]
        })
        game.playdf.index += 1
        obj = Analyzer(game)
        test_tuple = (2, 2)
        espected = True
        self.assertEqual(obj.combo().shape.equals(test_tuple), expected)
        
    def test_14_face_count(self):
        die1 = Die([1,2,3])
        die2 = Die([1,2,3])
        die3 = Die([1,2,3])
        dice = [die1, die2, die3]
        game = Game(dice)
        game.play(4)
        game.playdf = pd.DataFrame({
            1 : [1,1,2],
            2 : [2,3,3],
            3 : [1,3,1],
            4 : [3,2,2]
        })
        game.playdf.index += 1
        obj = Analyzer(game)
        test_df = pd.DataFrame({
            1 : [2,0,2,0],
            2 : [1,1,0,2],
            3 : [0,2,1,1]
        })
        test_df.index += 1
        espected = True
        self.assertEqual(obj.face_count().equals(test_df), expected)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)