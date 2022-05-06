import calc
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.add(3,5), 8)
        self.assertEqual(calc.add(-3,5), 2)
        self.assertEqual(calc.add(-3,-5), -8)
    def test_factorial(self):
        self.assertEqual(calc.fact(-3),"Invalid Input")
        self.assertEqual(calc.fact(3),6)
    def test_subtraction(self):
        self.assertEqual(calc.sub(3,-3),6)
        self.assertEqual(calc.sub(3,2),1)
        self.assertEqual(calc.sub(-3,2),-5)
if __name__ == '__main__':
    unittest.main()
