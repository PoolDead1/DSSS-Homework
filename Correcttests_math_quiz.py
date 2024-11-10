import unittest
from math_quiz import generate_number, generate_operator, generate_mathematic_problem_and_answer

class TestMathGame(unittest.TestCase):

    def test_generate_number(self):
        # Test if generated numbers are within the specified range
        min_val, max_val = 1, 10
        for _ in range(1000):  # Run multiple times to check random values
            rand_num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Generated number is out of bounds")

    def test_generate_operator(self):
        # Test if generated operators are among the allowed operators
        allowed_operators = ['+', '-', '*']
        for _ in range(1000):  # Test multiple times to check random selection
            operator = generate_operator()
            self.assertIn(operator, allowed_operators, "Generated operator is not among allowed operators")

    def test_generate_mathematic_problem_and_answer(self):
        # Define test cases with expected problem strings and answers
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            (10, 0, '+', '10 + 0', 10),
            (8, 2, '-', '8 - 2', 6),
            (3, 3, '*', '3 * 3', 9),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_mathematic_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "Problem string does not match expected format")
            self.assertEqual(answer, expected_answer, "Answer does not match expected result")

if __name__ == "__main__":
    unittest.main()
