import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee('Bob', 'Lee', 5000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 10000)

    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.salary, 13000)


if __name__ == '__main__':
    unittest.main()