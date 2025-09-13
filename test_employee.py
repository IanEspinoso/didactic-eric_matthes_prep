import pytest
from employee_lib import Employee

@pytest.fixture
def employee_for_tests():
    """An employee instance that will be available for all tests."""
    tested_employee = Employee('Jon', 'Doe', 1000)
    return tested_employee

def test_give_default_raise(employee_for_tests):
    """Tests the employee class by using the standard increase."""
    new_salary = employee_for_tests.give_raise()
    assert new_salary == 6000

def test_give_custom_raise(employee_for_tests):
    """Tests the employee class by incrementing the salary in 1."""
    new_salary = employee_for_tests.give_raise(1)
    assert new_salary == 1001