import unittest
from challenge import target_pair

class TestTargetPair(unittest.TestCase):

    """
        This class tests for all posible scenerio of input
        and target
    """
    def test_target_pair(self):
        """
            Test that there is a pair in the array that
            when summed equal to the target
        """
        input = [2, 3, 5, 2, 1]
        target = 7
        self.assertEqual(target_pair(input, target), True, "Should be True")

    
    def test_target_greater_than_zero(self):
        """
            Test that the target is greater than 1
        """
        input = [2, 3, 5, 2, 1]
        target1 = 0
        target2 = -1
        self.assertEqual(target_pair(input, target1), False, "Should be False. Target cannot be less than 1")
        self.assertEqual(target_pair(input, target2), False, "Should be False. Target cannot be less that 1")


    def test_no_target_pair(self):
        """
            Test that there is no pair in the array that equals to the target
        """
        input = [2, 3, 5, 2, 1]
        target = 10
        self.assertEqual(target_pair(input, target), False, "Should be False. No target pair")

        
if __name__ == "__main__":
    unittest.main()   