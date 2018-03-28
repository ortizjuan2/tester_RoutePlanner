import unittest

from helpers import load_map, show_map
import student_code

class BeginnerTestCase(unittest.TestCase):

    def setUp(self):
        # call before every test case
        self.M = load_map('map-40.pickle')
        self.shortest_path = student_code.shortest_path

    def tearDown(self):
        pass

    def testA(self):
        # first test case, note all test cases must begin with test
        start = 5
        goal = 5
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [5], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testB(self):
        start = 5
        goal = 34
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [5, 16, 37, 12, 34], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testC(self):
        start = 34
        goal = 5
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [34, 12, 37, 16, 5], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testD(self):
        start = 8
        goal = 24
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [8, 14, 16, 37, 12, 17, 10, 24], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testE(self):
        start = 24
        goal = 8
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [24, 10, 17, 12, 37, 16, 14, 8], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

class AdvanceTestCases(unittest.TestCase):

    def setUp(self):
        self.M = load_map('map-1000.pickle')
        self.shortest_path = student_code.shortest_path
    
    def tearDown(self):
        pass

    def testA(self):
        start = 0
        goal = 999
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [0, 99, 198, 297, 396, 429, 440, 444, 555, 666, 777, 888, 999], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testB(self):
        start = 999
        goal = 0
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [999, 888, 777, 666, 555, 444, 440, 429, 396, 297, 198, 99, 0], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

    def testC(self):
        start = 0
        goal = 271
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise

class ExpertTestCases(unittest.TestCase):

    def setUp(self):
        self.M = load_map('map-10000.pickle')
        self.shortest_path = student_code.shortest_path

    def tearDown(self):
        pass


    def testA(self):
        start = 0
        goal = 9999
        try:
            answer = self.shortest_path(self.M, start, goal)
            assert answer == [0, 1666, 3332, 4998, 6664, 8330, 9996, 9999], "Returning path is not correct!"
        except AssertionError as e:
            e.args += (answer)
            raise
    


if __name__ == "__main__":
    unittest.main() # Run all test cases
