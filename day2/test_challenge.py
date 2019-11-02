import unittest
from challenge import product_of_elements

class TestProductOfElements(unittest.TestCase):
    """
        This class tests for all posible scenerio of input
    """
    def test_product_of_elements(self):
        input1 = [1, 2, 3, 4, 5]
        input2 = [3, 2, 1]
        input3 = [1, 2, 3, 4, 5, 5]
        output1 = [120, 60, 40, 30, 24]
        output2 = [2, 3, 6]
        output3 = [600, 300, 200, 150, 120, 120]
        self.assertEqual(product_of_elements(input1), output1, "Should be [120, 60, 40, 30, 24]")
        self.assertEqual(product_of_elements(input2), output2, "Should be [2, 3, 6]")
        self.assertEqual(product_of_elements(input3), output3, "Should be [600, 300, 200, 150, 120, 120]")

    def test_input_lenght(self):
        input = [1, 2]
        self.assertEqual(product_of_elements(input), False)
    


if __name__ == "__main__":
    unittest.main()