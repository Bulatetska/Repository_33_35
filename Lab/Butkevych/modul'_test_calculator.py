import unittest


class simpleCalculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b ):
        return a / b


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator =  simpleCalculator()

    def tearDown(self):
        print("\ntear Down executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 2)
        self.assertEqual(result, 7)
        
    def test_addition_integer_string(self):
        result = self.calculator.sum(5, '2')
        self.assertEqual(result, 'ERROR')
    
    def test_addition_negative_integers(self):
        result = self.calculator.sum(5, -2)
        self.assertEqual(result, -7)
        self.assertNotEqual(result, 3)
        
        

    def test_subtraction_two_integers(self):
        result = self.calculator.sub(5, 2)
        self.assertEqual(result, 3)
        
    def test_subtraction_integer_string(self):
        result = self.calculator.sum(5, '2')
        self.assertEqual(result, 'ERROR')
    
    def test_subtraction_negative_integers(self):
        result = self.calculator.sum(5, -2)
        self.assertEqual(result, -7)
        self.assertNotEqual(result, 7)



    def test_multiplication_two_integers(self):
        result = self.calculator.mult(8, 3)
        self.assertEqual(result, 24)
    
    def test_multiplication_integer_string(self):
        result = self.calculator.sum(8, '3')
        self.assertEqual(result, 'ERROR')
    
    def test_multiplication_negative_integers(self):
        result = self.calculator.sum(8, -3)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 5)



    def test_divide_two_integers(self):
        result = self.calculator.div(16, 4)
        self.assertEqual(result, 4)
    
    def test_divide_integer_string(self):
        result = self.calculator.sum(16, '4')
        self.assertEqual(result, 'ERROR')
    
    def test_divide_negative_integers(self):
        result = self.calculator.sum(16, -4)
        self.assertEqual(result, -20)
        self.assertNotEqual(result, 12)


if __name__ == '__main__':
    unittest.main()