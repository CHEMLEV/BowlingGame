'''Autor: Junaid Hasseb
Editor: Alexey Chemlev
Last edited on 14-09-2022
'''

import unittest

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls.append(pins)

    def testGutterGame(self):
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.rolls.append(7)
        self.game.rolls.append(3)
        self.game.rolls.append(5)
        self.rollMany(0, 17)
        assert self.game.score() == 20

    def testOneStrike(self):
        self.game.rolls.append(10)
        self.game.rolls.append(4)
        self.game.rolls.append(3)
        self.rollMany(0, 17)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
                assert self.game.score() == 300

    def testAllSpares(self):
        def testOneSpare(self):
            self.rollMany(5, 21)
            assert self.game.score() == 150

'''
BowlingGame.roll.__doc__= "A function to add trow results to the 'rolls' list"
BowlingGame.frameScore.__doc__= "A function to calculate frame score by adding next trow results"
'''