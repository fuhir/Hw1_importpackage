from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees
from application.ya_music_rnd.yarndmusic import main

if __name__ == '__main__':
    print(date.today())
    calculate_salary()
    get_employees()
    main()
