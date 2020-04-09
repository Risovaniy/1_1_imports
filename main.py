from datetime import date
from application import salary
from application.db.people import get_employees


if __name__ == '__main__':
    print('Start')
    d = date.today().strftime("%d.%m.%Y")
    print(d)
    new_employee = get_employees('Ivan')
    salery_Ivan = salary.calculate_salary(2500)
    print('Finish')