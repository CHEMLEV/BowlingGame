# File 1 (Test.py)
# This file has information about test cases which you need to test.
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
        print(self.game.score())
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        print(self.game.score())
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.rolls.append(7)
        self.game.rolls.append(3)
        self.game.rolls.append(5)
        self.rollMany(0, 17)
        print(self.game.score())
        assert self.game.score() == 20

    def testOneStrike(self):
        self.game.rolls.append(10)
        self.game.rolls.append(4)
        self.game.rolls.append(3)
        self.rollMany(0, 17)
        print(self.game.score())
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        print(self.game.score())
        assert self.game.score() == 300

    def testAllSpares(self):
        def testOneSpare(self):
            self.rollMany(5, 21)
            assert self.game.score() == 150


# File 2 (BowlingGame.py)
# This file has information about Bowling Game for which the description is provided in project assessment.

# Your tasks for code parts:
# 1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
# 2: Refactor the code (Improve its structure without changing external behaviour).
# 3: Report everything using github commits and versioning control.

###### Important #####
