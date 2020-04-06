from application import salary
from application.people import get_employees


if __name__ == '__main__':
    print('Start\n')
    new_employee = get_employees('Ivan')
    salery_Ivan = salary.calculate_salary(2500)
    print('Finish')