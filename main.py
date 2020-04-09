from datetime import date
from application import salary
from application.db.people import get_employees


def format_date():
    d = date.today()
    print(f'{d.day}.{d.month}.{d.year}')


if __name__ == '__main__':
    print('Start')
    format_date()
    new_employee = get_employees('Ivan')
    salery_Ivan = salary.calculate_salary(2500)
    print('Finish')