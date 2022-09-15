'''
Author: Junaid Hasseb
Editor: Alexey Chemlev
Last edited: 14-09-2022
'''

import unittest

class BowlingGame:

    def __init__(self):
        self.rolls = [] #Creates empty list 'rolls' for roll results

    def roll(self, pins):
        self.rolls.append(pins) #Adds number of hit pins for the last roll to 'rolls' list

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10 #Checks if a throw was a strike. Returns boolan value

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10 #Checks if a throw was a spare. Returns boolan value

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def score(self):
        result = 0
        rollIndex = 0  # Starts new game
        for frameIndex in range(10): #Sets rules for 10 frames
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1  # Moves to the next frame
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2  # Moves to the next frame
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2   # Moves to the next frame
        return result

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls.append(pins) # Adds rolls score to the final game score ('rolls' list)

    def testGutterGame(self): # Creates game with 20 misses
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def testAllOnes(self): # Creates game with 20 throws each hitting 1 pin
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testRandomGame(self):  # Creates game with first 2 throws hitting 10 pins combined.
        self.game.rolls.append(3)
        self.game.rolls.append(6)
        self.game.rolls.append(2)
        self.game.rolls.append(5)
        self.game.rolls.append(4)
        self.game.rolls.append(1)
        self.rollMany(0, 14)
        assert self.game.score() == 21

    def testOneSpare(self): # Creates game with first 2 throws hitting 10 pins combined.
        self.game.rolls.append(7)
        self.game.rolls.append(3)
        self.game.rolls.append(5)
        self.rollMany(0, 17)
        assert self.game.score() == 20

    def testOneStrike(self): # Creates game with first throw hitting 10 pins
        self.game.rolls.append(10)
        self.game.rolls.append(4)
        self.game.rolls.append(3)
        self.rollMany(0, 17)
        assert self.game.score() == 24

    def testAllSpares(self):  # Creates game with all 21 throw hitting 5 pins
            self.rollMany(5, 21)
            assert self.game.score() == 150

    def testPerfectGame(self): # Creates game with all 12 throw hitting 10 pins
        self.rollMany(10, 12)
        assert self.game.score() == 300



BowlingGame.frameScore.__doc__ = "A method to calculate frame score by adding 2 throw result. "
BowlingGame.roll.__doc__ = "A method to add throw results to the 'rolls' list."
BowlingGame.isStrike.__doc__ = "A method to check if a throw was a strike."
BowlingGame.isSpare.__doc__ = "A method to check if a throw was a spare."
BowlingGame.strikeScore.__doc__ = "A method to calculate frame score in a case of strike."
BowlingGame.spareScore.__doc__ = "A method to calculate frame score in a case of spare."
BowlingGame.score.__doc__ = "A method to calculate final game score."

TestBowlingGame.rollMany.__doc__ = "A method to to make many rolls with same number of hit pins."
TestBowlingGame.setUp.__doc__ = "A method to create/initialize new game."
TestBowlingGame.testGutterGame.__doc__ = "A method to test result for game with all misses."
TestBowlingGame.testAllOnes.__doc__ = "A method to test result for game with all throws hitting 1 pin."
TestBowlingGame.testRandomGame.__doc__ = "A method to test result for game with throws hitting random number of pins but with no strikes or spares."
TestBowlingGame.testOneSpare.__doc__ = "A method to test results for game with one spare."
TestBowlingGame.testOneStrike.__doc__ = "A method to test results for game with one strike."
TestBowlingGame.testPerfectGame.__doc__ = "A method to test results for the game with all strikes."
TestBowlingGame.testAllSpares.__doc__ = "A method to test results for game with all spares."
TestBowlingGame.testRandomGame.__doc__ = "A method to test results for game with no strkes or spares."