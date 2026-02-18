import unittest
from src.expense import Expense

class TestExpense(unittest.TestCase):
    def test_creation(self):
        e = Expense(100, "Food", "2026-01-01", "Test")
        self.assertEqual(e.amount, 100.0)

if __name__ == "__main__":
    unittest.main()
