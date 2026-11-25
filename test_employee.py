from employee import employee_info

def test_employee_info():
    result = employee_info("Tanushree", 266, "IT", 30000)

    expected = ("Employee Name: Tanushree\n"
                "Employee ID: 266\n"
                "Department: IT\n"
                "Salary: 30000")

    assert result == expected